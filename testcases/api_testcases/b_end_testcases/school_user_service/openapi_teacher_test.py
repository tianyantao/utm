from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class OpenAPiTeacher(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_teacher_queryHeadTeacherByClassId(self):
        """
        title: 根据班级id获取班主任id_行政班
        url: /schooluserservice/teacher/queryHeadTeacherByClassId
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.teacher_queryHeadTeacherByClassId(classId=groupid_xingzheng)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(teacher_web.client.user_id), res['data'])

    def test_p1_2_teacher_queryHeadTeacherByClassId(self):
        """
        title: 根据班级id获取班主任id_教学班
        url: /schooluserservice/teacher/queryHeadTeacherByClassId
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.teacher_queryHeadTeacherByClassId(classId=groupid_jiaoxue)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(teacher_web.client.user_id), res['data'])

    def test_p1_teacher_queryHeadTeacherByClassIdList(self):
        """
        title: 批量根据班级id列表获取班主任id
        url: /schooluserservice/teacher/queryHeadTeacherByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        teacher_web2 = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.teacher_queryHeadTeacherByClassIdList(classIdList=[groupid_jiaoxue, groupid_xingzheng])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(2, len(res['data']))
        self.assertEqual(str(teacher_web.client.user_id), res['data'][str(groupid_jiaoxue)])
        self.assertEqual(str(teacher_web2.client.user_id), res['data'][str(groupid_xingzheng)])

    def test_p1_1_teacher_getTeachInfoListBySchoolAndClass(self):
        """
        title: 根据学校ID和班级ID查询老师教授班级信息列表_行政班,（teacherRole教授角色属性（班主任=0,语文=1）;）
        url: /schooluserservice/teacher/getTeachInfoListBySchoolAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        teacher_web2 = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.teacher_getTeachInfoListBySchoolAndClass(schoolId=schoolid, classId=groupid_xingzheng)
        print(res)
        self.assertEqual("200", res['code'])
        teacherRoles = {str(i['teacherRole']):i['userId'] for i in res['data']}
        self.assertEqual(str(teacher_web.client.user_id), teacherRoles['0'])
        self.assertEqual(str(teacher_web2.client.user_id), teacherRoles['1'])

    def test_p1_2_teacher_getTeachInfoListBySchoolAndClass(self):
        """
        title: 根据学校ID和班级ID查询老师教授班级信息列表_教学班,（teacherRole教授角色属性（教学班班主任=200））
        url: /schooluserservice/teacher/getTeachInfoListBySchoolAndClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.teacher_getTeachInfoListBySchoolAndClass(schoolId=schoolid, classId=groupid_jiaoxue)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(200, res['data'][0]['teacherRole'])
        self.assertEqual(str(teacher_web.client.user_id), res['data'][0]['userId'])
        self.assertEqual(1, res['data'][0]['teachSubjectId'])
