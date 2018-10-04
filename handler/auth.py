
from handler.main import  BaseHandler
from utils import account

class LoginHandler(BaseHandler):
    """
    用于用户登录验证及session设置
    """
    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        password = self.get_argument('password',None)
        next = self.get_argument('next',None)
        if username and password:
            passed = account.authenticate(username,password)
            if passed:
                self.session.set("username",username)
                self.redirect(next)
            else:
                self.redirect(r'/login')
        else:
            self.redirect('/login')

class SingnHandler(BaseHandler):
    pass

class loginOutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.session.delete('username')
        self.redirect('/')




