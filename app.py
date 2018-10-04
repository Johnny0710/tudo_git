import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define,options


from handler import main,auth

define('port', 9999, help='Default Run Port', type=int)


class Applictation(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',main.IndexHandler),
            (r'/explore',main.ExploerHandler),
            (r'/post/(?P<post_id>[a-zA-z0-9.]+)',main.PostHandler),
            (r'/upload',main.UploadFileHandler),
            (r'/login',auth.LoginHandler),
            (r'/loginout',auth.loginOutHandler),
            (r'/(.*)',main.ErrorHandler)
        ]
        setting = dict(
            debug = True,
            template_path = 'templates',
            static_path = 'statics',
            # 2018年10月4日21:25:42
            #
            # 添加cookie & session
            cookie_secret = 'test',
            login_url = r'/login',
            pycket={
                'engine':'redis',
                'storage':{
                    'host':'localhost',
                    'port': 6379,
                    'db_sessions': 5,
                    'db_notifications': 11,
                    'max_connections': 2 ** 31,
                },
                'cookies':{
                    'expires_days': 30
                }
            }
        )
        super(Applictation, self).__init__(handlers,**setting)

applictation = Applictation()
if __name__ == "__main__":
    tornado.options.parse_command_line()
    applictation.listen(options.port)
    tornado.ioloop.IOLoop.current().start()