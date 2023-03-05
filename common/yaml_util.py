
"""
对yaml文件的操作方法
"""
import yaml

#读取
def read_yaml(key):
    with open('../extract.yaml',mode='r',encoding='utf-8')as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]
#写入
def write_yaml(data):
    with open('../extract.yaml',mode='a',encoding='utf-8')as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空
def clean_yaml():
    with open('../extract.yaml',mode='w',encoding='utf-8')as f:
        f.truncate()