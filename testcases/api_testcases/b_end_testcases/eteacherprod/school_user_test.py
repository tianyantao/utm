from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import TeacherOaClient
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class SchoolUser(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_getschooluserinfo_by_principal(self):
        """
        title: 校长角色获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p1_getschooluserinfo_by_grademaster(self):
        """
        title: 年级主任角色获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p1_getschooluserinfo_by_headteacher(self):
        """
        title: 行政班班主任角色获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p1_getschooluserinfo_by_classheadteacher(self):
        """
        title: 教学班班主任角色获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p1_getschooluserinfo_by_psychologicalteacher(self):
        """
        title: 心理老师角色获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(1, res['data']['userCategory'])

    def test_p3_getschooluserinfo_by_student(self):
        """
        title: 学生账号获取学校信息
        url: /api/eteacherproduct/school/getSchoolUserInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.getSchoolUserInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual(2, res['data']['userCategory'])

    def test_p1_queryCurrentSchoolConf_by_teacher(self):
        """
        title: 老师获取学校配置
        url: /api/eteacherproduct/school/queryCurrentSchoolConf
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_web.queryCurrentSchoolConf()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 4)
        self.assertIn({'key': 'SCHOOL_BASED_VIDEO_PERMISSION', 'value': 'true'}, res['data'])
        self.assertIn({'key': 'SCHOOL_BASED_PAPERS_PERMISSION', 'value': 'true'}, res['data'])


    def test_p1_queryTeacherRoleAndSchoolInfo_by_principal(self):
        """
        title: 校长角色获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([1], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_grademaster(self):
        """
        title: 年级主任角色获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([2], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_headteacher(self):
        """
        title: 行政班班主任角色获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([6], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_classheadteacher(self):
        """
        title: 教学班班主任角色获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([4], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_psychologicalteacher(self):
        """
        title: 心理老师获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([5], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_teacher(self):
        """
        title: 任课老师获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([7], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_normalteacher(self):
        """
        title: 无角色老师获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=normalteacher_user['username'], password=normalteacher_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])

    def test_p1_queryTeacherRoleAndSchoolInfo_by_mixteacher(self):
        """
        title: 多角色老师获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username'], password=teacher_mix_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertTrue(len(res['data']['roleList']) > 1)
        self.assertTrue(res['data']['userName'])

    def test_p3_queryTeacherRoleAndSchoolInfo_by_student(self):
        """
        title: 学生账号获取角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.queryTeacherRoleAndSchoolInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertEqual([], res['data']['roleList'])
        self.assertTrue(res['data']['userName'])




class MenuInfo(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_menu_info_principal(self):
        """
        title: 验证校长的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)
        self.assertIn('数据报告', menu_names)
        self.assertIn('班级管理', menu_names)
        self.assertIn('老师管理', menu_names)

    def test_p1_menu_info_grademaster(self):
        """
        title: 验证年级主任的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)
        self.assertIn('数据报告', menu_names)
        self.assertIn('班级管理', menu_names)
        self.assertIn('老师管理', menu_names)

    def test_p1_menu_info_headteacher(self):
        """
        title: 验证行政班班主任的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)
        self.assertIn('数据报告', menu_names)
        self.assertIn('班级管理', menu_names)
        self.assertNotIn('老师管理', menu_names)

    def test_p1_menu_info_classheadteacher(self):
        """
        title: 验证教学班班主任的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)
        self.assertNotIn('数据报告', menu_names)
        self.assertIn('班级管理', menu_names)
        self.assertNotIn('老师管理', menu_names)

    def test_p1_menu_info_teacher(self):
        """
        title: 验证学科老师的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)
        self.assertNotIn('数据报告', menu_names)
        self.assertIn('班级管理', menu_names)
        self.assertNotIn('老师管理', menu_names)

    def test_p1_menu_info_normalteacher(self):
        """
        title: 验证无角色老师的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=normalteacher_user['username'], password=normalteacher_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)

    def test_p1_menu_info_teacher_mix(self):
        """
        title: 验证混合角色老师的左侧菜单栏
        url: /api/eteacherproduct/teacher/manage/queryMenuInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username'], password=teacher_mix_user['password']))
        res = teacher_web.queryMenuInfo(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        menu_names = [i['menuName'] for i in res['data']]
        self.assertTrue(len(menu_names) > 0)


class OaManage(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        cls.oa = teacher(TeacherOaClient(schoolid=schoolid))

    @classmethod
    def tearDownClass(cls):
        pass

    def test_oa_querySchoolInfo(self):
        """
        title: oa认证后获取学校信息
        url: /api/eteacherproduct/oa/schoolManage/querySchoolInfo, /api/eteacherproduct/oa/auth
        author: 田彦涛
        """
        res = self.oa.querySchoolInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['id'])
        self.assertTrue(res['data']['areaName'])
        self.assertTrue(res['data']['cityName'])
        self.assertTrue(res['data']['provinceName'])
        self.assertTrue(res['data']['classCount'])
        self.assertTrue(res['data']['studentCount'])
        self.assertTrue(res['data']['teacherCount'])
        self.assertTrue(res['data']['name'])
        self.assertTrue(res['success'])