import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define,options


from handler import main

define('port', 9999, help='Default Run Port', type=int)


class Applictation(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',main.IndexHandler),
            (r'/explore',main.ExploerHandler),
            (r'/post/(?P<post_id>[0-9]+)',main.PostHandler),
            (r'/upload',main.UploadFileHandler)


        ]
        setting = dict(
            debug = True,
            template_path = 'templates',
            static_path = 'statics',
        )
        super(Applictation, self).__init__(handlers,**setting)

applictation = Applictation()
if __name__ == "__main__":
    tornado.options.parse_command_line()
    applictation.listen(options.port)
    tornado.ioloop.IOLoop.current().start()