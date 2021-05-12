import json

import tornado.web
import tornado.ioloop

import cryptools


PORT = 8000


class AtbashCipher(tornado.web.RequestHandler):
    async def post(self):
        req_body: dict = json.loads(self.request.body)
        if req_body['encrypt']:
            text = await cryptools.AtbashCipher().encode(req_body['text'])
        else:
            text = await cryptools.AtbashCipher().decode(req_body['text'])
        self.write({"ciphertext": text})


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Dummy GET page')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/cipher/atbash/", AtbashCipher)
    ])

    app.listen(PORT)

    print(f"Application listening on port {PORT}")

    tornado.ioloop.IOLoop.current().start()
