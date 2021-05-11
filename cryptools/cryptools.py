import string


class Cipher:
    def __init__(self):
        super().__init__()

    def encode(self, plaintext: str) -> str:
        raise NotImplementedError

    def decode(self, ciphertext: str) -> str:
        raise NotImplementedError


class AtbashCipher(Cipher):
    def __init__(self):
        super().__init__()
        self._table = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])

    def encode(self, plaintext: str) -> str:
        return str.translate(plaintext.upper(), self._table)

    def decode(self, ciphertext: str) -> str:
        return str.translate(ciphertext.upper(), self._table)
