import tornado.web
import tornado.ioloop

PORT = 8000


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Dummy GET page')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])

    app.listen(PORT)

    print(f"Application listening on port {PORT}")

    tornado.ioloop.IOLoop.current().start()
