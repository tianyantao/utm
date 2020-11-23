from common import requests_v2 as requests
from common import helper
import json
from lib.api_lib.usercenter import usercenter_api
from lib.api_lib.teacher.teacher_urls import TeacherUrls
import time


class WebClient:

    def __init__(self, username, password='123456', login=True):
        self.username = username
        self.password = password
        self.request_session = requests.session()
        self.user_token = ""
        self.user_id = 0
        self.__is_login = login
        if self.__is_login:
            rs, user_token = usercenter_api.pc_login(self.username, self.password)
            self.request_session = rs
            self.user_token = user_token
            self.user_id = int(user_token.split('-')[0])

    def _login(self):
        rs, user_token = usercenter_api.pc_login(self.username, self.password)
        self.request_session = rs
        self.user_token = user_token
        self.user_id = int(user_token.split('-')[0])

    def get(self, url, params=None, **kwargs):
        # if self.__is_login:
        #     self._login()
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
        # bend项目全局get请求参数加了时间戳
        if 'bendbff' in url and params:
            params['timestamp'] = int(time.time()*1000)
        response = self.request_session.get(url, params=params, headers=headers, verify=False, **kwargs)
        ret_json = helper.check_json_response(response)
        return ret_json

    def post(self, url, data=None, **kwargs):
        # if self.__is_login:
        #     self._login()
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
        if isinstance(data, dict):
            data = json.dumps(data)
            headers["Content-Type"] = "application/json"
        response = self.request_session.post(url, data=data, headers=headers, verify=False, **kwargs)
        ret_json = helper.check_json_response(response)
        return ret_json


