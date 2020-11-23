from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.eteacherprod.teacher_manage_data import *
from common.unittest_v2 import TestCaseV2
import random


class ManageTeacherTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 校长分页查询管理教师列表
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        self.assertIn(principal_user['username'], str(res['data']))
        self.assertIn(psychologicalteacher_user['username'], str(res['data']))
        self.assertIn(headteacher_user['username'], str(res['data']))
        self.assertIn(grademaster_user['username'], str(res['data']))
        self.assertIn(teacher_user['username'], str(res['data']))
        self.assertIn(classheadteacher_user['username'], str(res['data']))
        self.assertIn(teacher_mix_user['username'], str(res['data']))
        self.assertNotIn(normalteacher_user['username'], str(res['data']))
        for i in res['data']:
            if i['cellphone'] == cellphone:
                self.assertEqual("校领导", i['roleAliasName'])
                self.assertEqual("全部年级全部班级", i['manageClassesName'])
                self.assertEqual(teacher_web.client.user_id, i['userId'])
            if i['cellphone'] == psychologicalteacher_user['username']:
                self.assertEqual("心理老师", i['roleAliasName'])
                self.assertEqual("全部年级全部班级", i['manageClassesName'])
            if i['cellphone'] == headteacher_user['username']:
                self.assertEqual("班主任", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_xingzheng, expireyear - 3), i['manageClassesName'])
            if i['cellphone'] == classheadteacher_user['username']:
                self.assertEqual("教学班主任", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_jiaoxue, expireyear - 3), i['manageClassesName'])
            if i['cellphone'] == teacher_user['username']:
                self.assertEqual("任课老师", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_xingzheng, expireyear - 3), i['teachClassesName'])
            if i['cellphone'] == grademaster_user['username']:
                self.assertEqual("年级主任", i['roleAliasName'])
                self.assertEqual("{0}全部班级({1}年入学)".format(gradename, expireyear - 3), i['manageClassesName'])

    def test_p1_2_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 年级主任分页查询管理教师列表
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        self.assertIn(principal_user['username'], str(res['data']))
        self.assertIn(psychologicalteacher_user['username'], str(res['data']))
        self.assertIn(headteacher_user['username'], str(res['data']))
        self.assertIn(grademaster_user['username'], str(res['data']))
        self.assertIn(teacher_user['username'], str(res['data']))
        self.assertIn(classheadteacher_user['username'], str(res['data']))
        self.assertIn(teacher_mix_user['username'], str(res['data']))
        self.assertNotIn(normalteacher_user['username'], str(res['data']))
        for i in res['data']:
            if i['cellphone'] == cellphone:
                self.assertEqual("校领导", i['roleAliasName'])
                self.assertEqual("全部年级全部班级", i['manageClassesName'])
            if i['cellphone'] == psychologicalteacher_user['username']:
                self.assertEqual("心理老师", i['roleAliasName'])
                self.assertEqual("全部年级全部班级", i['manageClassesName'])
            if i['cellphone'] == headteacher_user['username']:
                self.assertEqual("班主任", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_xingzheng, expireyear - 3), i['manageClassesName'])
            if i['cellphone'] == classheadteacher_user['username']:
                self.assertEqual("教学班主任", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_jiaoxue, expireyear - 3), i['manageClassesName'])
            if i['cellphone'] == teacher_user['username']:
                self.assertEqual("任课老师", i['roleAliasName'])
                self.assertEqual("{0}({1})".format(group_name_xingzheng, expireyear - 3), i['teachClassesName'])
            if i['cellphone'] == grademaster_user['username']:
                self.assertEqual("年级主任", i['roleAliasName'])
                self.assertEqual("{0}全部班级({1}年入学)".format(gradename, expireyear - 3), i['manageClassesName'])
                self.assertEqual(teacher_web.client.user_id, i['userId'])

    def test_p1_3_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 行政班主任没有分页查询管理教师列表的权限
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertTrue("用户无权限", res['msg'])

    def test_p1_4_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 学科老师没有分页查询管理教师列表的权限
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertTrue("用户无权限", res['msg'])

    def test_p1_5_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 无角色老师没有分页查询管理教师列表的权限
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=normalteacher_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertTrue("用户无权限", res['msg'])

    def test_p1_6_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 教学班班主任账号无角色老师没有分页查询管理教师列表的权限
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertTrue("用户无权限", res['msg'])

    def test_p1_7_manageteacher_pagerQueryTeacherInfo(self):
        """
        title: 心理老师账号无角色老师没有分页查询管理教师列表的权限
        url: /api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.manageteacher_pagerQueryTeacherInfo(schoolId=schoolid, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertTrue("用户无权限", res['msg'])

    def test_p1_1_manageteacher_verifyCellphone(self):
        """
        title: 手机号验证,已是老师账号
        url: /api/eteacherproduct/teacher/manage/verifyCellphone
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_verifyCellphone(schoolId=schoolid, cellphone=normalteacher_user['username'])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(normalteacher_user['username'], res['data']['cellphone'])

    def test_p1_2_manageteacher_verifyCellphone(self):
        """
        title: 手机号验证,未注册老师账号
        url: /api/eteacherproduct/teacher/manage/verifyCellphone
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_verifyCellphone(schoolId=schoolid, cellphone='19876543210')
        print(res)
        self.assertEqual("022601", res['code'])
        self.assertEqual("老师信息不存在", res['msg'])

    def test_p1_manageteacher_addTeacher(self):
        """
        title: web教师管理_先删除老师; 再新增老师; 新增老师后 校验该手机号已注册
        url: /api/eteacherproduct/teacher/manage/removeTeacher,/api/eteacherproduct/teacher/manage/addTeacher,/api/eteacherproduct/teacher/manage/removeTeacher
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        teacher_web2 = teacher(web_client(username=teacher_mix_user['username']))
        res2 = teacher_web.manageteacher_removeTeacher(schoolId=schoolid, userId=teacher_web2.client.user_id)
        print(res2)
        self.assertEqual("200", res2['code'])
        rolelist = [{"role": 1}, {"role": 2, "manageYear": [expireyear]}, {"role": 5},
                    {"role": 7, "teachInfo": [{"teachSubjectId": 6, "teachClass": [groupid_xingzheng]}]}]
        res = teacher_web.manageteacher_addTeacher(schoolId=schoolid, cellphone=teacher_mix_user['username'],
                                                   userId=teacher_web2.client.user_id, teacherName="test",
                                                   roleList=rolelist)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        res3 = teacher_web.manageteacher_verifyCellphone(schoolId=schoolid, cellphone=teacher_mix_user['username'])
        print(res3)
        self.assertEqual("022603", res3['code'])
        self.assertEqual("教师身份已添加", res3['msg'])

    def test_p1_1_manageteacher_listRole(self):
        """
        title: web教师端获取包含全部的职务列表， needAll = 0
        url: /api/eteacherproduct/teacher/manage/listRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listRole(needAll=0)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(rolelistNotALL, res['data'])

    def test_p1_2_manageteacher_listRole(self):
        """
        title: web教师端获取不包含全部的职务列表，needAll = 1
        url: /api/eteacherproduct/teacher/manage/listRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listRole(needAll=1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(rolelistNeedALL, res['data'])

    def test_p1_1_manageteacher_listTeachSubject(self):
        """
        title: web教师端教师科目列表(9大科目), 包含全部needAll = 0
        url: /api/eteacherproduct/teacher/manage/listTeachSubject
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listTeachSubject(needAll=0)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(subjectlistNotAll, res['data'])

    def test_p1_2_manageteacher_listTeachSubject(self):
        """
        title: web教师端教师科目列表(9大科目), 不包含全部needAll = 0
        url: /api/eteacherproduct/teacher/manage/listTeachSubject
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listTeachSubject(needAll=1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(subjectlistNeedAll, res['data'])

    def test_p1_manageteacher_updateTeacher(self):
        """
        title: 编辑教师；获取老师信息，验证编辑老师职务信息成功
        url: /api/eteacherproduct/teacher/manage/updateTeacher,/api/eteacherproduct/teacher/manage/queryTeacherRoleInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        teacher_web1 = teacher(web_client(username=teacher_mix_user['username']))
        rolelist = [{"role": 1, "roleName": "校领导", "roleAliasName": "校领导"},
                    {"role": 7, "roleName": "任课老师", "roleAliasName": "任课老师",
                     "teachInfo": [{"teachSubjectId": 6, "teachClass": [groupid_xingzheng]}]}]
        res = teacher_web.manageteacher_updateTeacher(schoolId=schoolid, cellphone=teacher_mix_user['username'],
                                                      userId=teacher_web1.client.user_id,
                                                      teacherName="test", roleList=rolelist)
        print(res)
        self.assertEqual("200", res['code'])

        res3 = teacher_web.manageteacher_queryTeacherRoleInfo(schoolId=schoolid, userId=teacher_web1.client.user_id)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertEqual(1, res3['data'][0]['role'])
        self.assertEqual(7, res3['data'][1]['role'])

    # 以下用例与school_user_test里面的用例重复了
    # def test_p1_1_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取 校领导 对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[0], len(res['data']))
    #
    # def test_p1_2_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取心理老师对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[1], len(res['data']))
    #
    # def test_p1_3_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取行政班主任对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=headteacher_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[2], len(res['data']))
    #
    # def test_p1_4_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取年级主任对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=grademaster_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[3], len(res['data']))
    #
    # def test_p1_5_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取学科老师账号对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=teacher_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[4], len(res['data']))
    #
    # def test_p1_6_manageteacher_queryMenuInfo(self):
    #     """
    #     title: 获取无角色老师对应的菜单信息
    #     url: /api/eteacherproduct/teacher/manage/queryMenuInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=normalteacher_user['username']))
    #     res = teacher_web.manageteacher_queryMenuInfo()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(menuNum[5], len(res['data']))

    def test_p1_manageteacher_queryTeacherGradeClassRole(self):
        """
        title: 获取老师年级班级教授角色信息
        url: /api/eteacherproduct/teacher/manage/queryTeacherGradeClassRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_queryTeacherGradeClassRole(schoolId=schoolid, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(4, len(res['data']))
        for i in res['data']:
            self.assertTrue(len(i['teacherClassRoleInfo']) > 0)
            for j in i['teacherClassRoleInfo']:
                self.assertEqual(i['gradeYear'], j['gradeYear'])
                self.assertTrue(j['classId'] > 1)
                self.assertTrue(len(j['className']) > 0)

    def test_p1_1_manageteacher_joinExecutiveClass(self):
        """
        title: 老师加入行政班主任;获取用户的在班级的职务信息
        url: /api/eteacherproduct/teacher/manage/joinExecutiveClass,/api/eteacherproduct/teacher/manage/getClassTeacherRole, /api/eteacherproduct/teacher/manage/removeTeacherClassRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.manageteacher_removeTeacherClassRole(userId=teacher_web.client.user_id, schoolId=schoolid,
                                                               classId=groupid_xingzheng, role=0)
        print(res)
        self.assertEqual("200", res['code'])
        res = teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                           classId=groupid_xingzheng, role=["0"])
        print(res)
        self.assertEqual("200", res['code'])
        res2 = teacher_web.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                             classId=groupid_xingzheng, schoolId=schoolid)
        print(res2)
        self.assertEqual("200", res2['code'])
        self.assertTrue(res2['data'][0]['ownerTeach'])
        self.assertIsNotNone(res2['data'][0]['teachTeacherName'])

    def test_p1_2_manageteacher_joinExecutiveClass(self):
        """
        title: 老师加入行政语文任课老师;获取班级的职务信息
        url: /api/eteacherproduct/teacher/manage/joinExecutiveClass,/api/eteacherproduct/teacher/manage/getClassTeacherRole, /api/eteacherproduct/teacher/manage/removeTeacherClassRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.manageteacher_removeTeacherClassRole(userId=teacher_web.client.user_id, schoolId=schoolid,
                                                               classId=groupid_xingzheng, role=1)
        print(res)
        self.assertEqual("200", res['code'])
        res = teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                           classId=groupid_xingzheng, role=["1"])
        print(res)
        self.assertEqual("200", res['code'])
        res2 = teacher_web.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                             classId=groupid_xingzheng, schoolId=schoolid)
        print(res2)
        self.assertEqual("200", res2['code'])
        self.assertTrue(res2['data'][1]['ownerTeach'])
        self.assertIsNotNone(res2['data'][1]['teachTeacherName'])

    def test_p1_1_manageteacher_listGrades(self):
        """
        title: 获取有效年级列表,校验新高一是否展示（ 0：直接全部展示）(Boolean)
        url: /api/eteacherproduct/teacher/manage/listGrades
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listGrades(checkEarlyRise=0)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(4, len(res['data']))

    def test_p1_2_manageteacher_listGrades(self):
        """
        title: 获取有效年级列表,　校验新高一是否展示（ 1：读配置）(Boolean)
        url: /api/eteacherproduct/teacher/manage/listGrades
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_listGrades(checkEarlyRise=1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 3)

    def test_p1_manageteacher_getClassTeacherRole(self):
        """
        title: 老师1加入行政数学老师;切换成老师2获取班级的职务信息，然后用户A 辞去数学任课老师职务
        url: /api/eteacherproduct/teacher/manage/joinExecutiveClass,/api/eteacherproduct/teacher/manage/getClassTeacherRole, /api/eteacherproduct/teacher/manage/removeTeacherClassRole
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        teacher_web1 = teacher(web_client(username=principal_user['username']))
        teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                     classId=groupid_xingzheng, role=[])
        res1 = teacher_web1.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                              classId=groupid_xingzheng, schoolId=schoolid)
        self.assertFalse(res1['data'][2]['otherTeach'])
        self.assertFalse(res1['data'][2]['ownerTeach'])
        self.assertIsNone(res1['data'][2]['teachTeacherName'])
        res = teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                           classId=groupid_xingzheng, role=["2"])
        print(res)
        self.assertEqual("200", res['code'])

        res2 = teacher_web1.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                              classId=groupid_xingzheng, schoolId=schoolid)
        print(res2)
        self.assertTrue(res2['data'][2]['otherTeach'])
        self.assertIsNotNone(res2['data'][2]['teachTeacherName'])
        res3 = teacher_web.manageteacher_removeTeacherClassRole(userId=teacher_web.client.user_id, schoolId=schoolid,
                                                                classId=groupid_xingzheng, role=2)
        print(res3)
        self.assertEqual("200", res3['code'])

    def test_p1_0_manageteacher_joinExecutiveClass(self):
        """
        title: 老师加入行政班，选择职务空，点击确定
        url: /api/eteacherproduct/teacher/manage/joinExecutiveClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        res = teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                           classId=groupid_xingzheng, role=["7", "8"])
        self.assertEqual("200", res['code'])
        res2 = teacher_web.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                             classId=groupid_xingzheng,
                                                             schoolId=schoolid)
        print(res2)
        self.assertTrue(len(res2['data']) > 0)
        self.assertTrue(res2['data'][7]['ownerTeach'])
        self.assertTrue(res2['data'][8]['ownerTeach'])
        res = teacher_web.manageteacher_joinExecutiveClass(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                           classId=groupid_xingzheng, role=[])
        print(res)
        self.assertEqual("200", res['code'])
        res2 = teacher_web.manageteacher_getClassTeacherRole(userId=teacher_web.client.user_id,
                                                             classId=groupid_xingzheng,
                                                             schoolId=schoolid)
        print(res2)
        self.assertTrue(len(res2['data']) > 0)
        for i in res2['data']:
            self.assertFalse(i['ownerTeach'])

    def test_p1_1_manageteacher_updateStudentName(self):
        """
        title: 班主任老师帮学生改名
        url: /api/eteacherproduct/teacher/manage/updateStudentName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        studentInfo = self.getstudentinfo(teacher_web, groupid_xingzheng)
        student_name = 'test{}'.format(random.randint(1000, 9999))
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_xingzheng, studentId=studentInfo[0],
                                                          name=student_name, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        studentInfo2 = self.getstudentinfo(teacher_web, groupid_xingzheng)
        self.assertEqual(student_name, studentInfo2[1])
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_xingzheng, studentId=studentInfo[0],
                                                          name=studentInfo[1], schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_2_manageteacher_updateStudentName(self):
        """
        title: 任课老师帮学生改名
        url: /api/eteacherproduct/teacher/manage/updateStudentName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        studentInfo = self.getstudentinfo(teacher_web, groupid_xingzheng)
        student_name = 'test{}'.format(random.randint(1000, 9999))
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_xingzheng, studentId=studentInfo[0],
                                                          name=student_name, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        studentInfo2 = self.getstudentinfo(teacher_web, groupid_xingzheng)
        self.assertEqual(student_name, studentInfo2[1])
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_xingzheng, studentId=studentInfo[0],
                                                          name=studentInfo[1], schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_3_manageteacher_updateStudentName(self):
        """
        title: 教学班主任帮学生改名
        url: /api/eteacherproduct/teacher/manage/updateStudentName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        studentInfo = self.getstudentinfo(teacher_web, groupid_jiaoxue)
        student_name = 'test{}'.format(random.randint(1000, 9999))
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_jiaoxue, studentId=studentInfo[0],
                                                          name=student_name, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        studentInfo2 = self.getstudentinfo(teacher_web, groupid_jiaoxue)
        self.assertEqual(student_name, studentInfo2[1])
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_jiaoxue, studentId=studentInfo[0],
                                                          name=studentInfo[1], schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_4_manageteacher_updateStudentName(self):
        """
        title: 非班主任/任课老师无权限帮学生改名
        url: /api/eteacherproduct/teacher/manage/updateStudentName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        studentInfo = self.getstudentinfo(teacher_web, groupid_jiaoxue)
        res = teacher_web.manageteacher_updateStudentName(classId=groupid_jiaoxue, studentId=studentInfo[0],
                                                          name="test", schoolId=schoolid)
        print(res)
        self.assertEqual("022417", res['code'])
        self.assertEqual("用户无权限", res['msg'])

    def getstudentinfo(self, teacher_web, classId):
        res = teacher_web.classesManager_listClassStudent(schoolId=schoolid, classId=classId, keyword="", pageIndex=1,
                                                          pageSize=20, sort=1)
        for i in res['data']:
            if i['realName'] != "":
                return [i['userId'], i['realName']]

    # 与school_user_test用例重复
    # def test_p1_1_manageteacher_queryTeacherRoleAndSchoolInfo(self):
    #     """
    #     title: 获取校长的用户信息和学校信息
    #     url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     userId = teacher_web.client.user_id
    #     res = teacher_web.manageteacher_queryTeacherRoleAndSchoolInfo(userId=userId)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(schoolid, res['data']['schoolId'])
    #     self.assertEqual(userId, res['data']['userId'])
    #     self.assertEqual(1, res['data']['roleList'][0])
    #
    # def test_p1_2_manageteacher_queryTeacherRoleAndSchoolInfo(self):
    #     """
    #     title: 获取无权限老师的用户信息和学校信息
    #     url: /api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=normalteacher_user['username']))
    #     userId = teacher_web.client.user_id
    #     res = teacher_web.manageteacher_queryTeacherRoleAndSchoolInfo(userId=userId)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(schoolid, res['data']['schoolId'])
    #     self.assertEqual(userId, res['data']['userId'])
    #     self.assertEqual([], res['data']['roleList'])

    # def test_p1_1_manageteacher_getSchoolUserInfo(self):
    #     """
    #     title: 校长登录，获取学校信息（不区分学生还是老师）
    #     url: /api/eteacherproduct/school/getSchoolUserInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     res = teacher_web.manageteacher_getSchoolUserInfo()
    #     print(res)
    #     self.assertEqual(1, res['data']['userCategory'])
    #     self.assertEqual(teacher_web.client.user_id, res['data']['userId'])
    #     self.assertEqual(schoolid, res['data']['schoolId'])
    #
    # def test_p1_2_manageteacher_getSchoolUserInfo(self):
    #     """
    #     title: 学生登录，获取学校信息（不区分学生还是老师）
    #     url: /api/eteacherproduct/school/getSchoolUserInfo
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=student02_user['username']))
    #     res = teacher_web.manageteacher_getSchoolUserInfo()
    #     print(res)
    #     self.assertEqual(2, res['data']['userCategory'])
    #     self.assertEqual(teacher_web.client.user_id, res['data']['userId'])
    #     self.assertEqual(schoolid, res['data']['schoolId'])

    def test_p1_manageteacher_updateUserName(self):
        """
        title: 修改姓名
        url: /api/eteacherproduct/teacher/manage/updateUserName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        userId = teacher_web.client.user_id
        real_name = 'test{}'.format(random.randint(1000, 9999))
        res = teacher_web.manageteacher_updateUserName(userId=userId, name=real_name)
        self.assertEqual("200", res['code'])
        res2 = teacher_web.manageteacher_queryTeacherRoleAndSchoolInfo(userId=userId)
        print(res2)
        self.assertEqual("200", res['code'])
        self.assertEqual(real_name, res2['data']['userName'])
        res = teacher_web.manageteacher_updateUserName(userId=userId, name="test")
        self.assertEqual("200", res['code'])

    def test_p1_1_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_校长返回全部年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(4, len(res['data']))
        self.assertIn(expireyear, res['data'])

    def test_p1_2_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_心理老师返回全部年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(4, len(res['data']))
        self.assertIn(expireyear, res['data'])

    def test_p1_3_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_年级主任返回相应管理年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIn(expireyear, res['data'])

    def test_p1_4_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_行政班主任主任返回相应管理年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIn(expireyear, res['data'])

    def test_p1_5_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_任课老师无管理年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    def test_p1_6_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_教学班主任无管理年级
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    def test_p1_7_manageteacher_teacherGradeList(self):
        """
        title: 获取用户权限范围内的年级列表_混合角色
        url: /api/eteacherproduct/teacher/manage/teacherGradeList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.manageteacher_teacherGradeList(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    # 与school_user_test用例重复
    # def test_p1_manageteacher_queryCurrentSchoolConf(self):
    #     """
    #     title: 获取当前用户学校配置信息
    #     url: /api/eteacherproduct/school/queryCurrentSchoolConf
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     res = teacher_web.manageteacher_queryCurrentSchoolConf()
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(schoolconf, res['data'])
