"""
ids :将变量名重命名，次要
name ：将fixture下的方法重命名，重命名后前者失效
"""
import pytest

import sys
type = sys.getfilesystemencoding()
def read_yaml():
    return ['zhangsan','lisi','wangwu']

@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['001','002','003'],name="db")
def exe_database_sql(request): # 此处request为固定写法
    print("执行sql查询")
    yield request.param # 返回获取的数据,param没有s
    print("关闭数据库")


class TestIds:
    def test_ids01(self):
        print('this is ids01')
    def test_id02(self,db):
        print("this is ids02:"+db)


class TestIdss:
    def test_idss01(self):
        print("this is idss01")
    def test_idsss02(self):
        print("this is idss02")