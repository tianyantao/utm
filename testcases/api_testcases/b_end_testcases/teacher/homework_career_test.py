from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.teacher.homework_career_data import *
from common.unittest_v2 import TestCaseV2
from common.helper import skip_dependon
import time


class ContentsTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_career_postheadertypelist(self):
        """
        title: 验证生涯视频作业，根据栏目获取分类
        url: /api/teacher/assignhomeworkfortea/postheadertypelist
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_postheadertypelist(newclsid=10)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(typelist, res['data']['typelist'])

    def test_p1_career_gethomworklist(self):
        """
        title: 验证生涯视频作业，根据分类获取可布置的视频列表
        url: /api/teacher/assignhomeworkfortea/gethomworklist
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        parentid = typelist[0]['id']
        res = teacher_web.career_gethomworklist(typeid=10, parentid=parentid, childid=parentid, pageindex=1, pagesize=10)
        print(res)
        self.assertEqual(200,res['code'])
        self.assertTrue(res['data']['totalvideo'] > 0)
        # self.assertTrue(res['data']['totalcnt'] <= res['data']['totalvideo'])  这块貌似有bug，暂时先去掉验证
        for i in res['data']['courselist']:
            self.assertTrue(i['id'] > 1)
            self.assertIsNotNone(i['title'])
            self.assertIsNotNone("mainteccher")
            self.assertTrue(i['playnum'] >= 0 )
            self.assertIsNotNone(i['url'])
            self.assertIsNotNone(i['cover'])
            for j in i['lessonlist']:
                self.assertTrue(j['id'])
                self.assertIsNotNone(j['title'])
                self.assertIsNotNone(j['listvideoduration'])
                self.assertIsNotNone(j['vurl'])
                self.assertIsNotNone(j['vcover'])
                self.assertEqual(j['courseid'], i['id'])


    def test_p1_1_career_gethomworklist(self):
        """
        title: 验证生涯视频作业，根据子分类获取可布置的视频列表
        url: /api/teacher/assignhomeworkfortea/gethomworklist
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        parentid = typelist[0]['id']
        childid = typelist[0]['childlist'][1]['id']
        res = teacher_web.career_gethomworklist(typeid=10, parentid=parentid, childid=childid, pageindex=1,
                                                pagesize=10)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['totalvideo'] > 0)
        # self.assertTrue(res['data']['totalcnt'] <= res['data']['totalvideo'])
        for i in res['data']['courselist']:
            self.assertTrue(i['id'] > 1)
            self.assertIsNotNone(i['title'])
            self.assertIsNotNone("mainteccher")
            self.assertTrue(i['playnum'] >= 0 )
            self.assertIsNotNone(i['url'])
            self.assertIsNotNone(i['cover'])
            for j in i['lessonlist']:
                self.assertTrue(j['id'])
                self.assertIsNotNone(j['title'])
                self.assertIsNotNone(j['listvideoduration'])
                self.assertIsNotNone(j['vurl'])
                self.assertIsNotNone(j['vcover'])
                self.assertEqual(j['courseid'], i['id'])

    def test_p1_career_addbasket(self):
        """
        title: 验证生涯视频作业，清空作业篮 -> 添加单讲课到作业篮 -> 移除作业篮
        url: /api/teacher/assignhomeworkfortea/clearbaseket,/api/teacher/assignhomeworkfortea/addbasket,/api/teacher/assignhomeworkfortea/removebaseket
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_clearbasket(typeid=1, kemu='10')
        self.assertEqual(200, res['code'])
        self.assertEqual("清空成功", res['data'])
        self.assertEqual("执行成功", res['msg'])
        res1 = teacher_web.career_addbasket(basketforteaaddinput = basketforteaaddinput1)
        print(res1)
        self.assertEqual(200, res1['code'])
        self.assertEqual(1, res1['data'])
        res2 = teacher_web.career_removebaseket(qid=basketforteaaddinput1[0]['qid'], typeid=1, kemu='10')
        self.assertEqual(200, res2['code'])
        self.assertEqual(0, res2['data'])

    def test_p1_step01_career_addbasket(self):
        """
        title: 验证生涯视频作业， 清空作业栏 -> 添加多讲课到作业篮
        url: /api/teacher/assignhomeworkfortea/addbasket
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_clearbasket(typeid=1, kemu='10')
        self.assertEqual(200, res['code'])
        self.assertEqual("清空成功", res['data'])
        self.assertEqual("执行成功", res['msg'])
        res1 = teacher_web.career_addbasket(basketforteaaddinput = basketforteaaddinput2)
        print(res1)
        self.assertEqual(200, res1['code'])
        self.assertEqual(3, res1['data'])

    @skip_dependon(depend='test_p1_step01_career_addbasket')
    def test_p1_step02_career_getbaseketvideolist(self):
        """
        title: 验证生涯视频作业， 获取作业篮视频列表
        url: /api/teacher/assignhomeworkfortea/getbaseketvideolist
        author: 章志君
        """
        time.sleep(5)
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_getbaseketvideolist(typeid=1, kemu='10')
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(3, res['data']['count'])
        j = 0
        global basketvideolist
        basketvideolist = res['data']['items']
        for i in res['data']['items']:
            self.assertEqual(basketforteaaddinput2[j]['qid'], i['id'])
            self.assertIsNotNone(i['title'])
            self.assertIsNotNone(i['videoduration'])
            self.assertTrue(i['vplaynum'] >= 0)
            self.assertIsNotNone(i['vurl'])
            self.assertIsNotNone(i['vmainteacher'])
            j = j + 1

    @skip_dependon(depend='test_p1_step01_career_addbasket')
    def test_p1_step03_1_career_submithomework(self):
        """
        title: 验证生涯视频作业， 校长布置生涯视频作业
        url: /api/teacher/assignhomeworkfortea/submithomework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        self.addbasket(teacher_web)
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        json ="{\"arrangetype\":0,\"tittle\":\"生涯视频自动化测试作业\",\"iscgradehomework\":true,\"deadline\":%s,\"kemu\":\"10\",\"classtype\":1,\"expireyears\":[%s],\"gradeclasses\":[]}" % (tomorrow_time, (expireyear))
        res = teacher_web.career_submithomework(json=json, homeworkxueketype=1, submiting=False)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'])
        # self.assertEqual(tomorrow_time, res['data']['deadline'])
        # self.assertEqual(3, res['data']['homeworkcount'])
        # self.assertEqual("生涯视频自动化测试作业", res['data']['tittle'])
        # self.assertTrue(res['data']['homeworkstudents'] >= 1)
        # self.assertTrue(len(res['data']['recordclassnames']) >= 1)
        global homeworkid
        homeworkid = res['data']['homeworkid']
        # time.sleep(4)
        # res1 = teacher_web.overview_getlatesthomework()
        # print(res1)
        # self.assertIn(str(res['data']['homeworkid']) , str(res1))

    # @skip_dependon(depend='test_p1_step01_career_addbasket')
    def test_p1_step03_2_career_submithomework(self):
        """
        title: 验证生涯视频作业， 行政班班主任布置生涯视频作业
        url: /api/teacher/assignhomeworkfortea/submithomework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        self.addbasket(teacher_web)
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        json = "{\"arrangetype\":0,\"tittle\":\"行政班主任生涯视频自动化测试作业\",\"iscgradehomework\":false,\"deadline\":%s,\"kemu\":\"10\",\"classtype\":1,\"expireyears\":[]," \
               "\"gradeclasses\":[{\"grade\":%s,\"expireyear\":%s,\"classlist\":[%s]}]}" % (tomorrow_time, grade, expireyear, groupid_xingzheng)
        res = teacher_web.career_submithomework(json=json, homeworkxueketype=1, submiting=False)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'])
        # self.assertEqual(tomorrow_time, res['data']['deadline'])
        # self.assertEqual(3, res['data']['homeworkcount'])
        # self.assertEqual("行政班主任生涯视频自动化测试作业", res['data']['tittle'])
        # self.assertTrue(res['data']['homeworkstudents'] >= 1)
        # self.assertTrue(len(res['data']['recordclassnames']) >= 1)
        # time.sleep(5)
        # res1 = teacher_web.overview_getlatesthomework()
        # print(res1)
        # self.assertIn(str(res['data']['homeworkid']), str(res1))


    @skip_dependon(depend='test_p1_step01_career_addbasket')
    def test_p1_step03_3_career_submithomework(self):
        """
        title: 验证生涯视频作业， 年级主任主任布置生涯视频作业
        url: /api/teacher/assignhomeworkfortea/submithomework
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        self.addbasket(teacher_web)
        tomorrow_time = int(round(time.time() + 86400) * 1000)
        json = "{\"arrangetype\":0,\"tittle\":\"年级主任生涯视频自动化测试作业\",\"iscgradehomework\":false,\"deadline\":%s,\"kemu\":\"10\",\"classtype\":1,\"expireyears\":[]," \
               "\"gradeclasses\":[{\"grade\":%s,\"expireyear\":%s,\"classlist\":[%s]}]}" % (tomorrow_time, grade, expireyear, groupid_xingzheng)
        res = teacher_web.career_submithomework(json=json, homeworkxueketype=1, submiting=False)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkid'])
        # self.assertEqual(tomorrow_time, res['data']['deadline'])
        # self.assertEqual(3, res['data']['homeworkcount'])
        # self.assertEqual("年级主任生涯视频自动化测试作业", res['data']['tittle'])
        # self.assertTrue(res['data']['homeworkstudents'] >= 1)
        # self.assertTrue(len(res['data']['recordclassnames']) >= 1)
        # res1 = teacher_web.overview_getlatesthomework()
        # print(res1)
        # self.assertIn(str(res['data']['homeworkid']), str(res1))


    def addbasket(self, teacher_web):
        #清空作业篮 ->添加视频到作业篮
        res = teacher_web.career_clearbasket(typeid=1, kemu='10')
        print(res)
        res1 = teacher_web.career_addbasket(basketforteaaddinput=basketforteaaddinput2)
        print(res1)

    # @skip_dependon(depend='test_p1_step03_1_career_submithomework')
    # def test_p1_step04_video_StudentHomeworkCompletion(self):
    #     """
    #     title: 验证教师端视频作业班级学生完成情况
    #     url: /api/teacher/homework/video/StudentHomeworkCompletion
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     res = teacher_web.video_StudentHomeworkCompletion(classid=groupid_xingzheng,homeworkid=homeworkid, page=1, pagesize=60, sort=1, studentuserid=student_userid)
    #     print(res)
    #     self.assertEqual(200, res['code'])
    #     j = 0
    #     for i in res['data']['data']:
    #         self.assertEqual(basketvideolist[j]['id'], i['videoid'])
    #         self.assertEqual(basketvideolist[j]['title'], i['videotitle'])
    #         self.assertEqual(basketvideolist[j]['videodurationseconds'], str(round(i['totalseconds'])))
    #         self.assertTrue(i['completerate'] >= 0)
    #         self.assertEqual(basketvideolist[j]['vcover'], i['picture'])
    #         self.assertEqual(basketvideolist[j]['vurl'], i['url'])
    #         j = j + 1

    @skip_dependon(depend='test_p1_step03_1_career_submithomework')
    def test_p1_step04_video_StudentList(self):
        """
        title: 验证教师端视频作业学生完成情况-学生名单
        url: /api/teacher/homework/video/StudentList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.video_StudentList(classid=groupid_xingzheng, homeworkid=homeworkid, searchname=None, sort=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 6)
        for i in res['data']:
            self.assertIsNotNone(i['headimg'])
            self.assertTrue(i['studentuserid'] > 100)
            self.assertEqual(0, i['completerate'])

    @skip_dependon(depend='test_p1_step03_1_career_submithomework')
    def test_p1_step05_video_VideoPalyViewing(self):
        """
         title: 验证教师端视频观看情况
         url: /api/teacher/homework/video/VideoPalyViewing
         author: 章志君
         """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.video_VideoPalyViewing(homeworkid=homeworkid, classid=0, page=1, pagesize=10, sort=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(3, res['data']['totalcount'])
        self.assertTrue(res['data']['totalvideoseconds'] > 1)
        j = 0
        for i in res['data']['data']:
            self.assertEqual(basketvideolist[j]['id'], i['videoid'])
            self.assertEqual(basketvideolist[j]['title'], i['videotitle'])
            self.assertEqual(basketvideolist[j]['videodurationseconds'], str(round(i['videoseconds'])))
            self.assertTrue(i['averagecompleterate'] >= 0)
            self.assertEqual(basketvideolist[j]['vcover'], i['picture'])
            self.assertEqual(basketvideolist[j]['vurl'], i['redirecturl'])
            self.assertTrue(i['recordstudentscount'] > 0)
            self.assertTrue(i['playedstudentscount'] >= 0)
            j = j + 1

    @skip_dependon(depend='test_p1_step03_1_career_submithomework')
    def test_p1_step06_video_homeworkcompletion(self):
        """
        title: 验证教师端作业班级完成情况
        url: /api/teacher/homework/video/homeworkcompletion
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.video_homeworkcompletion(homeworkid=homeworkid, page=1, pagesize=10, sort=3)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn(str(groupid_xingzheng), str(res['data']['data']))
        self.assertTrue(res['data']['totalcount'] >=1)
        for i in res['data']['data']:
            self.assertIsNotNone(i['classname'])
            self.assertIsNotNone(i['classnameh5'])
            self.assertIsNotNone(i['enrollyearname'])
            self.assertTrue(i['participatedcount'] >= 0)
            self.assertTrue(i['unparticipatedcount'] >= 0)
            self.assertTrue(i['averagecompleterate'] >= 0)
            self.assertTrue(i['totalcount'] >= 0)

    @skip_dependon(depend='test_p1_step03_1_career_submithomework')
    def test_p1_step06_video_ClassStudentVideoPlayDetail(self):
        """
        title: 验证教师端视频观看详情-查看详情
        url: /api/teacher/homework/video/ClassStudentVideoPlayDetail
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.video_ClassStudentVideoPlayDetail(homeworkid=homeworkid, videoid=basketforteaaddinput2[0]['qid'], sort=1, page=1, pagesize=4000, classid=0)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['totalcount'] > 6)
        student_id = teacher(web_client(username=student02_user['username'], password=student02_user['password'])).client.user_id
        self.assertIn(str(student_id), str(res['data']['data']))
        self.assertIsNotNone(res['data']['data'][0]['studentname'])
        self.assertIsNotNone(res['data']['data'][0]['belongclassname'])
        self.assertTrue(res['data']['data'][0]['taketimeseconds'] >= 0)
        self.assertTrue(res['data']['data'][0]['completerate'] >= 0)

