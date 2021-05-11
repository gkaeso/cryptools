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


class CaesarCipher(Cipher):

    def __init__(self, key: int):
        super().__init__()
        self.key: int = key

    def _process(self, text: str, key: int) -> str:
        processed_text: list[str] = []

        for char in text.upper():
            if char.isalpha():
                index: int = ord(char) + key % 26
                if index > ord('Z'):
                    index = index - 26
                processed_text.append(chr(index))
            else:
                processed_text.append(char)

        return ''.join(processed_text)

    def encode(self, plaintext: str) -> str:
        return self._process(plaintext, self.key) if self.key != 0 else plaintext.upper()

    def decode(self, ciphertext: str) -> str:
        return self._process(ciphertext, -1 * self.key)
