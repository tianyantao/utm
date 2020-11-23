from common.unittest_v2 import TestCaseV2
from lib.api_lib.usercenter.userinfo_api import *
from lib.api_lib.ewt_client import *
from testcases.api_testcases.usercenter_testcases.accout_data import *


class SendCodeTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_loginYichang(self):
        """
         title: 淘宝合买登录异常触发手机号校验发送手机验证码
         url: /api/usercenter/user/login/sms/sendcode
         author: 王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.loginYichang_sendcode(userid=userid, mobile=mobile, timestamp=int(time.time() * 1000))
        print(res)
