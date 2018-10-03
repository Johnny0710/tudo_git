import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class ExploerHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('exploer.html')

class PostHandler(BaseHandler):
    def get(self, post_id, *args, **kwargs):
        self.render('post.html',post_id=post_id)

class LoginHandler(BaseHandler):
    pass