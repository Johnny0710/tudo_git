import os
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
    path = file_path.split(r'/')
    img_split = path[-1].split('.')
    path = r'/'.join(path[0:-1])
    img = Image.open(file_path)
    img.thumbnail((200,200))
    img.save('{}/thumbnail/{}_200x200.{}'.format(path,img_split[0],img_split[1]))


