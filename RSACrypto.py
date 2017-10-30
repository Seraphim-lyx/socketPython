import rsa
from Crypto import Crypto


class RSACrypto(Crypto):
    """RSARrypto Module"""

    def __init__(self, message):
        # super(RSACrypto, self).__init__()
        self.length = 1024  # key length
        self.poorSize = 8  # 2 * computer core number
        self.message = message
        self.encryptMsg = []
        self.decryptMsg = []
        (self.pubKey, self.priKey) = rsa.newkeys(
            self.length, self.poorSize)  # keyPair generation

    def encrypt(self):

        for m in self.message:
            self.encryptMsg.append(rsa.encrypt(m.encode("utf8"), self.pubKey))

    def decrypt(self):

        for m in self.encryptMsg:
            self.decryptMsg.append(rsa.decrypt(m, self.priKey).decode("utf8"))

    def getEncryptMsg(self):
        return self.encryptMsg

    def getDecryptMsg(self):
        return self.decryptMsg

if __name__ == '__main__':
    r = RSACrypto("abc")
    print(r.pubKey)
