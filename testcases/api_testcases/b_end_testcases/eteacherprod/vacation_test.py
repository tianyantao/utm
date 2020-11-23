from testcases.api_testcases.b_end_testcases.eteacherprod.plan_homework_data import *
from common.unittest_v2 import TestCaseV2


class ContentsTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_teacherinfo(self):
        """
        title: 获取教师用户基础信息——教师角色
        url: /api/eteacherproduct/activity/getTeacherInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        teacherinfo = teacher_web.getteacherinfo()
        print(teacherinfo)
        self.assertEqual("200", teacherinfo['code'])
        self.assertEqual(1, teacherinfo['data']['isTeacher'])
        self.assertEqual(schoolid, teacherinfo['data']['schoolId'])

    def test_p3_get_teacherinfo(self):
        """
        title: 获取教师用户基础信息——学生角色
        url: /api/eteacherproduct/activity/getTeacherInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=student02_user['username']))
        teacherinfo = teacher_web.getteacherinfo()
        print(teacherinfo)
        self.assertEqual("200", teacherinfo['code'])
        self.assertEqual(0, teacherinfo['data']['isTeacher'])

    def test_p3_get_schoolhomeworkassigncount(self):
        """
        title: 获取假期作业布置总数
        url: /api/eteacherproduct/activity/getSchoolHomeworkAssignCount
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        homeworkassigncount = teacher_web.getschoolhomeworkassigncount(actId=actId)
        print(homeworkassigncount)
        self.assertEqual("200", homeworkassigncount['code'])
        self.assertTrue(homeworkassigncount['data']['cnt'] > 0)

    def test_p3_get_gradetagAndassignInfo(self):
        """
        title: 获取当前教师的年级方案概况
        url: /api/eteacherproduct/activity/getGradeTagAndAssignInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        token = teacher_web.client.user_token
        gradetagAndassignInfo = teacher_web.getgradetagAndassignInfo(token=token, actId=actId)
        print(gradetagAndassignInfo)
        self.assertEqual("200", gradetagAndassignInfo['code'])
        self.assertTrue(len(gradetagAndassignInfo['data']) == 3)

    def test_p3_get_gradetopcategoryid(self):
        """
        title: 按活动以及年级获取level=1分类信息
        url: /api/eteacherproduct/activity/getGradeTopCategoryId
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        token = teacher_web.client.user_token
        gradetagAndassignInfo = teacher_web.getgradetopcategoryid(token=token, actId=actId)
        print(gradetagAndassignInfo)
        self.assertEqual("200", gradetagAndassignInfo['code'])
        self.assertTrue(len(gradetagAndassignInfo['data']) > 0)
