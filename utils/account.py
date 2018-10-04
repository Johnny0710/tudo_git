import hashlib

def hash_passwd(password):
    """
    对用户密码进行重新加密
    :param password:
    :return:
    """
    return  hashlib.sha256(password.encode()).hexdigest()


def authenticate(usernmae,password):
    """
    检测用户名和密码是否匹配
    :param usernmae:
    :param password:
    :return:
    """
    if usernmae and password:
        return  True
    else:
        return False


if __name__ == '__main__':
    print(hash_passwd('123456'))