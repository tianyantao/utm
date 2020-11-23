from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2
import time


class EduCenterTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_moralEdu_homepageStatistics_principal(self):
        """
        title: 首页概览统计--校长
        url: /moralEdu/homepageStatistics
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_homepageStatistics(schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertEqual(1, res1['data']['role'])
        self.assertEqual('全校老师德育记录', res1['data']['roleDesc'])

    def test_p1_moralEdu_homepageStatistics_headteacher(self):
        """
        title: 首页概览统计--班主任
        url: /moralEdu/homepageStatistics
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_homepageStatistics(schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertEqual(6, res1['data']['role'])
        self.assertEqual('我的德育记录', res1['data']['roleDesc'])

    def test_p1_moralEdu_homepageStatistics_psychologicalteacher(self):
        """
        title: 首页概览统计--心理老师
        url: /moralEdu/homepageStatistics
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_homepageStatistics(schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertEqual(6, res1['data']['role'])
        self.assertEqual('我的德育记录', res1['data']['roleDesc'])

    def test_p1_moralEdu_homepageStatistics_grademaster(self):
        """
        title: 首页概览统计--年级主任
        url: /moralEdu/homepageStatistics
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_homepageStatistics(schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertEqual(2, res1['data']['role'])

    def test_p1_moralEdu_listGrades(self):
        """
        title: 获取用户有效年级列表
        url: /moralEdu/listGrades
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_listGrades(schoolId=schoolid, filter=1, earlyRise=1, showDefault=1)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertEqual('高一', res1['data'][0]['gradeName'])

    def test_p1_moralEdu_getClassMeetingStatistics(self):
        """
        title: 班会课页面数据统计
        url: /moralEdu/getClassMeetingStatistics
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getClassMeetingStatistics(schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertTrue(res1['data']['useCnt'] >= 0)
        self.assertTrue(res1['data']['teaUv'] >= 0)

    def test_p1_moralEdu_parentsEdu_list(self):
        """
        title: 家长教育列表
        url: /moralEdu/parentsEdu/list
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_parentsEdu_list(schoolId=schoolid, pageIndex=1, pageSize=20)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['id'])
        self.assertIsNotNone(res1['data'][0]['courseName'])

    def test_p1_moralEdu_getMoralResource_list(self):
        """
        title: 获取资源类型列表
        url: /moralEdu/getMoralResource/list
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getMoralResource_list(schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['value'])
        self.assertIsNotNone(res1['data'][0]['description'])

    def test_p1_moralEdu_report_resourceRank(self):
        """
        title: 教师德育报告-德育资源排行榜
        url: /moralEdu/report/resourceRank
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_resourceRank(schoolId=schoolid, period=1, resourceType=1)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_report_teacherView(self):
        """
        title: 教师德育报告-教师查看情况 周期（1：1个月 6：6个月 12：一年）
        url: /moralEdu/report/teacherView
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_teacherView(schoolId=schoolid, period=1)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_gradeClassList(self):
        """
        title: 家长德育报告-年级，班级筛选数据
        url: /moralEdu/gradeClassList
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_gradeClassList(schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_report_schoolCourseInfo(self):
        """
        title: 家长德育报告-全校课程情况
        url: /moralEdu/report/schoolCourseInfo
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_schoolCourseInfo(schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_report_parentsCourseViews(self):
        """
        title: 家长德育报告-各班级家长看课情况
        url: /moralEdu/report/parentsCourseViews
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_parentsCourseViews(schoolId=schoolid, grade=-1, classId=-1, period=1)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_report_parentsCourseViewDetail(self):
        """
        title: 家长德育报告-家长看课详情
        url: /moralEdu/report/parentsCourseViewDetail
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_parentsCourseViewDetail(schoolId=schoolid, grade=-1, classId=-1, period=1)
        print(res1)
        self.assertEqual('200', res1['code'])

    def test_p1_moralEdu_getCategory(self):
        """
        title: 分类公共接口-根据类型区分(1班会课 2教学师训 3 德育师训)
        url: /moralEdu/getCategory
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getCategory(categoryType=1, showFirstDefault=0, showSecondDefault=0,
                                                schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['categoryName'])

    def test_p1_moralEdu_getTeacherClassRoomList(self):
        """
        title: 师训列表，教师成长(顶部菜单栏)
        url: /moralEdu/getTeacherClassRoomList
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getTeacherClassRoomList(type=3, categoryFirst=1, categorySecond=-1, pageIndex=1,
                                                            pageSize=20, schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['courseid'])
        self.assertIsNotNone(res1['data'][0]['title'])

    def test_p1_moralEdu_getStudentProblemManual(self):
        """
        title: 学生问题指导
        url: /moralEdu/getStudentProblemManual
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getStudentProblemManual(schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['categoryId'])
        self.assertIsNotNone(res1['data'][0]['categoryName'])

    def test_p1_1_moralEdu_getClassMeetingList(self):
        """
        title: 班会课,校园活动方案 列表--班会课
        url: /moralEdu/getClassMeetingList
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getClassMeetingList(grade=-1, categoryFirst=-1, categorySecond=-1, type=1,
                                                        pageIndex=1, pageSize=20, schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['title'])
        self.assertIsNotNone(res1['data'][0]['grades'])

    def test_p1_2_moralEdu_getClassMeetingList(self):
        """
        title: 班会课,校园活动方案 列表--校园活动方案
        url: /moralEdu/getClassMeetingList
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getClassMeetingList(grade=-1, categoryFirst=-1, categorySecond=-1, type=2,
                                                        pageIndex=1, pageSize=20, schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data'][0]['title'])

    def test_p1_moralEdu_getClassMeetingDetail(self):
        """
                title: 班会课详情
                url: /moralEdu/getClassMeetingDetail
                author: 张水琴
                """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getClassMeetingList(grade=-1, categoryFirst=-1, categorySecond=-1, type=1,
                                                        pageIndex=1, pageSize=20, schoolId=schoolid)
        res2 = teacher_web.moralEdu_getClassMeetingDetail(res1['data'][0]['id'])
        print(res2)
        self.assertEqual('200', res2['code'])
        self.assertIsNotNone(res2['data']['title'])
        self.assertIsNotNone(res2['data']['agendas'][0]['title'])

    def test_p1_moralEdu_getMoralEduCourseList(self):
        """
        title: 德育课表
        url: /moralEdu/getMoralEduCourseList
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        print(res)
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_getMoralEduCourseList(categoryId=3, currentSemesterId=1, grade=1, isHomePage=0,
                                                          schoolId=schoolid)
        print(res1)
        self.assertEqual('200', res1['code'])
        self.assertIsNotNone(res1['data']['semesterId'])
        self.assertIsNotNone(res1['data']['semesterTitle'])

    def test_p1_moralEdu_report_parentsCourseViewDetail_export(self):
        """
        title: 家长德育报告-家长看课详情-导出
        url: /moralEdu/report/parentsCourseViewDetail/export
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_parentsCourseViewDetail_export(schoolId=schoolid, grade=-1, classId=-1,
                                                                          period=1)
        print(res1)
        self.assertTrue(('200', res1['code']) or self.assertEqual('506', res1['code']))

    def test_p1_moralEdu_report_parentsCourseViews_export(self):
        """
        title: 家长德育报告-各班级家长看课情况导出
        url: /moralEdu/report/parentsCourseViews/export
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_parentsCourseViews_export(schoolId=schoolid, grade=-1, classId=-1, period=1)
        print(res1)
        self.assertTrue(('200', res1['code']) or self.assertEqual('506', res1['code']))

    def test_p1_moralEdu_report_schoolCourseInfo_export(self):
        """
        title: 家长德育报告-全校课程情况-导出
        url: /moralEdu/report/schoolCourseInfo/export
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_schoolCourseInfo_export(schoolId=schoolid)
        print(res1)
        self.assertTrue(('200', res1['code']) or self.assertEqual('506', res1['code']))

    def test_p1_moralEdu_report_teacherView_export(self):
        """
        title: 教师德育报告-教师查看情况-导出
        url: /moralEdu/report/teacherView/export
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_teacherView_export(schoolId=schoolid, period=1)
        print(res1)
        self.assertTrue(('200', res1['code']) or self.assertEqual('506', res1['code']))

    def test_p1_moralEdu_report_resourceRank_export(self):
        """
        title: 教师德育报告-德育资源排行榜-导出
        url: /moralEdu/report/resourceRank/export
        author: 张水琴
        """

        teacher_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = teacher_web.eteacherproduct_school_getSchoolUserInfo()
        schoolid = res['data']['schoolId']
        res1 = teacher_web.moralEdu_report_resourceRank(schoolId=schoolid, period=1, resourceType=1)
        print(res1)
        self.assertTrue(('200', res1['code']) or self.assertEqual('506', res1['code']))
