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
        # cls.tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_post_answerreport(self):
        """
        title: 查看答题报告
        url: /api/answerservice/answer/queryAnswerReports
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_AnswerReport(userId=tiku_web.client.user_id, platformList=[9], bizCodeList=[100],
                                         subjectId=2, isFinished=1, paperIdList=[
                paperId], reportIdList=reportIdList, isAllRight=1, paperLimit=100)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(paperId, res['data'][0]['paperId'])
        self.assertIn('reportId', res['data'][0])
        self.assertIn('paperTitle', res['data'][0])

    def test_post_questionParse(self):
        """
        title: 查看答题解析
        url: /api/answerservice/answer/getQuestionParse
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_QuestionParse(userId=tiku_web.client.user_id, reportId=reportId, platform=9,
                                          paperId=paperId, questionId=questionId, bizCode=100)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(questionId, res['data']['id'])
        self.assertTrue(res['data']['content'] != None)
        self.assertTrue(res['data']['options'] != None)

    def test_get_createReport(self):
        """
        title: 创建答题报告
        url: /api/answerservice/answer/createReport
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_CreateReport(userId=tiku_web.client.user_id, platform=1, paperId=paperId,
                                        bizCode=100)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(paperId, res['data']['paperId'])
        self.assertIn('reportId', res['data'])
        self.assertIn('paperTitle', res['data'])

    def test_get_answerReportDetail(self):
        """
        title: 查看学生答题详情信息
        url: /api/answerservice/answer/getAnswerReportDetail
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_AnswerReportDetail(userId=tiku_web.client.user_id, platform=9,
                                              reportId=reportId, bizCode=100)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(paperId, res['data']['paperId'])
        self.assertTrue(res['data']['paperTitle'] != None)
        self.assertTrue(res['data']['knowledgeList'] != None)

    def test_get_questionInfosByIds(self):
        """
        title: 查询试卷下试题的详细信息
        url: /api/answerservice/answer/getQuestionInfosByIds
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_QuestionInfosByIds(platform=9, paperId=paperId, bizCode=100,
                                              questionIds=questionId)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(paperId, res['data']['paperId'])
        self.assertTrue(res['data']['paperTitle'] != None)
        self.assertTrue(res['data']['questionList'] != None)

    def test_get_questionIdsByPaperId(self):
        """
        title: 查询试卷下所有试题ID列表
        url: /api/answerservice/answer/getQuestionIdsByPaperId
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_QuestionIdsByPaperId(platform=9, paperId=paperId, bizCode=100)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(paperId, res['data']['paperId'])
        self.assertTrue(res['data']['paperTitle'] != None)
        self.assertTrue(res['data']['questionList'] != None)

    def test_get_OrCreateReport(self):
        """
        title: 查询或者新增答题报告
        url: /api/answerservice/answer/getOrCreateReport
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_OrCreateReport(userId=tiku_web.client.user_id, platform=9, paperId=paperId,
                                          bizCode=100, isRepeat=1, reportId=reportId)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(int(reportId), res['data']['reportId'])
        self.assertEqual(paperId, res['data']['paperId'])
        self.assertTrue(res['data']['paperTitle'] != None)
