import unittest
import uuid

import cryptools.cryptools as cryptools


class TestBase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.keys: list[str] = [str(uuid.uuid4()), str(uuid.uuid4())]

    def tearDown(self) -> None:
        super().tearDown()
        self.keys.clear()


class TestCipher(TestBase):

    def test_constructor(self) -> None:
        cryptools.Cipher()

    def test_encode(self) -> None:
        with self.assertRaises(NotImplementedError):
            cryptools.Cipher().encode('plaintext')

    def test_encode(self) -> None:
        with self.assertRaises(NotImplementedError):
            cryptools.Cipher().decode('ciphertext')
