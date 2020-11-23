from common import helper
# import requests
from common import requests_v2 as requests
from lib.api_lib.usercenter.usercenter_urls import UCUrls
import json
import time
from config.config_case import ConfigCase

# web_urls = UCUrls(ConfigCase.PROTOCOL, ConfigCase.HOST_WEB)
urls = UCUrls()
# ac_urls = UCUrls(ConfigCase.PROTOCOL, ConfigCase.HOST_GATEWAY)


def pc_login(username, password='123456', platform=1):
    aes_password = helper.encrypt_pc_password(password)
    queries = {"userName": username, "password": aes_password, "platform": platform}
    login_session = requests.session()
    response = login_session.post(urls.auth_login, json=queries)
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    res_json = json.loads(response.text)
    if int(res_json['code']) != 200:
        print("uc登录异常: {}".format(res_json))
    user_token = res_json['data']['token']
    login_session.cookies.set(name='ewt_user', value='tk={0}&info={1}'.format(res_json['data']['token'],
                                                                              res_json['data']['info']).replace('\n',
                                                                                                                ''))
    return login_session, user_token


def app_login(username, password='123456'):
    login_session = requests.session()
    encrypt_password = helper.encrypt_app_password(password)
    data = "password={0}&sign=10d20dd481a694bf73bbd75aa41062e9" \
           "&devicename=iPhone 6s&devicetoken=B5E1B1E4-BAA1-4F06-9011-A1E21A99DA79" \
           "&platform=2&timestamp={2}&username={1}&" \
           "token=&sid=7".format(encrypt_password, username, int(time.time() * 1000))

    response = login_session.post(urls.app_login, data=data,
                                  headers={"Content-Type": "application/x-www-form-urlencoded"},
                                  verify=False)
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    ret_json = helper.check_json_response(response)
    login_session.close()
    if int(ret_json['code']) != 200:
        print("uc登录异常: {}".format(ret_json))
    return ret_json['data']['member']['token']


# 接口：app登录接口
# author：王小娟
def auth_app_login(username='grade1', password='123456'):
    login_session = requests.session()
    encrypt_password = helper.encrypt_app_password(password)
    # platform: 1：WEB，2：ANDROID，3：IOS
    data = {
        "userName": username,
        "password": encrypt_password,
        "platform": 3,
        "deviceToken": "B5E1B1E4-BAA1-4F06-9011-A1E21A99DA79",
        "deviceName": "iPhone 6s"
    }
    json_data = json.dumps(data)
    response = login_session.post(urls.auth_app_login, data=json_data,
                                  headers={"Content-Type": "application/json"}
                                  )
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    ret_json1 = helper.check_json_response(response)
    login_session.close()
    if int(ret_json1['code']) != 200:
        print("uc登录异常: {}".format(ret_json1))
    return ret_json1, ret_json1['data']['token']


# 接口：pc登录
# author：王小娟
def auth_pc_login(username, password='123456'):
    login_session = requests.session()
    encrypt_password = helper.encrypt_pc_password(password)
    data = {
        "userName": username,
        "password": encrypt_password,
        "platform": 1
    }
    json_data = json.dumps(data)
    response = login_session.post(urls.auth_pc_login, data=json_data, headers={"Content-Type": "application/json"})
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    ret_json = helper.check_json_response(response)
    login_session.close()
    if int(ret_json['code']) != 200:
        print("uc登录异常：{}".format(ret_json))
    return ret_json


# 接口：三方app登录
# author：王小娟
def auth_third_login():
    login_session = requests.session()
    timestamp = int(time.time() * 1000)
    data = {
        "platform": 3,
        "thirdType": 1,
        "openId": ConfigCase.QQopenId,
        "deviceToken": "B5E1B1E4-BAA1-4F06-9011-A1E21A99DA79",
        "deviceName": "iPhone 6s",
        "sign": helper.get_str_md5(
            helper.APP_AES_KEY + ConfigCase.QQopenId + str(3) + str(1) + str(timestamp) + helper.APP_AES_KEY),
        "timestamp": timestamp
    }
    json_data = json.dumps(data)
    response = login_session.post(urls.auth_thirdApp_login, data=json_data,
                                  headers={"Content-Type": "application/json"})
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    ret_json = helper.check_json_response(response)
    login_session.close()
    if int(ret_json['code']) != 200:
        print("uc登录异常：{}".format(ret_json))
    return ret_json


# 接口：游客ios登录
# author：王小娟
def auth_visitor_login():
    login_session = requests.session()
    timestamp = int(time.time() * 1000)
    data = {
        "platform": 3,
        "deviceToken": "B5E1B1E4-BAA1-4F06-9011-A1E21A99DA79",
        "deviceName": "iPhone 6s",
        "sign": helper.get_str_md5(
            helper.APP_AES_KEY + "B5E1B1E4-BAA1-4F06-9011-A1E21A99DA79" + str(timestamp) + helper.APP_AES_KEY),
        "timestamp": timestamp

    }
    json_data = json.dumps(data)
    response = login_session.post(urls.auth_visitor_login, data=json_data,
                                  headers={"Content-Type": "application/json"})
    if response.status_code != 200:
        print("uc登录异常: {}".format(response.text))
    ret_json = helper.check_json_response(response)
    login_session.close()
    if int(ret_json['code']) != 200:
        print("uc登录异常：{}".format(ret_json))
    return ret_json


if __name__ == '__main__':
    res = auth_visitor_login()
    print(res)
