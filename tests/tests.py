import unittest

import cryptools.cryptools as cryptools


class TestAtbash(unittest.TestCase):

    def test_encode_only_letters(self) -> None:
        plaintext, ciphertext = 'This message shall remain private', 'GSRH NVHHZTV HSZOO IVNZRM KIREZGV'
        self.assertEqual(cryptools.AtbashCipher().encode(plaintext), ciphertext)

    def test_decode_only_letters(self) -> None:
        plaintext, ciphertext = 'THIS MESSAGE SHALL REMAIN PRIVATE', 'gsrh nvhhztv hszoo ivnzrm kirezgv'
        self.assertEqual(cryptools.AtbashCipher().decode(ciphertext), plaintext)

    def test_encode_any_character(self) -> None:
        plaintext, ciphertext = '#>This messag@ shall rema5!in private!', '#>GSRH NVHHZT@ HSZOO IVNZ5!RM KIREZGV!'
        self.assertEqual(cryptools.AtbashCipher().encode(plaintext), ciphertext)

    def test_decode_any_character(self) -> None:
        plaintext, ciphertext = '#>THIS MESSAG@ SHALL REMA5!IN PRIVATE!', '#>gsrh nvhhzt@ hszoo ivnz5!rm kirezgv!'
        self.assertEqual(cryptools.AtbashCipher().decode(ciphertext), plaintext)


class TestCipher(unittest.TestCase):

    def test_constructor(self) -> None:
        cryptools.Cipher()

    def test_encode(self) -> None:
        with self.assertRaises(NotImplementedError):
            cryptools.Cipher().encode('plaintext')

    def test_decode(self) -> None:
        with self.assertRaises(NotImplementedError):
            cryptools.Cipher().decode('ciphertext')
