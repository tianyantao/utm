from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.teacher.homework_sbr_video_data import *
from common.unittest_v2 import TestCaseV2
import time


class ContentsTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_step01_1_sbrvideo_getvideos(self):
        """
        title: 验证教师端获取语文科目的所有年级全部知识点的校本视频列表
        url: /api/teacher/homework/sbr/getvideos
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_getvideos(kemu=1, grades=[0], page=1,pagesize=10)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(1, res['data']['currentpage'])
        self.assertTrue(res['data']['totalpage'] >= 1)
        self.assertTrue(len(res['data']['datalist']) > 0)
        for i in res['data']['datalist']:
            self.assertTrue(i['id'] > 0)
            self.assertIsNotNone(i['title'])
            # self.assertEqual('5', i['status'])
            self.assertTrue(i['playtimes'] >= 0)
            self.assertTrue(i['videoplaytime'] >= 0)
            self.assertIsNotNone(i['thumbnailurl'])
            self.assertIsNotNone(i['playurl'])


    def test_p1_step01_2_sbrvideo_getvideos(self):
        """
        title: 验证教师端获取语文科目的高一年级某一知识点的校本视频列表
        url: /api/teacher/homework/sbr/getvideos
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_getvideos(kemu=1, grades=[0], page=1, pagesize=10, KnowLedgeId=knowLedgeIds)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['datalist']) > 0)
        for i in res['data']['datalist']:
            self.assertTrue(i['id'] > 0)
            self.assertIsNotNone(i['title'])
            # self.assertEqual('5', i['status'])
            self.assertTrue(i['playtimes'] >= 0)
            self.assertTrue(i['videoplaytime'] >= 0)
            self.assertIsNotNone(i['thumbnailurl'])
            self.assertIsNotNone(i['playurl'])

    def test_p1_step02_sbrvideo_getavailablegrades(self):
        """
        title: 验证教师端获取校本视频的适用年级
        url: /api/teacher/homework/sbr/getavailablegrades
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_getavailablegrades()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) >= 4)
        self.assertEqual("全部", res['data'][0]['name'])
        self.assertIn("高一", str(res['data']))

    def test_p1_step03_sbrvideo_removefromsbrbasket(self):
        """
        title: 验证教师端校本视频作业篮清空 -> 添加校本单个视频 -> 删除作业篮子中的校本资源
        url: /api/teacher/homework/sbr/clearsbrbasket, /api/teacher/homework/sbr/addtosbrbasket, /api/teacher/homework/sbr/removefromsbrbasket
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_clearsbrbasket(homeworksbrtype=1, kemu=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("清空成功", res['data'])
        res1 = teacher_web.sbrvideo_addtosbrbasket(homeworksbrtype=1, basketaddinputs=basketaddinputs1)
        print(res1)
        self.assertEqual(200, res1['code'])
        self.assertEqual(len(basketaddinputs1), res1['data'])
        rid = basketaddinputs1[0]['Qid']
        res2 = teacher_web.sbrvideo_removefromsbrbasket(rid=rid, homeworksbrtype=1, kemu=1)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertEqual(0, res2['data'])

    def test_p1_step04_sbrvideo_addtosbrbasket(self):
        """
        title: 验证教师端校本视频作业篮清空 -> 添加校本三个个视频 -> 删除作业篮子中的校本资源
        url: /api/teacher/homework/sbr/clearsbrbasket, /api/teacher/homework/sbr/addtosbrbasket
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_clearsbrbasket(homeworksbrtype=1, kemu=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("清空成功", res['data'])
        res1 = teacher_web.sbrvideo_addtosbrbasket(homeworksbrtype=1, basketaddinputs=basketaddinputs2)
        print(res1)
        self.assertEqual(200, res1['code'])
        self.assertEqual(len(basketaddinputs2), res1['data'])

    def test_p1_step05_sbrvideo_gesbrbasketitems(self):
        """
        title: 验证教师端获取校本资源作业篮子列表
        url: /api/teacher/homework/sbr/gesbrbasketitem
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrvideo_gesbrbasketitems(page=1, pagesize=10,homeworksbrtype=1, kemu=1)
        print(res)
        self.assertEqual(200, res['code'])
        if self.addsbrvideotobasket(teacher_web) == False:
            self.assertFalse("添加视频失败")
        time.sleep(sleeptime)
        res1 = teacher_web.sbrvideo_gesbrbasketitems(page=1, pagesize=10, homeworksbrtype=1, kemu=1)
        print(res1)
        self.assertEqual(200, res1['code'])
        self.assertEqual(1, res['data']['totalpage'])
        self.assertEqual(len(basketaddinputs2), res['data']['totalrecord'])
        self.assertEqual(len(basketaddinputs2), len(res['data']['datalist']))
        res2 = teacher_web.sbrvideo_getvideos(kemu=1, grades=[0], page=1, pagesize=10)
        for i in res2['data']['datalist']:
            for j in res['data']['datalist']:
                if j['id'] == i['id']:
                    self.assertEqual(i,j)

    def test_p1_step06_1_sbrvideo_set_homework(self):
        """
        title: 验证教师端校长布置校本视频作业_布置给高三年级,注册非注册学生均有收到作业
        url: /api/teacher/homework/sbr/set/homework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = "校本视频自动化测试"
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        self.addsbrvideotobasket(teacher_web)
        res = teacher_web.sbrvideo_set_homework(arrangetype=0, classtype=1, title=title, isgradehomework=True, deadline=tomorrow_time, kemu=1, expireyears=[expireyear], gradeclasses=[] )
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'] > 0)
        time.sleep(sleeptime)
        #学生端查看作业列表
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res2['data']))
        student_web = teacher(web_client(username=student02_user['username']))
        res3 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res3)
        self.assertEqual(200, res3['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res3['data']))


    def test_p1_step06_2_sbrvideo_set_homework(self):
        """
        title: 验证教师端布置校本视频作业_行政班主任布置给某个班级
        url: /api/teacher/homework/sbr/set/homework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        self.addsbrvideotobasket(teacher_web)
        title = "行政班主任布置校本视频自动化测试"
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        gradeclasses = [{"Grade":grade, "ExpireYear":expireyear, "ClassList":[groupid_xingzheng]}]
        res = teacher_web.sbrvideo_set_homework(arrangetype=0, classtype=1, title=title, isgradehomework=False, deadline=tomorrow_time, \
                                                kemu=1, expireyears=[], gradeclasses=gradeclasses)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'] > 0)
        # 学生端查看作业列表
        time.sleep(sleeptime)
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res2['data']))
        student_web = teacher(web_client(username=student02_user['username']))
        res3 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res3)
        self.assertEqual(200, res3['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res3['data']))

    def test_p1_step06_3_sbrvideo_set_homework(self):
        """
        title: 验证教师端布置校本视频作业_教学班主任布置给某个班级
        url: /api/teacher/homework/sbr/set/homework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        self.addsbrvideotobasket(teacher_web)
        title = "教学班主任布置校本视频自动化测试"
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        gradeclasses = [{"Grade": grade, "ExpireYear": expireyear, "ClassList": [groupid_jiaoxue]}]
        res = teacher_web.sbrvideo_set_homework(arrangetype=0, classtype=2, title=title, isgradehomework=False,
                                                deadline=tomorrow_time, \
                                                kemu=1, expireyears=[], gradeclasses=gradeclasses)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'] > 0)
        # 学生端查看作业列表
        time.sleep(sleeptime)
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res2['data']))
        student_web = teacher(web_client(username=student02_user['username']))
        res3 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res3)
        self.assertEqual(200, res3['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res3['data']))

    def test_p1_step06_4_sbrvideo_set_homework(self):
        """
        title: 验证教师端布置校本视频作业_学科老师主任布置年级作业
        url: /api/teacher/homework/sbr/set/homework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        self.addsbrvideotobasket(teacher_web)
        title = "学科老师布置校本视频自动化测试"
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        gradeclasses = [{"Grade":grade, "ExpireYear":expireyear, "ClassList":[groupid_xingzheng]}]
        res = teacher_web.sbrvideo_set_homework(arrangetype=0, classtype=1, title=title, isgradehomework=False, deadline=tomorrow_time, \
                                                kemu=1, expireyears=[], gradeclasses=gradeclasses)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'] > 0)
        # 学生端查看作业列表
        time.sleep(sleeptime)
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res2['data']))
        student_web = teacher(web_client(username=student02_user['username']))
        res3 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=60)
        print(res3)
        self.assertEqual(200, res3['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res3['data']))

    def test_p1_step06_5_sbrvideo_set_homework(self):
        """
        title: 验证教师端布置校本视频作业_年级主任布置年级作业
        url: /api/teacher/homework/sbr/set/homework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        self.addsbrvideotobasket(teacher_web)
        title = "年级主任布置校本视频自动化测试"
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        res = teacher_web.sbrvideo_set_homework(arrangetype=0, classtype=1, title=title, isgradehomework=True,
                                                deadline=tomorrow_time, \
                                                kemu=1, expireyears=[expireyear], gradeclasses=[])
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'] > 0)
        # 学生端查看作业列表
        time.sleep(sleeptime)
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=50)
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res2['data']))
        student_web = teacher(web_client(username=student02_user['username']))
        res3 = student_web.get_homeworklist_student_pc(homeworktype=1, homeworkstatus=1, pagesize=50)
        print(res3)
        self.assertEqual(200, res3['code'])
        self.assertIn(str(res['data']['homeworkid']), str(res3['data']))

    # def getKnowledgeid(self, teacher_web):
    #     res = teacher_web.get_getknowledgelist(kemu=1)
    #     return res['data'][0]['list'][0]['childnodes'][0]['id']

    def addsbrvideotobasket(self, teacher_web):
        res = teacher_web.sbrvideo_clearsbrbasket(homeworksbrtype=1, kemu=1)
        res1 = teacher_web.sbrvideo_addtosbrbasket(homeworksbrtype=1, basketaddinputs=basketaddinputs2)
        if res1['data'] == (len(basketaddinputs2)):
            return True
        else:
            return False
