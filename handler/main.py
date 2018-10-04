import  os
import hashlib

import tornado.web
from pycket.session import SessionMixin

from utils import img

class BaseHandler(tornado.web.RequestHandler,SessionMixin):
    """
    基础类,所有handler均继承至这里
    2018年10月4日21:22:10  添加了 pycket
    """
    def get_current_user(self):
        return self.session.get('username')


class IndexHandler(BaseHandler):
    @tornado.web.authenticated  # 登录验证装饰器
    def get(self):
        self.render("index.html",files = img.get_images('./statics/uploads'))

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

class ErrorHandler(BaseHandler):
    def get(self,*args,**kwargs):
        self.send_error(404)
    def write_error(self, status_code, **kwargs):
        self.render('error.html')