import  os
import hashlib

import tornado.web

from utils import img

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
        self.render('exploer.html',files = os.listdir('./statics/uploads/thumbnail'))

class PostHandler(BaseHandler):
    """
    获取图片原图
    """
    def get(self, post_id, *args, **kwargs):
        post_id_tr = post_id.replace('_200x200','')
        print(post_id_tr)
        self.render('post.html',post_id=post_id_tr)

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

        if res:
            new_name = img.hash_name(res[0].filename)
            with open('./statics/uploads/{}'.format(new_name),'wb') as img_file:
                img_file.write(res[0].body)
                img.create_thum('./statics/uploads/{}'.format(new_name))
        else:
            self.redirect(r'/upload')