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

    def test_post_getnewpaperinfo(self):
        """
        title: 获取某学科下最新的N张试卷的基础信息，不查询题目信息
        url: /api/paperservice/client/paper/info/getnewpaperinfo
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_getnewpaperinfo(subjectId=1, num=8, paperTypeList=[1])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertTrue(res['data'][0]['typeName'])
        self.assertIn('paperStatusName', res['data'][0])
        self.assertTrue(len(res['data'][0]['paperName']) >= 1)

    def test_post_addpaperusecount(self):
        """
        title: 增加某试卷某业务场景下的使用次数，单表修改数据
        url: /api/paperservice/client/paper/info/addpaperusecount
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_addpaperusecount(paperId=paperId, bizCode=101)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertTrue(res['data'] != None)

    def test_post_batchInfo(self):
        """
        title: 批量获取章节目录信息
        url: /api/paperservice/paper/chapter/batchInfo
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_batchInfo(chapterIds=[1])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual('教材同步', res['data'][0]['chapterName'])
        self.assertIn('chapterLevel', res['data'][0])

    def test_get_top(self):
        """
        title: 根据学科ID获取顶层目录分类
        url: /api/paperservice/paper/chapter/top
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_top(subjectId=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(1, res['data'][0]['subjectId'])
        self.assertEqual('教材同步', res['data'][0]['chapterName'])

    def test_get_childrenChapterByRelativeLevel(self):
        """
        title: 相对层级：根据目录ID获取下层目录基础信息
        url: /api/paperservice/paper/chapter/childrenChapterByRelativeLevel
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_childrenChapterByRelativeLevel(chapterId=1, relativeLevel=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual('教材同步', res['data']['chapterName'])
        self.assertTrue(len(res['data']['childrenList']) >= 1)

    def test_get_childrenChapter(self):
        """
        title: 根据目录ID获取所有子目录基础信息_树形结构
        url: /api/paperservice/paper/chapter/childrenChapter
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_childrenChapter(chapterId=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual('教材同步', res['data']['chapterName'])
        self.assertTrue(len(res['data']['childrenList']) >= 1)

    def test_get_childrenChapterIds(self):
        """
        title: 根据目录ID获取所有子目录ID列表_非树形
        url: /api/paperservice/paper/chapter/childrenChapterIds
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_childrenChapterIds(chapterId=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertTrue(len(res['data']) >= 1)

    def test_get_paperTypeSearchParam(self):
        """
        title: 根据章节目录ID获取试卷类型及标签筛选列表（内部教研组的卷子）
        url: /api/paperservice/paper/chapter/paperTypeSearchParam
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_paperTypeSearchParam(chapterId=1, platform=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertTrue(res['data'][0]['typeName'])
        self.assertTrue(len(res['data'][0]['tagList']) >= 1)

    def test_post_selectpaper(self):
        """
        title: 根据学科试卷类型标签及章节目录搜索试卷-带分页
        url: /api/paperservice/client/paper/info/selectpaper
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_selectpaper(pageSize=10, pageIndex=1, subjectId=1, typeId=2, platform=1, createSource=0,
                                        chapterId=1, tagValueList=tagValueList)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertIn('totalPages', res['data'])

    def test_get_detail(self):
        """
        title: 根据试卷类型获取标签及标签字段值
        url:/api/paperservice/admin/paper/type/detail
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.get_detail(id=1)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertEqual(1, res['data']['id'])
        self.assertEqual('章测', res['data']['typeName'])
        self.assertTrue(len(res['data']['platformList']) >= 1)

    def test_post_getbaseinfo(self):
        """
        title: 批量获取试卷基础信息，不查询题目信息
        url: /api/paperservice/client/paper/info/getbaseinfo
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_getbaseinfo(list=[{'paperId': paperId, 'bizCode': 201}])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('43739', res['data'][0]['id'])
        self.assertIn('paperName', res['data'][0])
        self.assertTrue(len(res['data'][0]['chapterValueList']) >= 1)

    def test_post_getpaperdetailinfo(self):
        """
        title: 批量获取试卷详细信息，查询题目信息（批量通过题目id获取题目内容信息）
        url: /api/paperservice/client/paper/info/getpaperdetailinfo
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_getpaperdetailinfo(bizCode=201, list=[{'paperId': paperId}])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(str(paperId), res['data'][0]['id'])
        self.assertIn('paperName', res['data'][0])
        self.assertTrue(len(res['data'][0]['questionList']) >= 1)

    def test_post_getpaperusecount(self):
        """
        title: 获取试卷某业务场景下的使用次数，单表查询
        url: /api/paperservice/client/paper/info/getpaperusecount
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_getpaperusecount(bizCode=201, paperIdList=[{'paperId': paperId}])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(paperId, res['data'][0]['id'])
        self.assertTrue(res['data'][0]['num'] >= 1)

    def test_post_addpublishedpaperc(self):
        """
        title: C端创建自主训练等试卷
        url: /api/paperservice/client/paper/info/addpublishedpaperc
        author: 廖文龙
        """
        tiku_web = tiku(WebClient(username=user_vip['username'], password=user_vip['password']))
        res = tiku_web.post_addpublishedpaperc(creater=tiku_web.client.user_id, paperName='性能测试数据', platformList=1,
                                               subjectId=1, questionIdList=[
                {"questionId": "2683947497210363904", "source": 2}, {"questionId": "2683947514390233139", "source": 2},
                {"questionId": "2683947497210363904", "source": 2}, {"questionId": "2683947514390233139", "source": 2},
                {"questionId": "1683946706936381604", "source": 2}])
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual('操作成功', res['msg'])
        self.assertTrue(res['data'] >= 1)
