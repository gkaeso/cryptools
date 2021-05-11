import unittest

import cryptools.cryptools as cryptools


class TestCaesar(unittest.TestCase):

    def setUp(self) -> None:
        self.plaintext_only_letters = 'This message shall remain private'
        self.ciphertexts_only_letters = {
            0: 'THIS MESSAGE SHALL REMAIN PRIVATE',
            1: 'UIJT NFTTBHF TIBMM SFNBJO QSJWBUF',
            2: 'VJKU OGUUCIG UJCNN TGOCKP RTKXCVG',
            3: 'WKLV PHVVDJH VKDOO UHPDLQ SULYDWH',
            4: 'XLMW QIWWEKI WLEPP VIQEMR TVMZEXI',
            5: 'YMNX RJXXFLJ XMFQQ WJRFNS UWNAFYJ',
            6: 'ZNOY SKYYGMK YNGRR XKSGOT VXOBGZK',
            7: 'AOPZ TLZZHNL ZOHSS YLTHPU WYPCHAL',
            8: 'BPQA UMAAIOM APITT ZMUIQV XZQDIBM',
            9: 'CQRB VNBBJPN BQJUU ANVJRW YAREJCN',
            10: 'DRSC WOCCKQO CRKVV BOWKSX ZBSFKDO',
            11: 'ESTD XPDDLRP DSLWW CPXLTY ACTGLEP',
            12: 'FTUE YQEEMSQ ETMXX DQYMUZ BDUHMFQ',
            13: 'GUVF ZRFFNTR FUNYY ERZNVA CEVINGR',
            14: 'HVWG ASGGOUS GVOZZ FSAOWB DFWJOHS',
            15: 'IWXH BTHHPVT HWPAA GTBPXC EGXKPIT',
            16: 'JXYI CUIIQWU IXQBB HUCQYD FHYLQJU',
            17: 'KYZJ DVJJRXV JYRCC IVDRZE GIZMRKV',
            18: 'LZAK EWKKSYW KZSDD JWESAF HJANSLW',
            19: 'MABL FXLLTZX LATEE KXFTBG IKBOTMX',
            20: 'NBCM GYMMUAY MBUFF LYGUCH JLCPUNY',
            21: 'OCDN HZNNVBZ NCVGG MZHVDI KMDQVOZ',
            22: 'PDEO IAOOWCA ODWHH NAIWEJ LNERWPA',
            23: 'QEFP JBPPXDB PEXII OBJXFK MOFSXQB',
            24: 'RFGQ KCQQYEC QFYJJ PCKYGL NPGTYRC',
            25: 'SGHR LDRRZFD RGZKK QDLZHM OQHUZSD',
            26: 'THIS MESSAGE SHALL REMAIN PRIVATE',
        }

    def test_encode(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).encode(
                self.plaintext_only_letters), self.ciphertexts_only_letters[i]
            )

    def test_decode(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).decode(
                self.ciphertexts_only_letters[i]), self.plaintext_only_letters.upper()
            )


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
