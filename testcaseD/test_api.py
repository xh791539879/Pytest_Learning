
import pytest

from common.common_util import Common_Util


# class TestApi(Common_Util):
#                                         #可以是列表嵌套列表[['李四', '张三'], ['5', '6']]
#                                         #可以是字典，也可以是元组('JQM01','JQM02','JQM03')
#                                         #可以是列表嵌套字典[{'name':'张三'},{'age':'4'}]
#     @pytest.mark.parametrize ('caseinfo',['鉴权码01','鉴权码02','鉴权码03'] )
#     def test_api_01(self,caseinfo):
#         print("获取接口鉴权码:"+str(caseinfo))  #str强转为字符串


#可以传多个值
class TestApi02(Common_Util):
    @pytest.mark.parametrize('arg1,arg2',[['name', '张三'], ['age', '6']])
    def test_api_01(self,arg1,arg2):
        print("测试接收到的数据为："+str(arg1)+" "+str(arg2))