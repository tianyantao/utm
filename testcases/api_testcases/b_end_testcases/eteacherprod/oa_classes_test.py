from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import TeacherOaClient
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.eteacherprod.teacher_manage_data import *
from testcases.api_testcases.b_end_testcases.case_services import CaseServices
from common.unittest_v2 import TestCaseV2


class ClassesManagerTest(TestCaseV2):
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

    def test_p1_1_oaclass_list(self):
        """
        title: 获取学校下的无条件的所有班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid,  pageIndex=1, pageSize=200)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 2)

    def test_p1_2_oaclass_list(self):
        """
        title: 获取学校下的某一年级下的所有班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid, gradeYear=expireyear, pageIndex=1, pageSize=200)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        for i in res['data']:
            self.assertEqual(expireyear, i['gradeYear'])

    def test_p1_3_oaclass_list(self):
        """
        title: 根据班级名称模糊查询
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid, className=classNameKeyword, pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        for i in res['data']:
            self.assertIn(classNameKeyword, i['name'])

    def test_p1_4_oaclass_list(self):
        """
        title: 获取学校下的某一年级下的所有行政班
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid, gradeYear=expireyear, classType=1, pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        for i in res['data']:
            self.assertEqual(expireyear, i['gradeYear'])
            self.assertEqual(1, i['type'])

    def test_p1_5_oaclass_list(self):
        """
        title: 获取学校下的某一年级下的所有教学班
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid, gradeYear=expireyear, classType=2, pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        for i in res['data']:
            self.assertEqual(expireyear, i['gradeYear'])
            self.assertEqual(2, i['type'])

    def test_p1_6_oaclass_list(self):
        """
        title: 根据教学班主任的手机号筛选班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid,  headTeacherMobile=classheadteacher_user['username'], pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        self.assertIn(str(groupid_jiaoxue), str(res['data']))

    def test_p1_7_oaclass_list(self):
        """
        title: 根据行政班主任的手机号筛选班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid,  headTeacherMobile=headteacher_user['username'], pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        self.assertIn(str(groupid_xingzheng), str(res['data']))

    def test_p1_8_oaclass_list(self):
        """
        title: 根据精准匹配班主任姓名班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid,  headTeacherName=teacherName, pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)

    def test_p1_9_oaclass_list(self):
        """
        title: 混合搜索班级列表
        url: /api/eteacherproduct/oa/classManage/list
        author: 章志君
        """
        res = self.oa.oaclass_list(schoolId=schoolid, classType=1,gradeYear=expireyear+grade-2, className=classNameKeyword, headTeacherName=teacherNameKeyword, pageIndex=1, pageSize=30)
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_oaclass_listGrades(self):
        """
        title: 获取学校下的年级列表
        url: /api/eteacherproduct/oa/classManage/listGrades
        author: 章志君
        """
        res = self.oa.oaclass_listGrades()
        print(res)
        self.assertEqual("200", res['code'])
        for i in range(0,3):
            self.assertEqual(expireyear+grade-i, res['data'][i]['index'])
            self.assertIn("%s年入学"%(expireyear+grade-3-i), res['data'][i]['value'])

    def test_p1_oaclass_create_dissolveClass(self):
        """
        title: 创建行政班以classNo命名，解散行政班
        url: /api/eteacherproduct/oa/classManage/create,/api/eteacherproduct/oa/classManage/listGrades
        author: 章志君
        """
        res = self.oa.oaclass_create(schoolId=schoolid, type=1, graduationYear=expireyear, classNo=121333, allowUserJoinValue=0, allowStudentChangeValue=0)
        print(res)
        self.assertEqual("200", res['code'])
        res1 = self.oa.oaclass_list(schoolId=schoolid, classType=1, gradeYear=expireyear, pageIndex=1, pageSize=10)
        print(res1)
        for i in res1['data']:
            if i['classNo'] == 121333:
                classId = i['id']
        res2 = self.oa.oaclass_dissolveClass(classId)
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_1_oaclass_create_dissolveClass(self):
        """
        title: 创建行政班以className命名，解散行政班
        url: /api/eteacherproduct/oa/classManage/create,/api/eteacherproduct/oa/classManage/listGrades
        author: 章志君
        """
        res = self.oa.oaclass_create(schoolId=schoolid, type=1, graduationYear=expireyear, className=121333, allowUserJoinValue=0, allowStudentChangeValue=0)
        print(res)
        self.assertEqual("200", res['code'])
        res1 = self.oa.oaclass_list(schoolId=schoolid, classType=1, gradeYear=expireyear, pageIndex=1, pageSize=10)
        print(res1)
        for i in res1['data']:
            if i['name'] == '121333':
                classId = i['id']
        res2 = self.oa.oaclass_dissolveClass(classId)
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_2_oaclass_create_dissolveClass(self):
        """
        title: web端老师创建教学班，OA端解散教学班
        url: /api/eteacherproduct/oa/classManage/create,/api/eteacherproduct/oa/classManage/listGrades
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.classesManager_create(schoolId=schoolid, type=2, allowStudentChangeValue=0,
                                                allowUserJoinValue=0, graduationYear=expireyear, subjectId=2, className="nifnsif")
        res2 = self.oa.oaclass_dissolveClass(classId = res['data'])
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_1_oaclass_modify(self):
        """
        title: 修改教学班班级
        url: /api/eteacherproduct/oa/classManage/modify
        author: 章志君
        """
        res1 = self.oa.oaclass_queryClassInfo(classId=classId_jx)
        print(res1)
        res2 = self.oa.oaclass_modify(id=classId_jx, schoolId=schoolid, classLeaderId =res1['data']['headTeacherId'] ,type=2, graduationYear=expireyear, className="autozzjjx1", subjectId = 1, allowUserJoinValue=0, allowStudentChangeValue=0)
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_2_oaclass_modify(self):
        """
        title: 修改行政班班级
        url: /api/eteacherproduct/oa/classManage/modify
        author: 章志君
        """
        res = self.oa.oaclass_modify(id=classId_xz, schoolId=schoolid, classLeaderId =1 ,type=1, graduationYear=expireyear, className="autozzjxz1", allowUserJoinValue=0, allowStudentChangeValue=0)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    def test_p1_1_oaclass_getEnumDetailList(self):
        """
        title: 获取枚举详情列表,type=1 1：用户加班设置
        url: /api/eteacherproduct/oa/classManage/getEnumDetailList
        author: 章志君
        """
        res = self.oa.oaclass_getEnumDetailList(type=1)
        print(res)
        self.assertEqual(classconfig_add, res['data'])

    def test_p1_2_oaclass_getEnumDetailList(self):
        """
        title: 获取枚举详情列表,type=2 2：学生改名设置
        url: /api/eteacherproduct/oa/classManage/getEnumDetailList
        author: 章志君
        """
        res = self.oa.oaclass_getEnumDetailList(type=2)
        print(res)
        self.assertEqual(classconfig_name, res['data'])

    def test_p1_3_oaclass_getEnumDetailList(self):
        """
        title: 获取枚举详情列表,type=4 4：获取学科列表
        url: /api/eteacherproduct/oa/classManage/getEnumDetailList
        author: 章志君
        """
        res = self.oa.oaclass_getEnumDetailList(type=4)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(classconfig_subject, res['data'])

    def test_p1_1_oaclass_modifyClassConfig(self):
        """
        title: 批量修改班级配置_修改学生加班设置
        url: /api/eteacherproduct/oa/classManage/modifyClassConfig
        author: 章志君
        """
        res = self.oa.oaclass_modifyClassConfig(classIdList=[classId_jx,classId_xz],classConfig={"type":1, "value":classconfig_add[0]['value']}, updateUser="zhijun")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    def test_p1_2_oaclass_modifyClassConfig(self):
        """
        title: 批量修改班级配置_允许学生改名设置为不限制
        url: /api/eteacherproduct/oa/classManage/modifyClassConfig
        author: 章志君
        """
        res = self.oa.oaclass_modifyClassConfig(classIdList=[classId_jx,classId_xz],classConfig={"type":2, "value":classconfig_name[0]['value']}, updateUser="zhijun")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    def test_p1_oaclass_listClassStudent(self):
        """
        title: 查询教学班班级学生列表
        url: /api/eteacherproduct/oa/classManage/listClassStudent
        author: 章志君
        """
        res = self.oa.oaclass_listClassStudent(classId=groupid_xingzheng, account=student04_user['username'],userName="", userId="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual(student04_user['username'], res['data'][0]['account'])
        self.assertEqual(1, res['totalRecords'])


    def test_p1_oaclass_listClassStudent_kick_add(self):
        """
        title: 根据学生userID查询班级学生列表,从行政班级移除学生, 添加学生到行政班
        url: /api/eteacherproduct/oa/classManage/listClassStudent,/api/eteacherproduct/oa/classManage/kickStudent,/api/eteacherproduct/oa/classManage/addSingleStudentToClass
        author: 章志君
        """
        res = self.oa.oaclass_listClassStudent(classId=groupid_xingzheng, account="",userName="", userId=studentIds[0], pageIndex=1, pageSize=100)
        print(res)
        if res['totalRecords'] ==1:
            res1 = self.oa.oaclass_kickStudent(classId=groupid_xingzheng, userId=studentIds[0], updateUser="zhijun")
            print(res1)
            self.assertEqual("200", res1['code'])
        res2 = self.oa.oaclass_addSingleStudentToClass(schoolId=schoolid, classId=groupid_xingzheng, userId=studentIds[0], createUser="")
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_oaclass_listClassStudent_kick_add(self):
        """
        title: 根据学生userID查询班级学生列表,从教学班级移除学生, 添加学生到教学班
        url: /api/eteacherproduct/oa/classManage/listClassStudent,/api/eteacherproduct/oa/classManage/kickStudent,/api/eteacherproduct/oa/classManage/addSingleStudentToClass
        author: 章志君
        """
        res = self.oa.oaclass_listClassStudent(classId=groupid_jiaoxue, account="",userName="", userId=studentIds[0], pageIndex=1, pageSize=100)
        print(res)
        if res['totalRecords'] ==1:
            res1 = self.oa.oaclass_kickStudent(classId=groupid_jiaoxue, userId=studentIds[0], updateUser="zhijun")
            print(res1)
            self.assertEqual("200", res1['code'])
        res2 = self.oa.oaclass_addSingleStudentToClass(schoolId=schoolid, classId=groupid_jiaoxue, userId=studentIds[0], createUser="")
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_1_oaclass_queryStudent(self):
        """
        title: 查询学生信息,根据userId查询
        url: /api/eteacherproduct/oa/classManage/queryStudent
        author: 章志君
        """
        res = self.oa.oaclass_queryStudent(classId=classId_xz, account="",userId=studentIds[1], mobile="")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(studentIds[1], res['data']['userId'])

    def test_p1_2_oaclass_queryStudent(self):
        """
        title: 查询学生信息，根据account查询
        url: /api/eteacherproduct/oa/classManage/queryStudent
        author: 章志君
        """
        res = self.oa.oaclass_queryStudent(classId=groupid_jiaoxue, account=student00_user['username'], userId="", mobile="")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(student00_user['username'], res['data']['account'])

    def test_p1_oaclass_addSingleStudentToClass(self):
        """
        title:  已加入行政班学生加入到行政班，报错
        url: /api/eteacherproduct/oa/classManage/addSingleStudentToClass
        author: 章志君
        """
        res = self.oa.oaclass_addSingleStudentToClass(schoolId=schoolid, classId=groupid_xingzheng, userId=studentIds[3], createUser="")
        print(res)
        self.assertNotEqual(200, res['code'])

    def test_p1_oaclass_queryClassInfo(self):
        """
        title:  获取班级信息
        url: /api/eteacherproduct/oa/classManage/queryClassInfo
        author: 章志君
        """
        res = self.oa.oaclass_queryClassInfo(classId=groupid_xingzheng)
        print(res)
        self.assertNotEqual(200, res['code'])
        self.assertNotEqual(str(groupid_xingzheng), res['data']['classId'])
        self.assertTrue(res['data']['headTeacherId'] > 1)
        for i in res['data']['teacherList']:
            self.assertTrue(i['userId'] >1)
            self.assertTrue(i['subjectId'] > 0)

    def test_p1_oaclass_getSchoolClassList(self):
        """
        title:  获取学校下的班级列表（行政班）
        url: /api/eteacherproduct/oa/classManage/getSchoolClassList
        author: 章志君
        """
        get_classlist = self.oa.oaclass_getSchoolClassList()
        print(get_classlist)
        self.assertNotEqual(200, get_classlist['code'])
        self.assertEqual("200", get_classlist['code'])
        self.assertIn(CaseServices.get_expireyear()[0], [item['gradeYear'] for item in get_classlist['data']])
        self.assertIn(CaseServices.get_expireyear()[1], [item['gradeYear'] for item in get_classlist['data']])
        self.assertIn(CaseServices.get_expireyear()[2], [item['gradeYear'] for item in get_classlist['data']])
