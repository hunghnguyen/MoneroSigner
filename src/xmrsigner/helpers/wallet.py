from subprocess import run
from os import path, kill


class MoneroWalletRPCManager:

    def __init__(self):
        self.networks = ['main', 'test', 'stage']
        self.init_script = '/etc/init.d/S99monero-wallet-rpc'
        self.pidfile_base = '/tmp/monero-wallet-rpc'

    def start_daemon(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        cmd = [self.init_script, 'start', network]
        result = run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def stop_daemon(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        cmd = [self.init_script, 'stop', network]
        result = run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def restart_daemon(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        cmd = [self.init_script, 'restart', network]
        result = run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def is_daemon_running(self, network):
        if network not in self.networks:
            raise ValueError(f"Invalid network: {network}")
        
        pidfile = f"{self.pidfile_base}-{network}.pid"
        if not path.exists(pidfile):
            return False
        
        with open(pidfile, 'r') as f:
            pid = f.read().strip()
        
        try:
            kill(int(pid), 0)
            return True
        except OSError:
            return False

    def get_all_daemon_statuses(self):
        return {network: self.is_daemon_running(network) for network in self.networks}
