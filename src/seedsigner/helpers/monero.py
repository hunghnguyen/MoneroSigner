from monero.seed import Seed
from monero.wallet import Wallet
from monero.backends.offline import OfflineWallet
from monero.transaction import Transaction


def sign_transaction(seed: Seed, unsigned_transaction: Transaction) -> Transaction:
    wallet = Wallet(OfflineWallet(seed=seed))
    return wallet.sign_transaction(unsigned_transaction)
