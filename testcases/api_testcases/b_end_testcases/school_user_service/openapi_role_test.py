from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.zzj_testcases_data import *
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class OpenAPiRole(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_校长
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['principal_user'], roles)

    def test_p1_2_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_心理老师
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['psychologicalteacher_user'], roles)

    def test_p1_3_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_行政班班主任
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['headteacher_user'], roles)

    def test_p1_4_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_仅担任expireyear所在年级的年级主任
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['grademaster_user'], roles)
        self.assertEqual([expireyear], res['data']['roleInfoList'][0]['gradeYearList'])

    def test_p1_5_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_任课老师
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['teacher_user'], roles)

    # def test_p1_6_role_getUserRoleWithGrade(self):
    #     """
    #     title: 获取用户角色（管理年级）_无角色老师
    #     url: /schooluserservice/role/getUserRoleWithGrade
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=normalteacher_user['username']))
    #     res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(str(schoolid), res['data']['schoolId'])
    #     self.assertIsNone(res['data']['roleInfoList'])

    def test_p1_7_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_教学班主任
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['classheadteacher_user'], roles)

    def test_p1_8_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_混合角色老师账号（既担任校领导，又担任多个老师角色）
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(str(res['data']['roleInfoList'])) > 1)
        self.assertEqual(str(schoolid), res['data']['schoolId'])

    def test_p1_9_role_getUserRoleWithGrade(self):
        """
        title: 获取用户角色（管理年级）_学生账号
        url: /schooluserservice/role/getUserRoleWithGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.role_getUserRoleWithGrade(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIsNone(res['data'])

    def test_p1_1_role_getUserRoleWithGradeAndTeachClass(self):
        """
        title: 获取用户角色（管理年级，教授班级）_年级主任
        url: /schooluserservice/role/getUserRoleWithGradeAndTeachClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndTeachClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([expireyear], res['data']['roleInfoList'][0]['gradeYearList'])

    def test_p1_2_role_getUserRoleWithGradeAndTeachClass(self):
        """
        title: 获取用户角色（管理年级，教授班级）_行政班班主任
        url: /schooluserservice/role/getUserRoleWithGradeAndTeachClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndTeachClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['headteacher_user'], roles)
        self.assertIn(str(groupid_xingzheng), str(res['data']))

    def test_p1_3_role_getUserRoleWithGradeAndTeachClass(self):
        """
        title: 获取用户角色（管理年级，教授班级）_任课老师
        url: /schooluserservice/role/getUserRoleWithGradeAndTeachClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndTeachClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['teacher_user'], roles)
        self.assertIn(str(groupid_xingzheng), str(res['data']))

    def test_p1_3_role_getUserRoleWithGradeAndTeachClass(self):
        """
        title: 获取用户角色（管理年级，教授班级）_教学班主任
        url: /schooluserservice/role/getUserRoleWithGradeAndTeachClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndTeachClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['classheadteacher_user'], roles)
        self.assertIn(str(groupid_jiaoxue), str(res['data']))

    def test_p1_1_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_校长，管理所有班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']['manageClassList']]
        self.assertTrue(len(list(set(graduationYears))) >= 3)
        self.assertIn(expireyear, graduationYears)
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)

    def test_p1_2_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_年级主任, 管理对应年级的班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']['manageClassList']]
        self.assertEqual([expireyear], list(set(graduationYears)))
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)

    def test_p1_3_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_班主任, 管理对应的班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertEqual([str(groupid_xingzheng)], list(set(classIds)))

    def test_p1_4_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_教学班主任, 管理对应的班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertEqual([str(groupid_jiaoxue)], list(set(classIds)))

    def test_p1_5_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_任课老师, 管理任课对应的班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertEqual([str(groupid_xingzheng)], list(set(classIds)))

    def test_p1_6_role_getUserRoleWithGradeAndClass(self):
        """
        title: 获取用户角色（管理年级，教授班级、管辖班级）（高并发业务场景）_心理老师, 管理所有的班级
        url: /schooluserservice/role/getUserRoleWithGradeAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.role_getUserRoleWithGradeAndClass(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']['manageClassList']]
        self.assertTrue(len(list(set(graduationYears))) >= 3)
        self.assertIn(expireyear, graduationYears)
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        classIds = [i['classId'] for i in res['data']['manageClassList']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)

    def test_p1_1_role_getUserRole(self):
        """
        title: 仅获取用户角色_学生无角色
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_2_role_getUserRole(self):
        """
        title: 仅获取用户角色_校长
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['principal_user'], roles)

    def test_p1_3_role_getUserRole(self):
        """
        title: 仅获取用户角色_混合角色
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['principal_user'], roles)
        self.assertTrue(len(roles) >= 2)

    def test_p1_4_role_getUserRole(self):
        """
        title: 仅获取用户角色_心理老师
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['psychologicalteacher_user'], roles)

    def test_p1_5_role_getUserRole(self):
        """
        title: 仅获取用户角色_行政班主任
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['headteacher_user'], roles)

    def test_p1_6_role_getUserRole(self):
        """
        title: 仅获取用户角色_教学班主任
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        roles = [i['role'] for i in res['data']['roleInfoList']]
        self.assertEqual(str(schoolid), res['data']['schoolId'])
        self.assertIn(role['classheadteacher_user'], roles)

    def test_p1_7_role_getUserRole(self):
        """
        title: 仅获取用户角色_学生
        url: /schooluserservice/role/getUserRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.role_getUserRole(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIsNone(res['data'])