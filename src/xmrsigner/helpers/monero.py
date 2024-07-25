from monero.wallet import Wallet
from monero.backends.offline import OfflineWallet
from monero.transaction import Transaction
from requests.exceptions import ConnectionError
from monero.backends.jsonrpc.exceptions import RPCError
from typing import Optional, Union
from binascii import hexlify


def sign_transaction(wallet: Wallet, unsigned_transaction: Transaction) -> Transaction:
    return wallet.sign_transaction(unsigned_transaction)


class WalletRpcWrapper:

    wallet: Optional[Wallet] = None

    def __init__(self, wallet: Wallet):
        self.wallet = wallet

    def get_encrypted_key_images(self) -> Optional[str]:
        try:
            result = self.wallet._backend.raw_request('export_encrypted_key_images')
            print(result)
            if 'encrypted_key_images_blob' in result:
                return result['encrypted_key_images_blob']
        except ConnectionError as ce:
            print(f'WalletRpcWrapper.get_encrypted_key_images(): {ce}')
            raise ce
        except RPCError as re:
            print(f'WalletRpcWrapper.get_encrypted_key_images(): {re}')
            raise re
        return None

    def update_outputs(self, outputs: Union[str, bytes]) -> Optional[int]:
        try:
            result = self.wallet._backend.raw_request('import_outputs', {'outputs_data_hex': hexlify(outputs).decode() if type(outputs) == bytes else outputs})
            print(result)
            if 'num_imported' in result and result['num_imported'] > 0:
                return result['num_imported']
        except ConnectionError as ce:
            print(f'WalletRpcWrapper.update_outputs(): {ce}')
            raise ce
        except RPCError as re:
            print(f'WalletRpcWrapper.update_outputs(): {re}')
        return None
