from subprocess import Popen, TimeoutExpired, DEVNULL, run
from os import path
from signal import SIGTERM, SIGKILL
from time import sleep
from psutil import Process
from monero.const import NET_MAIN, NET_TEST, NET_STAGE
from re import search
from monero.backends import jsonrpc
from monero.seed import Seed
from typing import Optional, Tuple


WALLET_PORTS = {
    NET_MAIN: 18082,
    NET_TEST: 28082,
    NET_STAGE: 38082
}

WALLET_DAEMON_PATH = '/usr/bin/monero-wallet-rpc'
PIDFILE_BASE_PATH = '/tmp/monero-wallet-rpc'


class MoneroWalletRPCManager:

    def __init__(self, daemon_path: Optional[str] = None, pidfile_base_path: Optional[str] = None):
        self.networks = [NET_MAIN, NET_TEST, NET_STAGE]
        self.daemon_path = daemon_path or WALLET_DAEMON_PATH
        self.pidfile_base = pidfile_base_path or PIDFILE_BASE_PATH
        self.processes = {}

    def _get_command(self, network):
        port = WALLET_PORTS[network]
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

    def get_version_string(self) -> Optional[str]:
        try:
            result = run([self.daemon_path, '--version'], capture_output=True, text=True, timeout=10)
            version_string = result.stdout.strip()
            print(version_string)
            version = search(r'v(\d+.\d+.\d+.\d+)', version_string)
            if version:
                return version.group(1)
        except Exception as e:
            print(f'Error retrieving Monero version: {e}')
        return None

    def get_version(self) -> Optional[Tuple[int, int, int]]:
        version = self.get_version_string()
        if version:
            version = version.split('.')
            return (int(version[0]), int(version[1]), int(version[2]), int(version[3]))
        return None

    def load_wallet_from_seed(self, seed: Seed):
        wallet = jsonrpc.JSONRPCWallet(f'http://127.0.0.1:{WALLET_PORTS[seed.network]}')
        wallet.raw_request('restore_deterministic_wallet', {'restore_height': seed.height, 'filename': seed.fingerprint, 'seed': seed.mnemonic_str})
        return wallet

    def load_wallet(
            self,
            network: str,
            wallet_name: str,
            public_address: str,
            view_key: str,
            spend_key: str,
            restore_height: int = 0,
            password: Optional[str] = None
        ):
        wallet = jsonrpc.JSONRPCWallet(f'http://127.0.0.1:{WALLET_PORTS[network]}')
        wallet.raw_request('open_wallet', {'filename': wallet_name})
        wallet.raw_request('generate_from_keys', {'filename': wallet_name, 'address': public_address, 'viewkey': view_key, 'spendkey': spend_key, 'seed': seed_key})
        return wallet

    def close_wallet(self, network: str):
        wallet = jsonrpc.JSONRPCWallet(f'http://127.0.0.1:{WALLET_PORTS[network]}')
        wallet.raw_request('close_wallet')
