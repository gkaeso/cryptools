from http import HTTPStatus
import json

import tornado.testing
import tornado.web

from app import make_app


class TestAffineCipherHandler(tornado.testing.AsyncHTTPTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = '/cipher/affine/'
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.plaintext = 'This message shall remain private'

    def get_app(self) -> tornado.web.Application:
        return make_app()

    def test_post_invalid_argument_type_key(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": self.plaintext, 'encrypt': True, "keys": 'not a list'})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': "Invalid type for body argument 'keys'"})

    def test_post_encode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": self.plaintext, 'encrypt': True, "keys": [5, 7]})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': 'YQVT PBTTHLB TQHKK OBPHVU EOVIHYB'})

    def test_post_decode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "YQVT PBTTHLB TQHKK OBPHVU EOVIHYB", "encrypt": False, "keys": [5, 7]})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': self.plaintext.upper()})


class TestCaesarCipherHandler(tornado.testing.AsyncHTTPTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = '/cipher/caesar/'
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.plaintext = 'This message shall remain private'

    def get_app(self) -> tornado.web.Application:
        return make_app()

    def test_post_invalid_argument_type_key(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": 1, 'encrypt': True, "key": 'not an int'})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': "Invalid type for body argument 'text'"})

    def test_post_encode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": self.plaintext, 'encrypt': True, "key": 3})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': 'WKLV PHVVDJH VKDOO UHPDLQ SULYDWH'})

    def test_post_decode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "WKLV PHVVDJH VKDOO UHPDLQ SULYDWH", "encrypt": False, "key": 3})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': self.plaintext.upper()})


class TestAtbashCipherHandler(tornado.testing.AsyncHTTPTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = '/cipher/atbash/'
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.plaintext = 'This message shall remain private'

    def get_app(self) -> tornado.web.Application:
        return make_app()

    def test_post_encode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": self.plaintext, "encrypt": True})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': 'GSRH NVHHZTV HSZOO IVNZRM KIREZGV'})

    def test_post_decode(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "GSRH NVHHZTV HSZOO IVNZRM KIREZGV", "encrypt": False})
        )
        self.assertEqual(response.code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.body), {'text': self.plaintext.upper()})


class TestBaseCipherValidation(tornado.testing.AsyncHTTPTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = '/cipher/atbash/'
        self.headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.plaintext = 'This message shall remain private'

    def get_app(self) -> tornado.web.Application:
        return make_app()

    def test_post_invalid_argument_type_text(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": 1, 'encrypt': True})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': "Invalid type for body argument 'text'"})

    def test_post_invalid_argument_type_encrypt(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "Dummy string", 'encrypt': 'not a boolean'})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': "Invalid type for body argument 'encrypt'"})

    def test_post_missing_argument(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "Dummy string"})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': 'Missing body argument'})