import os
import hashlib
import datetime

from PIL import Image

def get_images(path):
    """
    获取提供的文件夹下的所有图片
    :param path:
    :return:wir
    """
    files = os.listdir(path)
    return files

# def create_thum(files_path):
#     files = os.listdir(files_path)
#     for file in files:
#         img_split = file.split('.')
#         img = Image.open('{}/{}'.format(files_path,file))
#         img.thumbnail((200,200))
#         print('{}thumbnail/{}_200x200.{}'.format(files_path,img_split[0],img_split[1]))
def create_thum(file_path):
    """
    用户上传图片后,同步生成缩略图
    :param file_path:
    :return:
    """
    path_split = os.path.split(file_path)   # 将路径与文件分开
    img_split = path_split[-1].split('.')   #  提取文件名及扩展名
    img = Image.open(file_path)
    img.thumbnail((200,200))
    img.save('{}/thumbnail/{}_200x200.{}'.format(path_split[0],img_split[0],img_split[1]))

def hash_name(file_name):
    """
    生成文件名称的唯一名
    :param file_name:
    :return:
    """
    name_split = file_name.split('.')
    new_name = str(datetime.datetime.now())+ name_split[0]
    new_name = hashlib.md5(new_name.encode()).hexdigest()+'.'+name_split[1]
    print(new_name)
    return new_name


