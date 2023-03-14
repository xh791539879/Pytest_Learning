
import pytest

from common.common_util import Common_Util


class TestApi(Common_Util):

    @pytest.mark.parametrize('caseinfo',['鉴权码01','鉴权码02','鉴权码03'])
    def test_api_01(self,caseinfo):
        print("获取接口鉴权码")