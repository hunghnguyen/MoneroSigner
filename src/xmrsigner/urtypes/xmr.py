from urtypes import RegistryType, Bytes

XMR_OUTPUT = RegistryType('xmr-output', 610)
XMR_KEY_IMAGE = RegistryType('xmr-keyimage', 611)
XMR_TX_UNSIGNED = RegistryType('xmr-txunsigned', 612)
XMR_TX_SIGNED = RegistryType('xmr-txsigned', 613)


class XmrOutput(Bytes):

    @classmethod
    def register_type(cls):
        return XMR_OUTPUT


class XmrKeyImage(Bytes):

    @classmethod
    def register_type(cls):
        return XMR_KEY_IMAGE


class XmrTxUnsigned(bytes):

    @classmethod
    def register_type(cls):
        return XMR_TX_UNSIGNED


class XmrTxSigned(bytes):

    @classmethod
    def register_type(cls):
        return XMR_TX_SIGNED
