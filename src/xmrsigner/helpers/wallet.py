from subprocess import Popen, TimeoutExpired, DEVNULL
from os import path
from signal import SIGTERM, SIGKILL
from time import sleep
from psutil import Process
from monero.const import NET_MAIN, NET_TEST, NET_STAGE


class MoneroWalletRPCManager:

    def __init__(self):
        self.networks = [NET_MAIN, NET_TEST, NET_STAGE]
        self.daemon_path = '/usr/bin/monero-wallet-rpc'
        self.pidfile_base = '/tmp/monero-wallet-rpc'
        self.processes = {}

    def _get_command(self, network):
        port = {NET_MAIN: 18082, NET_TEST: 28082, NET_STAGE: 38082}[network]
        return [
            self.daemon_path,
            '--offline',
            f'--rpc-bind-port={port}',
            '--wallet-dir=/tmp',
            '--rpc-login=monero:monero',
            f'--{network}',
            f'--log-file=/tmp/monero-wallet-rpc-{network}.log'
        ]

    def start_daemon(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        if self.is_daemon_running(network):
            return True

        cmd = self._get_command(network)
        process = Popen(cmd, stdout=DEVNULL, stderr=DEVNULL)
        self.processes[network] = process

        # Wait a bit to ensure the process started
        sleep(1)
        return self.is_daemon_running(network)

    def stop_daemon(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        if not self.is_daemon_running(network):
            return True

        process = self.processes.get(network)
        if process:
            process.terminate()
            try:
                process.wait(timeout=10)
            except TimeoutExpired:
                process.kill()
            
            del self.processes[network]

        return not self.is_daemon_running(network)

    def restart_daemon(self, network):
        self.stop_daemon(network)
        return self.start_daemon(network)

    def is_daemon_running(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        process = self.processes.get(network)
        if process:
            return process.poll() is None
        return False

    def get_all_daemon_statuses(self):
        return {network: self.is_daemon_running(network) for network in self.networks}

    def get_daemon_resource_usage(self, network):
        if not self.is_daemon_running(network):
            return None
        
        process = Process(self.processes[network].pid)
        return {
            'cpu_percent': process.cpu_percent(interval=1),
            'memory_info': process.memory_info(),
            'num_threads': process.num_threads(),
            'connections': len(process.connections())
        }

    def cleanup(self):
        for network in self.networks:
            self.stop_daemon(network)
