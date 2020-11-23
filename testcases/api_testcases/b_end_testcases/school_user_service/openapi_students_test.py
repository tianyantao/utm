from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class OpenAPiStudent(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_students_getJoinClassList(self):
        """
        title: 根据学生id获取其当前所在班级信息(不包含已删除班级)_加入班级的学生
        url: /schooluserservice/students/getJoinClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username']))
        res = teacher_web.students_getJoinClassList(schoolId=schoolid, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIn(str(groupid_xingzheng), str(res['data']))
        self.assertIn(str(groupid_jiaoxue), str(res['data']))
        for i in res['data']:
            self.assertEqual(str(schoolid), i['schoolId'])
            if  str(groupid_xingzheng) == i['classId']:
                self.assertEqual(expireyear, i['graduationYear'])
                self.assertTrue(i['numberOfStudent'] > 4)
                self.assertEqual(0, i['subjectId'])
                self.assertFalse(i['disbanded'])
            if  str(groupid_jiaoxue) == i['classId']:
                self.assertEqual(expireyear, i['graduationYear'])
                self.assertTrue(i['numberOfStudent'] > 4)
                self.assertEqual(1, i['subjectId'])
                self.assertFalse(i['disbanded'])

    def test_p1_2_students_getJoinClassList(self):
        """
        title: 根据学生id获取其当前所在班级信息(不包含已删除班级)_退出班级的学生
        url: /schooluserservice/students/getJoinClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username']))
        res = teacher_web.students_getJoinClassList(schoolId=schoolid, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    def test_p1_3_students_getJoinClassList(self):
        """
        title: 根据学生id获取其当前所在班级信息(不包含已删除班级)_老师的账号
        url: /schooluserservice/students/getJoinClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.students_getJoinClassList(schoolId=schoolid, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    def test_p1_1_students_getAdminClassInfoByUserIdList(self):
        """
        title: 批量学生id获取其当前所在班级信息（仅行政班）_加班的学生
        url: /schooluserservice/students/getAdminClassInfoByUserIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.students_getAdminClassInfoByUserIdList(schoolId=schoolid, userIdList=[teacher_web.client.user_id])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, len(res['data']))
        for i in res['data']:
            self.assertEqual(str(schoolid), i['schoolId'])
            self.assertEqual(str(groupid_xingzheng), i['classId'])
            self.assertEqual(expireyear, i['graduationYear'])
            self.assertEqual(1, i['classType'])
            self.assertEqual(0, i['subjectId'])
            self.assertEqual('N', i['isLeft'])

    def test_p1_2_students_getAdminClassInfoByUserIdList(self):
        """
        title: 批量学生id获取其当前所在班级信息（仅行政班）_退出班级的学生
        url: /schooluserservice/students/getAdminClassInfoByUserIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username'], password=student200_user['password']))
        res = teacher_web.students_getAdminClassInfoByUserIdList(schoolId=schoolid, userIdList=[teacher_web.client.user_id])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    # def test_p1_students_deleteStudent(self):
    #     """
    #     title: 删除学生信息（单个）
    #     url: /schooluserservice/students/deleteStudent
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user))
    #     res = teacher_web.students_deleteStudent(schoolId=schoolid, userId='112010230')
    #     print(res)
    #     self.assertEqual("200", res['code'])