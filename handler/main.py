import tornado.web
import  os



class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html",files = os.listdir('./statics/uploads'))

class ExploerHandler(BaseHandler):
    """
    图片缩略图
    """
    def get(self, *args, **kwargs):
        self.render('exploer.html',files = os.listdir('./statics/uploads'))

class PostHandler(BaseHandler):
    """
    获取图片原图
    """
    def get(self, post_id, *args, **kwargs):
        self.render('post.html',post_id=post_id)

class LoginHandler(BaseHandler):
    pass


class UploadFileHandler(BaseHandler):
    """
    用于提供图片上传的功能
    """
    def get(self, *args, **kwargs):
        self.render('upload.html')
    def post(self, *args, **kwargs):
        res = self.request.files.get('newimg',None)
        with open('statics/uploads/{}'.format(res[0].filename),'wb') as img_file:
            img_file.write(res[0].body)