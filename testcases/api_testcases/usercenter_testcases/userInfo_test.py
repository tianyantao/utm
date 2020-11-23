from common.unittest_v2 import TestCaseV2
from lib.api_lib.ewt_client import *
from lib.api_lib.usercenter.userinfo_api import UserInfo
from testcases.api_testcases.usercenter_testcases.accout_data import *


class GetUserInfoTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_province(self):
        """
         title:获取省份信息
          url:/api/usercenter/area/getProvinces
          author:王小娟
        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_province()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data'])>0)

    def test_userMobileList(self):
        """
          title:获取用户常用手机类型信息
          url:/api/usercenter/authentication/mobiletype/list
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_userMobileTypeList()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_userAccountInfo_svip(self):
        """
          title:获取svip用户账号信息
          url:/api/authcenter/account/get/info
          author:王小娟
        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_accountInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_userAccountInfo_unreactivated(self):
        """
          title:获取注册用户账号信息
          url:/api/authcenter/account/get/info
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_accountInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_userAccountInfo_mobile(self):
        """
          title:获取手机号账号信息
          url:/api/authcenter/account/get/info
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_accountInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_onTrialInfo_svip(self):
        """
          title:获取至尊会员的试用信息
          url:/api/usercenter/member/onTrialInfo
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_ontrialInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_onTrialInfo_unreactivated(self):
        """
          title:获取未激活会员的的试用信息
          url:/api/usercenter/member/onTrialInfo
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=unreactivated_account))
        res = app.get_ontrialInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_onTrialInfo_ontrial(self):
        """
            title:获取试用会员的的试用信息
            url:/api/usercenter/member/onTrialInfo
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=ontrial))
        res = app.get_ontrialInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_baseInfo_svip(self):
        """
            title:获取至尊会员的的基本信息
            url:/api/usercenter/user/baseinfo
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_baseInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_baseInfo_unreactivated(self):
        """
            title:获取注册会员的的基本信息
            url:/api/usercenter/user/baseinfo
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=unreactivated_account))
        res = app.get_baseInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_baseInfo_ontrial(self):
        """
            title:获取试用会员的的基本信息
            url:/api/usercenter/user/baseinfo
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=ontrial))
        res = app.get_baseInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_updateAvatarUrl_p5(self):
        """
            title:更换用户的头像p5
            url:/api/usercenter/user/update/avatarUrl
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.update_avatarUrl(pn="p5")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertEqual(True ,res['data'])


    def test_updateAvatarUrl_p6(self):
        """
            title:更换用户的头像到p6
            url:/api/usercenter/user/update/avatarUrl
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.update_avatarUrl(pn="p6")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertEqual(True, res['data'])

    def test_updateUserInfo_nickName(self):
        """
            title:修改用户的昵称为蘑菇
            url:/api/usercenter/user/update
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.update_userinfo(sex=1, nickName='蘑菇')
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertEqual(True, res['data'])

    def test_updateUserInfo_sex(self):
        """
            title:修改用户的昵称为香菇，以及修改性别为女
            url:/api/usercenter/user/update
            author:王小娟

          """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.update_userinfo(sex=2, nickName='香菇')
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertEqual(True, res['data'])

    def test_getUserId_mobile(self):
        """
          title:根据手机号获取用户userID
          url:/api/usercenter/user/queryUserId
          author:王小娟
        """
        app = UserInfo(AppNewClient(username=mobile))
        res =app.get_userId(type=1,value=mobile)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_getUserId_account(self):
        """
          title:根据账号获取用户userID
          url:/api/usercenter/user/queryUserId
          author:王小娟

        """
        app = UserInfo(AppNewClient(username=svip_account))
        res = app.get_userId(type=2, value=svip_account)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(True, res['success'])
        self.assertTrue(len(res['data']) > 0)
