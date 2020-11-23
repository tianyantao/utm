from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class OpenAPiSchool(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_school_listPrincipalsUid(self):
        """
        title: 获取学校领导的用户id
        url: /schooluserservice/school/listPrincipalsUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        teacher_web2 = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.school_listPrincipalsUid(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIn(str(teacher_web.client.user_id), res['data'])
        self.assertNotIn(str(teacher_web2.client.user_id), res['data'])

    def test_p1_school_batchSchoolStat(self):
        """
        title: 获取学校的教师数及学生数（批量）(包括未加班级的学生)
        url: /schooluserservice/school/batchSchoolStat
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.school_batchSchoolStat(schoolIdList=[schoolid])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'][0]['teacherCount'] > 5)
        self.assertTrue(res['data'][0]['classCount'] > 2)
        self.assertTrue(res['data'][0]['studentCount'] > 2)

    def test_p1_school_getDetailInfoAndConf(self):
        """
        title: 获取学校配置和其地区信息
        url: /schooluserservice/school/getDetailInfoAndConf
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.school_getDetailInfoAndConf(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']['configList']) >= 4)
        self.assertIn({'key': 'SCHOOL_BASED_VIDEO_PERMISSION', 'value': 'true'}, res['data']['configList'])
        self.assertIn({'key': 'SCHOOL_BASED_PAPERS_PERMISSION', 'value': 'true'}, res['data']['configList'])
        self.assertIsNotNone(res['data']['schoolName'])

    def test_p1_school_getSchoolStaffs(self):
        """
        title: 获取学校的组织结构及担任教师
        url: /schooluserservice/school/getSchoolStaffs
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.school_getSchoolStaffs(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertTrue(len(res['data']['principalList']) > 1)
        self.assertTrue(len(res['data']['psychologyTeacherList']) >= 1)
        self.assertTrue(len(res['data']['gradeYearList']) >= 3)
        self.assertIn(expireyear, [i['graduationYear'] for i in res['data']['gradeYearList']])
        for i in res['data']['gradeYearList']:
            if i['graduationYear'] == expireyear:
                self.assertTrue(len(i['gradeDirectorList']) >= 1)
                self.assertTrue(len(i['classList']) >= 1)
                for j in i['classList']:
                    if j['classId'] == groupid_xingzheng:
                        self.assertEqual(str(teacher_web.client.user_id), j['classMaster'])
                        self.assertTrue(len(i['subjectTeacherList']) >= 1)

    def test_p1_school_getConfigs(self):
        """
        title: 获取学校配置
        url: /schooluserservice/school/getConfigs
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.school_getConfigs(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 4)
        self.assertIn({'key': 'SCHOOL_BASED_VIDEO_PERMISSION', 'value': 'true'}, res['data'])
        self.assertIn({'key': 'SCHOOL_BASED_PAPERS_PERMISSION', 'value': 'true'}, res['data'])

    def test_p1_1_school_getSchoolUserInfo(self):
        """
        title: 根据用户Id获取学校信息_根据老师UserId
        url: /schooluserservice/school/getSchoolUserInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.school_getSchoolUserInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p1_2_school_getSchoolUserInfo(self):
        """
        title: 根据用户Id获取学校信息_根据已加班学生UserId
        url: /schooluserservice/school/getSchoolUserInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.school_getSchoolUserInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])

    def test_p1_3_school_getSchoolUserInfo(self):
        """
        title: 根据用户Id获取学校信息_根据未加班学生UserId，学校ID=0
        url: /schooluserservice/school/getSchoolUserInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.school_getSchoolUserInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual('0', res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])

    def test_p1_4_school_getSchoolUserInfo(self):
        """
        title: 根据用户Id获取学校信息_根据退出班级的学生，学校ID不为0
        url: /schooluserservice/school/getSchoolUserInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username'], password=student200_user['password']))
        res = teacher_web.school_getSchoolUserInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])

    def test_p1_1_school_getSchoolStudentInfo(self):
        """
        title: 根据学生Id获取学校及毕业年份信息_无学校信息的学生
        url: /schooluserservice/school/getSchoolStudentInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.school_getSchoolStudentInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual('0', res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])
        self.assertIsNone(res['data']['graduationYear'])

    def test_p1_2_school_getSchoolStudentInfo(self):
        """
        title: 根据学生Id获取学校及毕业年份信息_已加班的学生
        url: /schooluserservice/school/getSchoolStudentInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.school_getSchoolStudentInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])
        self.assertEqual(expireyear, res['data']['graduationYear'])

    def test_p1_3_school_getSchoolStudentInfo(self):
        """
        title: 根据学生Id获取学校及毕业年份信息_加班后退出的学生
        url: /schooluserservice/school/getSchoolStudentInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username'], password=student200_user['password']))
        res = teacher_web.school_getSchoolStudentInfo(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])
        self.assertEqual(expireyear, res['data']['graduationYear'])