class AppClient:

    def __init__(self, username, password='123456', login=True, sid=2, version='7.8.1'):
        self.username = username
        self.password = password
        self.sid = sid
        self.request_session = requests.session()
        self.user_token = ""
        self.user_id = 0
        self.__is_login = login
        self.version = version
        if self.__is_login:
            user_token = usercenter_api.app_login(self.username, self.password)
            self.user_token = user_token
            self.user_id = int(user_token.split('-')[0])
            userid_keybin = 30205014
            self.__userid = int(userid_keybin ^ self.user_id)

    def _login(self):
        user_token = usercenter_api.app_login(self.username, self.password)
        self.user_token = user_token
        self.user_id = int(user_token.split('-')[0])
        userid_keybin = 30205014
        self.__userid = int(userid_keybin ^ self.user_id)

    def __get_request_header(self, data=None):
        headers = {"userid": str(self.__userid)}
        if isinstance(data, dict):
            headers["Content-Type"] = "application/json"
        headers['version'] = self.version
        headers['token'] = self.user_token
        return headers

    def get(self, url, params=None, sign_mode=0, **kwargs):
        return self.__send_request(method='get', url=url, params=params, sign_mode=sign_mode, **kwargs)

    def post(self, url, data=None, datastr=None, sign_mode=0, **kwargs):
        if datastr:
            # if isinstance(datastr, dict):
            #     datastr = json.dumps(datastr)
            return self.__send_request(method='post', url=url, datastr=datastr, sign_mode=sign_mode, **kwargs)
        return self.__send_request(method='post', url=url, data=data, sign_mode=sign_mode, **kwargs)

    def __append_request_params(self, origin_params, sign_mode=None):
        sign_key = "eo^nye1j#!wt2%v)"
        exclude_keys = ['sid', 'osVersion', 'token']
        prepared_params = {}
        if not origin_params:
            origin_params = {}
        # if isinstance(origin_params, str):
        #     origin_params = eval(origin_params)
        prepared_params.update(origin_params)

        if 'sign' not in prepared_params:
            _content = ''
            _content += sign_key
            value_list_for_sign = []
            keys = [k for k in prepared_params.keys() if k not in exclude_keys]
            if sign_mode == 0:
                return prepared_params
            if sign_mode == 1:
                # 签名时包含token，先按照key进行排序，再拼接value
                if 'token' in origin_params:
                    keys.append('token')
                value_list_for_sign = [prepared_params[k] for k in sorted(keys)]
            elif sign_mode == 2:
                # 签名时包含token，先按照key进行排序，再按照key=value的格式拼接后进行签名
                if 'token' in origin_params:
                    keys.append('token')
                value_list_for_sign = ["&{}={}".format(k, prepared_params[k]) for k in sorted(keys)]
            elif sign_mode == 3:
                # 签名时包含token，不排序，按原顺序拼接value后进行签名
                if 'token' in origin_params:
                    keys.append('token')
                value_list_for_sign = [prepared_params[k] for k in keys]
            elif sign_mode == 4:
                # 签名时包含token，不排序，按原顺序按照key=value的格式拼接后进行签名
                if 'token' in origin_params:
                    keys.append('token')
                value_list_for_sign = ["&{}={}".format(k, prepared_params[k]) for k in keys]
            elif sign_mode == 5:
                # 签名时不包含token，先按照key进行排序，再拼接value
                value_list_for_sign = [prepared_params[k] for k in sorted(keys)]
            elif sign_mode == 6:
                # 签名时不包含token，先按照key进行排序，再按照key=value的格式拼接后进行签名
                value_list_for_sign = ["&{}={}".format(k, prepared_params[k]) for k in sorted(keys)]
            elif sign_mode == 7:
                # 签名时不包含token，不排序，按原顺序拼接value后进行签名
                value_list_for_sign = [prepared_params[k] for k in keys]
            elif sign_mode == 8:
                # 签名时不包含token，不排序，按原顺序按照key=value的格式拼接后进行签名
                value_list_for_sign = ["&{}={}".format(k, prepared_params[k]) for k in keys]
            elif sign_mode == 9:
                # 签名时包含token和sid，先按照key进行排序，再拼接value
                if 'sid' in origin_params:
                    keys.append('sid')
                if 'token' in origin_params:
                    keys.append('token')
                value_list_for_sign = [prepared_params[k] for k in sorted(keys)]
            elif sign_mode == 11:  # app教师端接口校验方式
                # 签名时包含token、sid，先按照key进行排序，再拼接value
                prepared_params["token"] = self.user_token
                keys.append('token')
                if 'sid' in origin_params:

                    keys.append('sid')
                value_list_for_sign = [prepared_params[k] for k in sorted(keys)]
            for v in value_list_for_sign:
                _content += str(v)
            if sign_mode in (2, 4, 6, 8):
                _content += "&" + sign_key
            else:
                _content += sign_key
            if sign_mode == 10:
                _content = sign_key + str(self.user_id) + sign_key
            prepared_params["sign"] = helper.get_str_md5(_content)
        return prepared_params

    def __send_request(self, sign_mode, method, url, params=None, data=None, datastr=None, json=None, **kwargs):
        ret_json = None
        # if self.__is_login:
        #     self._login()
        headers = self.__get_request_header(data=data)
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
        retry_for_sign_mode = True
        # if 'sign' in params or 'sign' in str(data):
        #     retry_for_sign_mode = False
        if params and 'sign' in params:
            retry_for_sign_mode = False
        if data and 'sign' in data:
            retry_for_sign_mode = False
        if datastr and 'sign' in datastr:
            retry_for_sign_mode = False
        if json and 'sign' in json:
            retry_for_sign_mode = False
        # 尝试不同的加签模式进行签名并发送请求，遇到签名验证通过的结果即返回
        if sign_mode:
            params_prepared = self.__append_request_params(origin_params=params,
                                                           sign_mode=sign_mode) if 'get' == method.lower() else self.__append_request_params(
                origin_params=datastr if datastr else data, sign_mode=sign_mode)
            if 'get' == method.lower():
                response = self.request_session.get(url, params=params_prepared, headers=headers, verify=False,
                                                    **kwargs)
            elif datastr:
                response = self.request_session.post(url, data=params_prepared, headers=headers, verify=False, **kwargs)
            else:
                response = self.request_session.post(url, json=params_prepared, headers=headers,
                                                     verify=False, **kwargs)
            ret_json = helper.check_json_response(response)
        elif retry_for_sign_mode:
            for sm in range(0, 12):
                params_prepared = self.__append_request_params(origin_params=params,
                                                               sign_mode=sm) if 'get' == method.lower() else self.__append_request_params(
                    origin_params=datastr if datastr else data, sign_mode=sm)

                if 'get' == method.lower():
                    response = self.request_session.get(url, params=params_prepared, headers=headers, verify=False, **kwargs)
                elif datastr:
                    response = self.request_session.post(url, data=params_prepared, headers=headers, verify=False, **kwargs)
                else:
                    response = self.request_session.post(url, json=params_prepared, headers=headers, verify=False, **kwargs)
                ret_json = helper.check_json_response(response)
                # 如果返回的结果是签名验证失败（703），则继续循环尝试采用不同的签名方式进行验证，否则退出循环
                if 'code' in ret_json and (ret_json['code'] == 703):
                    continue
                else:
                    break
        else:
            if 'get' == method.lower():
                response = self.request_session.get(url, params=params, headers=headers, verify=False, **kwargs)
            else:
                if isinstance(data, dict):
                    response = self.request_session.post(url, json=data, headers=headers, verify=False, **kwargs)
                else:
                    response = self.request_session.post(url, data=data, json=json, headers=headers, verify=False, **kwargs)
            ret_json = helper.check_json_response(response)
        return ret_json


