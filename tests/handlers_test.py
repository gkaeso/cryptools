from http import HTTPStatus
import json

import tornado.testing
import tornado.web

from app import make_app


class TestAtbashHandler(tornado.testing.AsyncHTTPTestCase):

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
        self.assertEqual(json.loads(response.body), {'error': "Body argument 'text' is not a string"})

    def test_post_invalid_argument_type_encrypt(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "Dummy string", 'encrypt': 'not a boolean'})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': "Body argument 'encrypt' is not a boolean"})

    def test_post_missing_argument(self) -> None:
        response = self.fetch(
            self.url,
            method='POST',
            headers=self.headers,
            body=json.dumps({"text": "Dummy string"})
        )
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json.loads(response.body), {'error': 'Missing body argument'})

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
