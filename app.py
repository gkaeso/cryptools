from http import HTTPStatus
import json
import typing

import tornado.web
import tornado.ioloop

import cryptools


PORT = 8000


class AtbashCipher(tornado.web.RequestHandler):
    async def post(self):
        is_valid, error = self._validate()
        if not is_valid:
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.write({'error': error})
        else:
            c = self.get_status()
            req_body: dict = json.loads(self.request.body)
            c = self.get_status()
            try:
                if req_body['encrypt']:
                    text = await cryptools.AtbashCipher().encode(req_body['text'])
                    c = self.get_status()
                else:
                    text = await cryptools.AtbashCipher().decode(req_body['text'])
                    c = self.get_status()
                self.write({'text': text})
            except Exception:
                self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
                self.write({'error': 'Unexpected error'})

    def _validate(self) -> tuple[bool, str]:
        is_valid: bool = True
        error: str = ''

        body: dict = json.loads(self.request.body)
        expected_args: list[str] = ['text', 'encrypt']

        if not all(arg in body for arg in expected_args):
            is_valid, error = False, 'Missing body argument'
        elif not isinstance(body['text'], str):
            is_valid, error = False, "Body argument 'text' is not a string"
        elif not isinstance(body['encrypt'], bool):
            is_valid, error = False, "Body argument 'encrypt' is not a boolean"

        return is_valid, error


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Dummy GET page')


def make_app() -> tornado.web.Application:
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/cipher/atbash/", AtbashCipher)
    ])

    app.listen(PORT)

    return app


if __name__ == '__main__':

    app = make_app()

    print(f"Application listening on port {PORT}")

    tornado.ioloop.IOLoop.current().start()
