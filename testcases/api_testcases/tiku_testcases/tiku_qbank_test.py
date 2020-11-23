from common.unittest_v2 import TestCaseV2
from lib.api_lib.tiku.tiku_api import Tiku as tiku
from lib.api_lib.ewt_client import WebClient
from testcases.api_testcases.tiku_testcases.tiku_data import *
import unittest
from config.config_env import get_env


@unittest.skipIf(get_env() != 'prod', "线下case还未跑通")
class SubjectTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass
        # cls.tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
    @classmethod
    def tearDownClass(cls):
        pass

    def test_post_unioncheck(self):
        """
        title: 聚合接口-查询题目信息（自建题库、菁优题库和老数据）
        url: /api/qbank/uniform/question/info
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_Unioncheck(questionIdList=questionIdList)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertIn('questionId', res['data'][0])
        self.assertIn('optionsList', res['data'][0])
        self.assertIn('optionsObjectList', res['data'][0])
