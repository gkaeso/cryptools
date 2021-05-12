import unittest

import cryptools.cryptools as cryptools


class TestAffine(unittest.TestCase):

    def setUp(self) -> None:
        self.plaintext_only_letters = 'This message shall remain private'
        self.ciphertexts_only_letters = {
            '3-1': 'GWZD LNDDBTN DWBII ANLBZO UAZMBGN',
            '3-2': 'HXAE MOEECUO EXCJJ BOMCAP VBANCHO',
            '5-7': 'YQVT PBTTHLB TQHKK OBPHVU EOVIHYB',
            '5-8': 'ZRWU QCUUIMC URILL PCQIWV FPWJIZC',
            '9-3': 'SOXJ HNJJDFN JODYY ANHDXQ IAXKDSN',
        }
        self.plaintext_any_character = '#>This messag@ shall rema5!in private'
        self.ciphertexts_any_character = {
            '3-1': '#>GWZD LNDDBT@ DWBII ANLB5!ZO UAZMBGN',
            '3-2': '#>HXAE MOEECU@ EXCJJ BOMC5!AP VBANCHO',
            '5-7': '#>YQVT PBTTHL@ TQHKK OBPH5!VU EOVIHYB',
            '5-8': '#>ZRWU QCUUIM@ URILL PCQI5!WV FPWJIZC',
            '9-3': '#>SOXJ HNJJDF@ JODYY ANHD5!XQ IAXKDSN',
        }

    def test_invalid_argument(self) -> None:
        with self.assertRaises(ValueError):
            cryptools.AffineCipher(2, 2)    # not co-prime

    def test_encode_only_letters(self) -> None:
        for key in self.ciphertexts_only_letters.keys():
            keyA, keyB = int(key.split('-')[0]), int(key.split('-')[1])
            self.assertEqual(
                cryptools.AffineCipher(keyA, keyB).encode(self.plaintext_only_letters),
                self.ciphertexts_only_letters[key]
            )

    def test_decode_only_letters(self) -> None:
        for key in self.ciphertexts_only_letters.keys():
            keyA, keyB = int(key.split('-')[0]), int(key.split('-')[1])
            self.assertEqual(
                cryptools.AffineCipher(keyA, keyB).decode(self.ciphertexts_only_letters[key]),
                self.plaintext_only_letters.upper()
            )

    def test_encode_any_character(self) -> None:
        for key in self.ciphertexts_any_character.keys():
            keyA, keyB = int(key.split('-')[0]), int(key.split('-')[1])
            self.assertEqual(
                cryptools.AffineCipher(keyA, keyB).encode(self.plaintext_any_character),
                self.ciphertexts_any_character[key]
            )

    def test_decode_any_character(self) -> None:
        for key in self.ciphertexts_any_character.keys():
            keyA, keyB = int(key.split('-')[0]), int(key.split('-')[1])
            self.assertEqual(
                cryptools.AffineCipher(keyA, keyB).decode(self.ciphertexts_any_character[key]),
                self.plaintext_any_character.upper()
            )


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
        self.plaintext_any_character = '#>This messag@ shall rema5!in private'
        self.ciphertexts_any_character = {
            0: '#>THIS MESSAG@ SHALL REMA5!IN PRIVATE',
            1: '#>UIJT NFTTBH@ TIBMM SFNB5!JO QSJWBUF',
            2: '#>VJKU OGUUCI@ UJCNN TGOC5!KP RTKXCVG',
            3: '#>WKLV PHVVDJ@ VKDOO UHPD5!LQ SULYDWH',
            4: '#>XLMW QIWWEK@ WLEPP VIQE5!MR TVMZEXI',
            5: '#>YMNX RJXXFL@ XMFQQ WJRF5!NS UWNAFYJ',
            6: '#>ZNOY SKYYGM@ YNGRR XKSG5!OT VXOBGZK',
            7: '#>AOPZ TLZZHN@ ZOHSS YLTH5!PU WYPCHAL',
            8: '#>BPQA UMAAIO@ APITT ZMUI5!QV XZQDIBM',
            9: '#>CQRB VNBBJP@ BQJUU ANVJ5!RW YAREJCN',
            10: '#>DRSC WOCCKQ@ CRKVV BOWK5!SX ZBSFKDO',
            11: '#>ESTD XPDDLR@ DSLWW CPXL5!TY ACTGLEP',
            12: '#>FTUE YQEEMS@ ETMXX DQYM5!UZ BDUHMFQ',
            13: '#>GUVF ZRFFNT@ FUNYY ERZN5!VA CEVINGR',
            14: '#>HVWG ASGGOU@ GVOZZ FSAO5!WB DFWJOHS',
            15: '#>IWXH BTHHPV@ HWPAA GTBP5!XC EGXKPIT',
            16: '#>JXYI CUIIQW@ IXQBB HUCQ5!YD FHYLQJU',
            17: '#>KYZJ DVJJRX@ JYRCC IVDR5!ZE GIZMRKV',
            18: '#>LZAK EWKKSY@ KZSDD JWES5!AF HJANSLW',
            19: '#>MABL FXLLTZ@ LATEE KXFT5!BG IKBOTMX',
            20: '#>NBCM GYMMUA@ MBUFF LYGU5!CH JLCPUNY',
            21: '#>OCDN HZNNVB@ NCVGG MZHV5!DI KMDQVOZ',
            22: '#>PDEO IAOOWC@ ODWHH NAIW5!EJ LNERWPA',
            23: '#>QEFP JBPPXD@ PEXII OBJX5!FK MOFSXQB',
            24: '#>RFGQ KCQQYE@ QFYJJ PCKY5!GL NPGTYRC',
            25: '#>SGHR LDRRZF@ RGZKK QDLZ5!HM OQHUZSD',
            26: '#>THIS MESSAG@ SHALL REMA5!IN PRIVATE',
        }

    def test_encode_only_letters(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).encode(
                self.plaintext_only_letters), self.ciphertexts_only_letters[i]
            )

    def test_decode_only_letters(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).decode(
                self.ciphertexts_only_letters[i]), self.plaintext_only_letters.upper()
            )

    def test_encode_any_character(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).encode(
                self.plaintext_any_character), self.ciphertexts_any_character[i]
            )

    def test_decode_any_character(self) -> None:
        for i in range(27):
            self.assertEqual(cryptools.CaesarCipher(i).decode(
                self.ciphertexts_any_character[i]), self.plaintext_any_character.upper()
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
