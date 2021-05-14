from http import HTTPStatus
import json
from typing import Optional, Awaitable, Any

import tornado.web
import tornado.ioloop

from src import cryptools


PORT = 5000


class BaseCipherHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def _validate_post(self, expected_args: dict[str, Any] = None) -> None:
        is_valid: bool = True
        error: str = ''

        required_args = {'text': str, 'encrypt': bool}
        if expected_args:
            required_args.update(expected_args)

        body: dict = json.loads(self.request.body)

        if not all(arg in body for arg in required_args.keys()):
            is_valid, error = False, 'Missing body argument'
        else:
            for arg_name, arg_type in required_args.items():
                if not isinstance(body[arg_name], arg_type):
                    is_valid, error = False, f"Invalid type for body argument '{arg_name}'"
                    break

        self.is_valid, self.error = is_valid, error


class AtbashCipherHandler(BaseCipherHandler):
    async def post(self):
        self._validate_post()

        if self.is_valid:
            req_body: dict = json.loads(self.request.body)
            try:
                if req_body['encrypt']:
                    text = await cryptools.AtbashCipher().encode(req_body['text'])
                else:
                    text = await cryptools.AtbashCipher().decode(req_body['text'])
                self.write({'text': text})
            except Exception:
                self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
                self.write({'error': 'Unexpected error'})
        else:
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.write({'error': self.error})


class CaesarCipherHandler(BaseCipherHandler):
    async def post(self):
        self._validate_post({'key': int})

        if self.is_valid:
            req_body: dict = json.loads(self.request.body)
            try:
                if req_body['encrypt']:
                    text = await cryptools.CaesarCipher(req_body['key']).encode(req_body['text'])
                else:
                    text = await cryptools.CaesarCipher(req_body['key']).decode(req_body['text'])
                self.write({'text': text})
            except Exception:
                self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
                self.write({'error': 'Unexpected error'})
        else:
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.write({'error': self.error})


class AffineCipherHandler(BaseCipherHandler):
    async def post(self):
        self._validate_post({'keys': list})

        if self.is_valid:
            req_body: dict = json.loads(self.request.body)
            try:
                if req_body['encrypt']:
                    text = await cryptools.AffineCipher(*req_body['keys']).encode(req_body['text'])
                else:
                    text = await cryptools.AffineCipher(*req_body['keys']).decode(req_body['text'])
                self.write({'text': text})
            except Exception as exc:
                self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
                self.write({'error': 'Unexpected error'})
        else:
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.write({'error': self.error})


def make_app() -> tornado.web.Application:
    app = tornado.web.Application([
        (r"/cipher/atbash/", AtbashCipherHandler),
        (r"/cipher/caesar/", CaesarCipherHandler),
        (r"/cipher/affine/", AffineCipherHandler),
    ])

    app.listen(PORT)

    return app


if __name__ == '__main__':
    app = make_app()

    print(f"Application listening on port {PORT}")

    tornado.ioloop.IOLoop.current().start()