class TeacherOaClient:

    def __init__(self, schoolid):
        self.schoolid = schoolid
        self.request_session = requests.session()
        self.token4oa = ''
        self.oatoken = self.__get_oatoken(schoolid=self.schoolid)

    def __get_oatoken(self, schoolid):
        data = {
                  "uid": 1234,
                  "schoolId": schoolid,
                  "userName": "测试",
                  "userRole": 2,
                  "projectId": 12345,
                  "expireYear": 2022
                }
        res = helper.check_json_response(requests.SessionV2().post(url=TeacherUrls().oa_auth, json=data))
        return res['data']['oaToken']


    def __get_request_header(self):
        headers = {}
        headers['oaToken'] = self.oatoken
        return headers


    def get(self, url, params=None, **kwargs):
        response = self.request_session.get(url=url, headers=self.__get_request_header(), params=params, verify=False, **kwargs)
        return helper.check_json_response(response)

    def post(self, url, data=None, json=None, **kwargs):
        headers = self.__get_request_header()
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
        response = self.request_session.post(url=url, headers=headers, verify=False, data=data, json=json, **kwargs)
        return helper.check_json_response(response)


class AppNewClient:

    def __init__(self, username=None, password='123456', openid=None):
        self.username = username
        self.password = password
        self.request_session = requests.session()
        self.user_token = ""
        self.user_id = 0
        if username:
            user_token = usercenter_api.auth_app_login(self.username, self.password)
            self.user_token = user_token[-1]
        elif openid:
            self.user_token = usercenter_api.auth_third_login()['data']['token']
        else:
            self.user_token = usercenter_api.auth_visitor_login()['data']['token']

        self.user_id = int(self.user_token.split('-')[0])
            # userid_keybin = 30205014
            # self.__userid = int(userid_keybin ^ self.user_id)

    # def _login(self):
    #     user_token = usercenter_api.app_login(self.username, self.password)
    #     self.user_token = user_token
    #     self.user_id = int(user_token.split('-')[0])
        # userid_keybin = 30205014
        # self.__userid = int(userid_keybin ^ self.user_id)

    def __get_request_header(self, data=None):
        # headers = {"userid": str(self.__userid)}
        headers = {}
        if isinstance(data, dict):
            headers["Content-Type"] = "application/json"
        # headers['version'] = self.version
        headers['token'] = self.user_token
        return headers

    def get(self, url, params=None, **kwargs):
        return self.__send_request(method='get', url=url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.__send_request(method='post', url=url, data=data, json=json, **kwargs)

    def __send_request(self, method, url, params=None, data=None, json=None, **kwargs):
        headers = self.__get_request_header(data=data)
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))

        if 'get' == method.lower():
                response = self.request_session.get(url, params=params, headers=headers, verify=False, **kwargs)
        else:
            if isinstance(data, dict):
                response = self.request_session.post(url, json=data, headers=headers, verify=False, **kwargs)
            else:
                response = self.request_session.post(url, data=data, json=json, headers=headers, verify=False, **kwargs)
        ret_json = helper.check_json_response(response)
        return ret_json


if __name__ == '__main__':
    # oa = TeacherOaClient(25729)
    # res = oa.get(url='http://teacher.test.mistong.com/api/eteacherproduct/oa/schoolManage/querySchoolInfo')
    # print(res)
    pass
    app = AppNewClient()
    print(app.user_token)