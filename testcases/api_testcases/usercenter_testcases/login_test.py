from common.unittest_v2 import TestCaseV2
from lib.api_lib.usercenter.usercenter_api import *
from testcases.api_testcases.usercenter_testcases.accout_data import *



class ApploginTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_svip_login(self):
        """
           title:app svip会员登录
           url:/api/authcenter/oauth/login/app
           author:王小娟
        """
        res = auth_app_login(username=svip_account)
        print(res)
        self.assertEqual("200", res[0]['code'])
        self.assertEqual(15, res[0]['data']['memberType'])

    def test_unactivated_login(self):
        """
         title:app 注册会员登录
         url:/api/authcenter/oauth/login/app
         author:王小娟
        """
        res = auth_app_login(username=unreactivated_account)
        print(res)
        self.assertEqual("200", res[0]['code'])
        self.assertEqual(99, res[0]['data']['memberType'])

    def test_QQ_login(self):
        """
         title:app QQ登录
         url:/api/usercenter/user/login/third/app/openId/login
         author:王小娟
        """
        res = auth_third_login()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])

    def test_visitor_login(self):
        """
          title: ios 游客登录
          url:/api/usercenter/user/login/visitor/login
          author:王小娟
        """
        res = auth_visitor_login()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])


class PcloginTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_svip_login(self):
        """
           title:pc svip会员登录
           url:/api/authcenter/oauth/login
           author:王小娟
        """
        res = auth_pc_login(username=svip_account)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(15, res['data']['memberType'])

    def test_unactivated_login(self):
        """
         title:pc 注册会员登录
         url:/api/authcenter/oauth/login
         author:王小娟
        """
        res = auth_pc_login(username=unreactivated_account)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(99, res['data']['memberType'])
