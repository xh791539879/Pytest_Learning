
"""
对yaml文件的操作方法
"""
import os

import yaml

#获取当前根目录路径
def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]


#读取
def read_yaml(yamlpath):
    with open(get_obj_path() + yamlpath,mode='r',encoding='utf-8')as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
#写入
def write_yaml(data):
    with open('../extract.yaml',mode='a',encoding='utf-8')as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空
def clean_yaml():
    with open('../extract.yaml',mode='w',encoding='utf-8')as f:
        f.truncate()

if __name__ == '__main__':
    print(read_yaml('testcaseD/get_token.yaml'))