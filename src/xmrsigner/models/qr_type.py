class QRType:
    '''
    Used with DecodeQR and EncodeQR to communicate qr encoding type
    '''
    UR2 = 'ur2'

    SEED__SEEDQR = 'seed__seedqr'
    SEED__COMPACTSEEDQR = 'seed__compactseedqr'
    SEED__UR2 = 'seed__ur2'
    SEED__MNEMONIC = 'seed__mnemonic'
    SEED__FOUR_LETTER_MNEMONIC = 'seed__four_letter_mnemonic'

    SETTINGS = 'settings'

    MONERO_ADDRESS = 'monero_address'
    MONERO_WALLET = 'monero_wallet'
    XMR_OUTPUT_UR = 'xmr__output__ur'
    XMR_KEYIMAGE_UR = 'xmr__keyimage__ur'
    XMR_TX_UNSIGNED_UR = 'xmr__unsigned__tx__ur'
    XMR_TX_SIGNED_UR = 'xmr__signed__tx_ur'

    SIGN_MESSAGE = "sign_message"

    WALLET_VIEW_ONLY = 'wallet__view__only'
    WALLET_VIEW_ONLY_JSON = 'wallet__view__only__json'
    WALLET__UR = 'wallet__ur'
    WALLET__CONFIGFILE = 'wallet__configfile'
    WALLET__GENERIC = 'wallet__generic'
    OUTPUT__UR = 'output__ur'
    ACCOUNT__UR = 'account__ur'
    BYTES__UR = 'bytes__ur'

    INVALID = 'invalid'
