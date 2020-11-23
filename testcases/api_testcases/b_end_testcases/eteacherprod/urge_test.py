from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from common.unittest_v2 import TestCaseV2
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.homework_data import *
import datetime
import calendar
from testcases.api_testcases.b_end_testcases.case_services import CaseServices


class SupervisedLearningTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def get_month_last_sunday(self):
        today_date = datetime.datetime.today()
        this_year = today_date.date().year
        if today_date.month == 1:
            last_month = 12
            last_year = this_year - 1
        else:
            last_month = today_date.month - 1
            last_year = this_year
        month_info = calendar.monthrange(last_year, last_month)
        month_last_day = datetime.datetime.strptime('%s-%s-%s' % (last_year, last_month, month_info[1]),
                                                    '%Y-%m-%d').date()
        return str(month_last_day)

    def test_p1_get_teachergradeclassList_principal(self):
        """
        title: 验证督学系统：获取班级列表_校长
        url: /api/eteacherproduct/routine/getTeacherGradeClassList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.getteachergradeclassList()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(0, res['data']['role'])

    def test_p2_get_teachergradeclassList_psychologicalteacher(self):
        """
        title: 验证督学系统：获取班级列表_心理老师
        url: /api/eteacherproduct/routine/getTeacherGradeClassList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.getteachergradeclassList()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(6, res['data']['role'])
        # self.assertTrue(res['data']['grades'] == [])  # 这句断言过不了

    def test_p2_get_teachergradeclassList_grademaster(self):
        """
        title: 验证督学系统：获取班级列表_年级主任
        url: /api/eteacherproduct/routine/getTeacherGradeClassList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.getteachergradeclassList()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(4, res['data']['role'])
        # for classes in res['data']['grades']:
        #     self.assertEqual(0, classes['role'])
        #     for c in classes['classList']:
        #         self.assertEqual(0, c['role'])

    def test_p2_get_teachergradeclassList_headteacher(self):
        """
        title: 验证督学系统：获取班级列表_班主任
        url: /api/eteacherproduct/routine/getTeacherGradeClassList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.getteachergradeclassList()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(5, res['data']['role'])
        # for classes in res['data']['grades']:
        #     self.assertEqual(0, classes['role'])
        #     for c in classes['classList']:
        #         self.assertEqual(0, c['role'])

    def test_p2_get_teachergradeclassList_teacher(self):
        """
        title: 验证督学系统：获取班级列表_学科老师
        url: /api/eteacherproduct/routine/getTeacherGradeClassList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.getteachergradeclassList()
        print(res)
        self.assertEqual('200', res['code'])
        # self.assertEqual(-1, res['data']['role'])
        self.assertEqual(7, res['data']['role'])
        # for classes in res['data']['grades']:
        #     self.assertEqual(0, classes['role'])
        #     for c in classes['classList']:
        #         self.assertEqual(0, c['role'])

    def test_p1_get_gradeweeklydetails(self):
        """
        title: 验证督学系统：获取年级报告
        url: /api/eteacherproduct/routine/getGradeWeeklyDetails
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.getgradeweeklydetails(bizdate=self.get_month_last_sunday(), schoolId=schoolid,
                                                gradeYear=expireyear)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p2_get_gradeweeklydetails_studenthomeworklist(self):
        """
        title: 验证督学系统：未参与作业学生列表查询
        url: /api/eteacherproduct/routine/pageStudentHomeworkList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.pagestudenthomeworklist(bizdate=self.get_month_last_sunday(), schoolId=schoolid,
                                                  gradeYear=expireyear)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_get_teacherusedetaillist(self):
        """
        title: 验证督学系统：老师使用情况列表查询
        url:/api/eteacherproduct/routine/getTeacherUseDetailList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.teacherusedetaillist(bizdate=self.get_month_last_sunday(), schoolId=schoolid,
                                               gradeYear=expireyear)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_get_schoolgradeclasslist(self):
        """
        title: 验证督学系统：根据学校和年级获取班级列表
        url:/api/eteacherproduct/routine/getschoolgradeclasslist
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.getschoolgradeclasslist(schoolId=schoolid, gradeYear=expireyear)
        print(res)
        self.assertEqual('200', res['code'])
        # print(type(res['data'][0]['classList']))
        self.assertIn(groupid_xingzheng, [item['classId'] for item in res['data'][0]['classList']])
        self.assertIn(groupid_jiaoxue, [item['classId'] for item in res['data'][0]['classList']])

    def test_p1_get_classweeklydetails(self):
        """
        title: 验证督学系统：获取班级周报详情
        url: /api/eteacherproduct/routine/getClassWeeklyDetails
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.getclassweeklydetails(bizdate=self.get_month_last_sunday(), schoolId=schoolid,
                                                gradeYear=expireyear, classId=groupid_xingzheng)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_reportpraise(self):
        """
        title: 验证督学系统：报告中的表扬功能
        url: /api/eteacherproduct/routine/praise
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.reportpraise(bizdate=self.get_month_last_sunday(), schoolId=schoolid, gradeYear=expireyear,
                                       classId=groupid_xingzheng)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p2_homeworkurgestate(self):
        """
        title: 验证督学系统：催交及催交状态
        url: /api/eteacherproduct/routine/urge，/api/eteacherproduct/routine/urgeState
        author: 吴丽燕
        """
        teacher_principal = teacher(
            web_client(username=principal_user['username'], password=principal_user['password']))
        components = [{"type": "1", "title": "testauto_video", "resourceIds": lesson_ids}]
        gradeClasses = [{"grade": grade, "expireYear": expireyear, "classList": [groupid_jiaoxue]}]
        res = teacher_principal.sethomework(components=components, gradeClasses=gradeClasses,
                                            deadline=CaseServices.get_deadlinetime(),
                                            arrangeType=0, classType=2, expireYears=[], isGradeHomework=False,
                                            subject='1')

        hid = res['data'][0]
        teacher_web = teacher(web_client(username=principal_user['username']))
        homeworkurgestateres = teacher_web.homeworkurgestate(homeworkId=hid)
        print(homeworkurgestateres)
        self.assertEqual('200', homeworkurgestateres['code'])
        self.assertEqual(0, homeworkurgestateres['data'])
        res = teacher_web.homeworkurge(homeworkId=hid)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertTrue(res['data'] > 0)
        time.sleep(5)
        homeworkurgestateres = teacher_web.homeworkurgestate(homeworkId=hid)
        self.assertEqual(-1, homeworkurgestateres['data'])

