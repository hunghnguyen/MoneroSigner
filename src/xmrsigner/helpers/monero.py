from monero.wallet import Wallet
from monero.backends.offline import OfflineWallet
from monero.transaction import Transaction


def sign_transaction(wallet: Wallet, unsigned_transaction: Transaction) -> Transaction:
    return wallet.sign_transaction(unsigned_transaction)
