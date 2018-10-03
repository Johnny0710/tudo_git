import os

def get_images(path):
    """
    获取提供的文件夹下的所有图片
    :param path:
    :return:
    """
    files = os.listdir(path)
    return files


