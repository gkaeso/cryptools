class Cipher:
    def __init__(self):
        super().__init__()

    def encode(self, plaintext: str) -> str:
        raise NotImplementedError

    def decode(self, ciphertext: str) -> str:
        raise NotImplementedError
