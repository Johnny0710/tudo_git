import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ExploerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('exploer.html')

class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id, *args, **kwargs):
        self.render('post.html',post_id=post_id)

class LoginHandler(tornado.web.RequestHandler):
    pass