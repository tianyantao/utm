from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from lib.api_lib.ewt_client import TeacherOaClient
from common.unittest_v2 import TestCaseV2
import time


class OpenAPiClass(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        try:
            cls.oa = teacher(TeacherOaClient(schoolid))
            time.sleep(10)
            cls.oa = teacher(TeacherOaClient(schoolid))
            time.sleep(10)
        except Exception as e:
            print(e)
        cls.oa = teacher(TeacherOaClient(schoolid))
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_class_getClassStudentListByUid(self):
        """
        title: 根据用户id查询用户班级关系列表_存在班级的学生账号
        url: /schooluserservice/class/getClassStudentListByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_getClassStudentListByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)

    def test_p1_2_class_getClassStudentListByUid(self):
        """
        title: 根据用户id查询用户班级关系列表_不存在班级的学生账号
        url: /schooluserservice/class/getClassStudentListByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.class_getClassStudentListByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(0, len(res['data']))

    def test_p1_1_class_listTeachingClassByUid(self):
        """
        title: 获取用户管辖的教学班列表_班主任
        url: /schooluserservice/class/listTeachingClassByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.class_listTeachingClassByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            if i['classId'] == groupid_xingzheng:
                self.assertEqual(expireyear, i['graduationYear'])
                self.assertEqual(schoolid, i['schoolId'])
                self.assertEqual(1, i['type'])
                self.assertTrue(i['numberOfStudent'] >= 10)

    def test_p1_2_class_listTeachingClassByUid(self):
        """
        title: 获取用户管辖的教学班列表_任课老师
        url: /schooluserservice/class/listTeachingClassByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.class_listTeachingClassByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            if i['classId'] == groupid_xingzheng:
                self.assertEqual(expireyear, i['graduationYear'])
                self.assertEqual(schoolid, i['schoolId'])
                self.assertEqual(1, i['type'])
                self.assertTrue(i['numberOfStudent'] >= 10)

    def test_p1_3_class_listTeachingClassByUid(self):
        """
        title: 获取用户管辖的教学班列表_教学班主任
        url: /schooluserservice/class/listTeachingClassByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.class_listTeachingClassByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            if i['classId'] == groupid_jiaoxue:
                self.assertEqual(expireyear, i['graduationYear'])
                self.assertEqual(schoolid, i['schoolId'])
                self.assertEqual(1, i['type'])
                self.assertTrue(i['numberOfStudent'] >= 10)

    def test_p1_4_class_listTeachingClassByUid(self):
        """
        title: 获取用户管辖的教学班列表_校长（只返回担任班主任/教学班主任/任课老师的班级）
        url: /schooluserservice/class/listTeachingClassByUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.class_listTeachingClassByUid(userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) < 10)


    def test_p1_1_class_getClassInfoAndHeadTeacherByClassIdList(self):
        """
        title: 批量获取班级信息及其班主任_行政班
        url: /schooluserservice/class/getClassInfoAndHeadTeacherByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.class_getClassInfoAndHeadTeacherByClassIdList(classIdList=[groupid_xingzheng])
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            self.assertEqual(expireyear, i['graduationYear'])
            self.assertEqual(str(schoolid), i['schoolId'])
            self.assertEqual(1, i['type'])
            self.assertTrue(i['numberOfStudent'] >= 10)
            self.assertEqual(str(teacher_web.client.user_id), i['headTeacherId'])

    def test_p1_2_class_getClassInfoAndHeadTeacherByClassIdList(self):
        """
        title: 批量获取班级信息及其班主任——教学班
        url: /schooluserservice/class/getClassInfoAndHeadTeacherByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.class_getClassInfoAndHeadTeacherByClassIdList(classIdList=[groupid_jiaoxue])
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            self.assertEqual(expireyear, i['graduationYear'])
            self.assertEqual(str(schoolid), i['schoolId'])
            self.assertEqual(2, i['type'])
            self.assertTrue(i['numberOfStudent'] >= 2)
            self.assertEqual(str(teacher_web.client.user_id), i['headTeacherId'])

    def test_p1_class_getClassStudentListBySchoolAndUid(self):
        """
        title: 根据学校id和用户id批量查询用户班级关系列表
        url: /schooluserservice/class/getClassStudentListBySchoolAndUid
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_getClassStudentListBySchoolAndUid(schoolId=schoolid, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)

    def test_p1_class_getClassStudentListBySchoolAndGrade(self):
        """
        title: 获取学校年级下的学生列表
        url: /schooluserservice/class/getClassStudentListBySchoolAndGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.class_getClassStudentListBySchoolAndGrade(schoolId=schoolid, graduationYear=expireyear)
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            self.assertTrue(i['classId'])
            self.assertTrue(i['userId'])
            self.assertEqual(str(schoolid), i['schoolId'])
            self.assertEqual(expireyear, i['graduationYear'])

    def test_p1_class_listClassDetailAndStudentsByClassIdList(self):
        """
        title: 根据班级id获取班级信息及学生信息
        url: /schooluserservice/class/listClassDetailAndStudentsByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student02_user['username']))
        res = teacher_web.class_listClassDetailAndStudentsByClassIdList(schoolId=schoolid, classIdList=[groupid_xingzheng, groupid_jiaoxue])
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)
        for i in res['data']:
            self.assertEqual(str(schoolid), i['schoolId'])
            self.assertIn(str(teacher_web.client.user_id), str(i['studentList']))

    def test_p1_class_listClassDetailAndStudentsByClassIdListContainLeft(self):
        """
        title: 根据班级id获取班级信息及学生信息
        url: /schooluserservice/class/listClassDetailAndStudentsByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_listClassDetailAndStudentsByClassIdList(schoolId=schoolid, classIdList=[groupid_xingzheng, groupid_jiaoxue])
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)
        self.assertTrue(len(res['data'][0]['studentList']) > 0)
        self.assertTrue(len(res['data'][1]['studentList']) > 0)

    def test_p1_1_class_listClassDetailAndStudents(self):
        """
        title: 根据班级和学生id查询学生信息、班级信息、学生班级关系
        url: /schooluserservice/class/listClassDetailAndStudents
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student07_user['username'], password=student07_user['password']))
        classAndStudentList = [
                {
                    "userId": teacher_web.client.user_id,
                    "classId": groupid_xingzheng
                }]
        res = teacher_web.class_listClassDetailAndStudents(classAndStudentList=classAndStudentList)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        self.assertEqual(str(schoolid), res['data'][0]['schoolId'])
        self.assertEqual(1,len(res['data'][0]['studentList']))

    def test_p1_2_class_listClassDetailAndStudents(self):
        """
        title: 根据班级和学生id查询学生信息、班级信息、学生班级关系-学生未加班
        url: /schooluserservice/class/listClassDetailAndStudents
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        classAndStudentList = [
                {
                    "userId": teacher_web.client.user_id,
                    "classId": groupid_xingzheng
                }]
        res = teacher_web.class_listClassDetailAndStudents(classAndStudentList=classAndStudentList)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        self.assertEqual(str(schoolid), res['data'][0]['schoolId'])
        self.assertEqual(0,len(res['data'][0]['studentList']))

    def test_p1_class_listClassInfoBySchoolAndGradeContainDisbanded(self):
        """
        title: 创建班级解散班级，获取学校的所有班级(包含行政班、教学班、已解散的班级)
        url: /schooluserservice/class/listClassInfoBySchoolAndGradeContainDisbanded
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.class_listClassInfoBySchoolAndGradeContainDisbanded(schoolId=schoolid, gradeYearList=[expireyear])
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)
        self.assertIn(str(groupid_isdeleted), classIds)

    def test_p1_class_listGradeAndClassBySchoolIdAndGrade(self):
        """
        title: 获取学校下所有班级
        url: /schooluserservice/class/listGradeAndClassBySchoolIdAndGrade
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_listGradeAndClassBySchoolIdAndGrade(schoolId=schoolid, graduationYearList=expireyear)
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data'][0]['classInfoList']]
        self.assertIn(str(groupid_xingzheng), classIds)
        self.assertIn(str(groupid_jiaoxue), classIds)
        for i in res['data'][0]['classInfoList']:
            self.assertEqual(expireyear, i['graduationYear'])
            self.assertIsNotNone(i['className'])
            self.assertIn(i['type'],[1,2])
            self.assertEqual(str(schoolid), i['schoolId'])

    def test_p1_class_listGradeAndClassBySchoolId(self):
        """
        title: 根据学校id获取学校下所有班级
        url: /schooluserservice/class/listGradeAndClassBySchoolId
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_listGradeAndClassBySchoolId(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']]
        self.assertIn(expireyear, graduationYears)
        for i in res['data']:
            self.assertTrue(len(i['classInfoList']) > 0)

    def test_p1_class_batchAddStudentToClass(self):
        """
        title: 加入班级（新模式批量导入-OA用）,使用OA踢出该用户
        url: /schooluserservice/class/oa/batchAddStudentToClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        studentList = [{"classId": groupid_xingzheng, "userId": teacher_web.client.user_id}]
        res = teacher_web.class_batchAddStudentToClass(schoolId=schoolid, studentList=studentList)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        self.oa.oaclass_kickStudent(classId=groupid_xingzheng, userId=teacher_web.client.user_id, updateUser="zhijun")
        self.assertEqual("200", res['code'])

    def test_p1_class_addSingleStudentToAdminClass(self):
        """
        title: 加入班级（.net对外提供用）
        url: /schooluserservice/class/addSingleStudentToAdminClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username'], password=student200_user['password']))
        res = teacher_web.class_addSingleStudentToAdminClass(classId=groupid_xingzheng, userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        self.oa.oaclass_kickStudent(classId=groupid_xingzheng, userId=teacher_web.client.user_id, updateUser="zhijun")
        self.assertEqual("200", res['code'])

    def test_p1_class_listClassesContainDisbanded(self):
        """
        title: 批量获取班级信息(包含解散)
        url: /schooluserservice/class/listClassesContainDisbanded
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_listClassesContainDisbanded(classIdList=[groupid_isdeleted, groupid_xingzheng, groupid_jiaoxue])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(3, len(res['data']))
        disbanded = [i['disbanded'] for i in res['data']]
        self.assertIn(False, disbanded)
        self.assertIn(True, disbanded)

    def test_p1_class_getClassInfoListByClassIdList(self):
        """
        title: 批量获取班级信息(不包含解散)
        url: /schooluserservice/class/getClassInfoListByClassIdList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.class_getClassInfoListByClassIdList(classIdList=[groupid_isdeleted, groupid_xingzheng, groupid_jiaoxue])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(2, len(res['data']))
        self.assertNotIn(str(groupid_isdeleted), str(res['data']))




