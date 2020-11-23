import base64
import json
import hashlib
import pymysql
import uuid
import unittest
from functools import wraps
import requests
import logging
from flask import current_app
from config.config_web import ConfigWeb




WEB_AES_IV = "2017110912453698"
WEB_AES_KEY = "20171109124536982017110912453698"
APP_AES_KEY = "eo^nye1j#!wt2%v)"
WEB_STUDY_MD5_KEY = "apibib1b7b0d2a8d827e2a946b1861ea"
WEB_TEACHER_KEY = "teacherbd61a36617ac680ebb83c160d"
OA_EncryptingKey = "30a9a958cb11e53c3103fe870be68920"

# 移动端登陆时需要用到的sgin值
IOS_SIGN = '7ios5f576beec73f652a045904ef15101'
ANDROID_SIGN = '6faa3e603feba8003ca858ceb694bc81a'
WEB_SIGN = '2www465b1dbd68d0578f7fa2a28049523'
# 移动端接口用来计算userid的值
USERID_KEYBIN = 30205014


# 获取字符串的md5加密
def get_str_md5(str, isupper=False):
    if type(str) is not bytes:
        str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    a = m.hexdigest()
    if isupper:
        a = a.upper()
    return a

def pkcs7_pad(text, length):
    count = len(text)
    pad_size = length - (count % length)
    text = text + (chr(pad_size) * pad_size)
    return text

def aes_encrypt_cbc(text, key, iv, block_size=16):
    '''
    这里密钥长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
    需要将传入的text,key,iv都转为bytes类型，否则在python3.6中会报错：TypeError: Object type <class 'str'> cannot be passed to C code
    :param text: 需加密的文本
    :param key: 密钥
    :param iv: 模式为CBC时，需指定偏移量
    :param block_size: 可以是8,16,32,64
    :return: 16进制字符串
    '''
    from Crypto.Cipher import AES
    key = key.encode()
    btext = pkcs7_pad(text, block_size).encode()
    iv = iv.encode()
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = cryptor.encrypt(btext)
    return encrypt_text


def hex_str(input):
    # python3.5之前的python3版本，可以用如下方式转换为hex str
    # hex_text=''.join( [ "%02X" % x for x in text ] ).strip()
    # python3.6 可以直接用hex()函数
    if isinstance(input, str):
        input = input.encode()
    return input.hex()


def aes_encrypt_ecb(text, key, block_size=16):
    '''
    aes encrypt with ecb mode
    :param text: text to encrypt
    :param key: key size should be times of 8
    :param block_size: block size
    :return:
    '''
    from Crypto.Cipher import AES
    key = key.encode()
    text = pkcs7_pad(text, block_size).encode()
    cryptor = AES.new(key, AES.MODE_ECB)
    encrypt_text = cryptor.encrypt(text)
    return encrypt_text


def base64_encode_str(input):
    if isinstance(input, str):
        input = input.encode()
    encrypted_content = base64.b64encode(input)
    # 加密后的内容是bytes类型的，要解码为str类型返回
    return encrypted_content.decode()


def encrypt_pc_password(text, key=WEB_AES_KEY, iv=WEB_AES_IV, block_size=16):
    """
    web登录接口密码加密算法
    :param text: 密码
    :param key: 密钥
    :param iv: 密钥偏移量
    :param block_size: 分组块大小
    :return: 16进制字符串
    """
    encrypt_text = aes_encrypt_cbc(text, key, iv, block_size)
    hex_text = hex_str(encrypt_text)
    return hex_text


def encrypt_app_password(text, key=APP_AES_KEY, block_size=16):
    encrypt_text = aes_encrypt_ecb(text, key, block_size)
    b64encode_text = base64_encode_str(encrypt_text)
    return b64encode_text


def check_json_response(response):
    if response.status_code == 200 and response.content:
        try:
            retJson = json.loads(response.content)
        except ValueError as e:
            pass
            # print("Load conetent as json failed: {}".format(e))
        else:
            return retJson
    else:
        # 剩下的情况是：1. response.content为空 2. status_code不为200
        print("Unexpected response of: %s\n" % response.url)
        if not response.content:
            errorMsg = 'response code is %s, but content is None' % response.status_code
            errorMsg += 'input : ' + response.json()
            errorMsg += 'response : ' + response.content
            print(errorMsg)
        else:
            errorMsg = 'response status code is: %s\n' % response.status_code
            errorMsg += 'response content: %s' % response.content
            print(errorMsg)
            # raise AssertionError(errorMsg)
    return response.text


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)

        return inner_func
    return wraper_func


def ding(msg,
         # webhook="https://oapi.dingtalk.com/robot/send?access_token=83a007cf771b185ccd555282513d5ef9c2639e09880ec05d0b96f597a1f4b0f0",
         webhook=ConfigWeb.DING_WEBHOOK_ZHILIANGZU,
         at=["13388601523"]):
    data = {
                "msgtype": "text",
                "text": {
                    "content": msg
                },
                "at": {
                    "atMobiles": at,
                    "isAtAll": False
                }
            }
    logging.info('开始发送钉钉提醒{}'.format(data))
    res = requests.post(url=webhook, json=data, verify=False)
    return res.content.decode('utf-8')


def ding_decorator(**dkargs):
    def wrap(a_func):
        def _wrap(*args):
            a_func(*args)
            try:
                from flask import current_app
                if hasattr(current_app, 'monitor_run'):
                    if hasattr(args[1], '_testMethodDoc'):
                        test_title = args[1]._testMethodDoc
                    else:
                        test_title = args[1].description
                    if hasattr(args[1], '_testMethodName'):
                        test_method_name = args[1]._testMethodName
                    else:
                        test_method_name = args[1].description

                    out_put = '{0}{1}'.format(args[0].result[-1][2], args[0].result[0][3])
                    msgs = '{3} \n用例信息：{0}testMethodName: {1}\n{2}'.format(
                        test_title, test_method_name, out_put, dkargs['msg'])
                    if not dkargs.get('webhook'):
                        ding_conf = {}
                        if hasattr(args[1], '__module__'):
                            ding_key = args[1].__module__.split('.')
                        else:
                            ding_key = ['api_testcases']
                        for i in ding_key[::-1]:
                            if i in ConfigWeb.CONFIG_DING.keys():
                                ding_conf = ConfigWeb.CONFIG_DING[i]
                                break
                        webhook = ding_conf['webhook']
                        at = ding_conf['ding_at']
                    else:
                        webhook = dkargs.get('webhook')
                        at = []
                    print(ding(msg=msgs[:5000], at=at, webhook=webhook))
            except Exception as e:
                logging.error(e)

        return _wrap

    return wrap



