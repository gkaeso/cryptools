import string


class Cipher:
    """
    This is the parent cipher class.

    This class should not be instantiated.
    """
    def __init__(self):
        super().__init__()

    def encode(self, plaintext: str) -> str:
        """
        This method encodes the input text.

        In this method should be the logic necessary to transform the initial plain text into its ciphered version.

        :argument: plaintext (str)
            The text to cipher.

        :return: (str)
            The ciphered text.
        """
        raise NotImplementedError

    def decode(self, ciphertext: str) -> str:
        """
        This method decodes the input text.

        In this method should be the logic necessary to transform the initial ciphered text into its plain version.

        :argument: ciphertext (str)
            The text to decipher.

        :return: (str)
            The plain text.
        """
        raise NotImplementedError


class AtbashCipher(Cipher):
    """
    Atbash cipher.

    This is a mono-alphabetic substitution cipher.

    The plain text alphabet is reversed to create the cipher text alphabet. In other words, the first letter of the \
    alphabet is encrypted to the last letter of the alphabet, the second letter to the penultimate letter and so forth.

    e.g. A becomes Z, B becomes Y, C becomes X, ...

    It is a variant of the affine cipher, for which the multiplicative key equals 1 and the additive key equals 25.
    """
    def __init__(self):
        super().__init__()
        self._table = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])

    def encode(self, plaintext: str) -> str:
        """
        This method encodes the input text.

        In this method should be the logic necessary to transform the initial plain text into its ciphered version.

        :argument: plaintext (str)
            The text to cipher.

        :return: (str)
            The ciphered text.
        """
        return str.translate(plaintext.upper(), self._table)

    def decode(self, ciphertext: str) -> str:
        """
        This method decodes the input text.

        In this method should be the logic necessary to transform the initial ciphered text into its plain version.

        :argument: ciphertext (str)
            The text to decipher.

        :return: (str)
            The plain text.
        """
        return str.translate(ciphertext.upper(), self._table)


class CaesarCipher(Cipher):
    """
    Caesar cipher.

    This is a mono-alphabetic substitution cipher.

    The plain text alphabet is shifted to create the cipher text alphabet. In other words, any letter L of the alphabet\
    is encrypted to the L+Nth letter of the same alphabet (where N is the input key).

    e.g. if key = 1 then A becomes B, B becomes C, C becomes D, ...
    e.g. if key = 3 then A becomes D, B becomes E, C becomes F, ...

    It is a variant of the affine cipher, for which the multiplicative key equals 1 \
    and the additive key equals the input key.
    """
    def __init__(self, key: int):
        super().__init__()
        self.key: int = key

    def _process(self, text: str, decode: bool) -> str:
        processed_text: list[str] = []

        key: int = self.key if not decode else -1 * self.key

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
        """
        This method encodes the input text.

        In this method should be the logic necessary to transform the initial plain text into its ciphered version.

        :argument: plaintext (str)
            The text to cipher.

        :return: (str)
            The ciphered text.
        """
        return self._process(plaintext, decode=False) if self.key != 0 else plaintext.upper()

    def decode(self, ciphertext: str) -> str:
        """
        This method decodes the input text.

        In this method should be the logic necessary to transform the initial ciphered text into its plain version.

        :argument: ciphertext (str)
            The text to decipher.

        :return: (str)
            The plain text.
        """
        return self._process(ciphertext, decode=True)
