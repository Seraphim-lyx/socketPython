import RSACrypto.RSACrypto
import AESCrypto.AESCrypto


class Crypto(object):
    """docstring for Crypto"""

    def __init__(self, encrypt, message):

        self.encrypt = encrypt
        self.message = message

    def getEncrypto(self):

        if self.encrypt is "RSA":
            return RSACrypto(self.message)
        elif self.encrypt is "AES":
            return AESCrypto(self.message)
