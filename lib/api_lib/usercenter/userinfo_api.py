from lib.api_lib.usercenter.usercenter_urls import UCUrls
import datetime
from common.helper import *
from config.config_case import ConfigCase
import time
import requests
from common import helper
now = int(time.time())


class UserInfo:

    def __init__(self, client):
        self.client = client
        self.url_builder = UCUrls()

    def get_province(self):
        return self.client.get(url=self.url_builder.get_province)

    def get_userMobileTypeList(self):
        return self.client.get(url=self.url_builder.get_usermobiletype)

    def get_accountInfo(self):
        return self.client.get(url=self.url_builder.get_accountinfo)

    def get_ontrialInfo(self):
        return self.client.get(url=self.url_builder.get_trialinfo)

    def get_baseInfo(self):
        return self.client.get(url=self.url_builder.get_baseinfo)

    def update_avatarUrl(self, pn):
        data = {
            "avatarPath": pn
        }
        return self.client.post(url=self.url_builder.update_avatar, json=data)

    def update_userinfo(self, sex, nickName):
        data = {
            "nickName": nickName,
            "sex": sex
        }
        return self.client.post(url=self.url_builder.update_userinfo, json=data)

    def loginYichang_sendcode(self, userid, mobile, timestamp):
        data = {
            "userId": userid,
            "mobile": mobile,
            "timestamp": timestamp,
            "sign": get_str_md5(APP_AES_KEY + str(mobile) + str(timestamp) + str(userid) + APP_AES_KEY)
        }

        return requests.post(url=self.url_builder.sendcode, json=data).content.decode('utf-8')

    def get_userId(self,type,value):
        data={
            "type":type,
            "value":value
        }

        return self.client.get(url=self.url_builder.get_userid ,params=data)


