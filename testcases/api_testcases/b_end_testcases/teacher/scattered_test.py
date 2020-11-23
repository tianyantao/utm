from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class ContentsTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_ads_getbanners(self):
        """
        title: 验证教师端首页获取广告
        url: /api/services/ads/ads/GetBanners
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.ads_getbanners()
        print(res)
        self.assertTrue(200, res['code'])
        self.assertEqual(len(res['data']['banners']),res['data']['totalcount'])
        self.assertTrue(res['data']['totalcount'] >= 1)
        for i in res['data']['banners']:
            self.assertIsNotNone(i['bannername'])
            self.assertIsNotNone(i['imageurl'])
            self.assertTrue(i['bannerid'] > 0)

    def test_p1_overview_getlatesthomework(self):
        """
        title: 验证教师端概览页最新作业列表
        url: /api/teacher/overview/getlatesthomework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.overview_getlatesthomework()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['homeworklist']) == 5, "最近作业显示少于5条")
        self.assertTrue(res['data']['count'] > 10, "作业总数返回错误")
        for i in  res['data']['homeworklist']:
            self.assertIsNotNone(i['sourcehomeworktype'])
            self.assertIsNotNone(i["homeworkkemu"])
            self.assertIsNotNone(i["homeworktypename"])
            self.assertIsNotNone(i['tittle'])
            self.assertTrue(i['homeworkid'] > 1)
            self.assertIsNotNone(i['starttime'])
            self.assertIsNotNone(i['deadline'])
            self.assertTrue(i['totalcount'] >= 0)
            self.assertTrue(len(i['recordclassnames']) >= 1)