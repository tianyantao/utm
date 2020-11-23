from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import TeacherOaClient
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.eteacherprod.teacher_manage_data import *
from common.unittest_v2 import TestCaseV2


class StudentManage(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        # #将用户所在班级都设置为改名不限制
        # teacher_web = teacher(web_client(username=student02_user['username']))
        # res = teacher_web.studentManage_getMyClassList()
        # classIds = [i['classId'] for i in res['data']]
        # teacher_web = teacher(web_client(username=principal_user['username']))
        # res = teacher_web.classesManager_modifyClassConfig(classIdList=classIds,
        #                                                    classConfig={"type": 2,"value": classconfig_name[0][ 'value']},
        #                                                    updateUser="zhijun")
        # print(res)
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

    def test_p1_1_admin_pageStudentList(self):
        """
        title: 获取班级下学生列表_无条件
        url: /api/eteacherproduct/admin/classManage/pageStudentList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.admin_pageStudentList(schoolId=schoolid, classId=groupid_xingzheng, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        userIds = [i["userId"] for i in res['data']]
        self.assertIn(teacher_web.client.user_id, userIds)
        self.assertIn(student_user['username'], str(res['data']))
        self.assertTrue(len(res['data']) > 0)

    def test_p1_2_admin_pageStudentList(self):
        """
        title: 获取班级下学生列表_按userId精准查询
        url: /api/eteacherproduct/admin/classManage/pageStudentList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student07_user['username'], password=student07_user['password']))
        res = teacher_web.admin_pageStudentList(schoolId=schoolid, classId=groupid_xingzheng,
                                                userId=teacher_web.client.user_id, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIn(student07_user['username'], str(res['data']))
        self.assertEqual(1, len(res['data']))

    def test_p1_2_studentManage_info(self):
        """
        title: 获取未加班学生信息
        url: /api/eteacherproduct/studentManage/info
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.studentManage_info()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(teacher_web.client.user_id, res['data']['userId'])
        self.assertFalse(res['data']['ifJoinClass'])

    def test_p1_1_studentManage_studentChangeName(self):
        """
        title: 无班级学生可改名
        url: /api/eteacherproduct/studentManage/studentChangeName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.studentManage_studentChangeName(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                          name='123')
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    def test_p1_2_studentManage_studentChangeName(self):
        """
        title: 所属行政班 班级禁止改名，改名失败
        url: /api/eteacherproduct/studentManage/studentChangeName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res1 = teacher_web.classesManager_modifyClassConfig(classIdList=[groupid_xingzheng],
                                                            classConfig={"type": 2,
                                                                         "value": classconfig_name[1]['value']},
                                                            updateUser="zhijun")
        self.assertEqual("200", res1['code'])
        print(res1)
        teacher_web1 = teacher(web_client(username=student02_user['username']))
        res1 = teacher_web1.studentManage_studentChangeName(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                            name='02')
        print(res1)
        self.assertEqual("022626", res1['code'])
        self.assertEqual("所属班级不允许学生改名", res1['msg'])
        res2 = teacher_web.classesManager_modifyClassConfig(classIdList=[groupid_xingzheng],
                                                            classConfig={"type": 2,
                                                                         "value": classconfig_name[0]['value']},
                                                            updateUser="zhijun")
        print(res2)
        self.assertEqual("200", res2['code'])

    def test_p1_3_studentManage_studentChangeName(self):
        """
        title: 所属班级无禁止改名的设置
        url: /api/eteacherproduct/studentManage/studentChangeName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.classesManager_modifyClassConfig(classIdList=[groupid_xingzheng],
                                                           classConfig={"type": 2,
                                                                        "value": classconfig_name[0]['value']},
                                                           updateUser="zhijun")
        self.assertEqual("200", res['code'])
        print(res)
        teacher_web = teacher(web_client(username=student02_user['username']))
        res = teacher_web.studentManage_studentChangeName(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                          name='02')
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    def test_p1_4_studentManage_studentChangeName(self):
        """
        title: 所属教学班班级无禁止改名的设置，改名成功
        url: /api/eteacherproduct/studentManage/studentChangeName
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.classesManager_modifyClassConfig(classIdList=[groupid_jiaoxue],
                                                           classConfig={"type": 2,
                                                                        "value": classconfig_name[0]['value']},
                                                           updateUser="zhijun")
        self.assertEqual("200", res['code'])
        print(res)
        teacher_web = teacher(web_client(username=student02_user['username']))
        res = teacher_web.studentManage_studentChangeName(schoolId=schoolid, userId=teacher_web.client.user_id,
                                                          name='02')
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])

    # def test_p1_studentManage_canStudentChangeName(self):
    #     """
    #     title: 学生是否能够改名
    #     url: /api/eteacherproduct/studentManage/studentChangeName
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     res = teacher_web.classesManager_modifyClassConfig(classIdList=[groupid_jiaoxue],
    #                                                        classConfig={"type": 2,"value": classconfig_name[0][ 'value']},
    #                                                        updateUser="zhijun")
    #     self.assertEqual("200", res['code'])
    #     res = teacher_web.studentManage_canStudentChangeName(schoolId=schoolid, userId=teacher_web.client.user_id)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertTrue(res['data'])

    def test_p1_1_studentManage_getJoinedClassesAndExtendedInfo(self):
        """
        title: 获取学生已加入的班级和学校信息_已加班学生
        url: /api/eteacherproduct/studentManage/getJoinedClassesAndExtendedInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.studentManage_getJoinedClassesAndExtendedInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolId'])
        self.assertIn(str(groupid_xingzheng), str(res['data']['joinedAdminClassInfo']))
        self.assertIn(str(groupid_jiaoxue), str(res['data']['joinedTeachingClassList']))

    def test_p1_2_studentManage_getJoinedClassesAndExtendedInfo(self):
        """
        title: 获取学生已加入的班级和学校信息_未加班学生
        url: /api/eteacherproduct/studentManage/getJoinedClassesAndExtendedInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.studentManage_getJoinedClassesAndExtendedInfo()
        print(res)
        self.assertEqual("022210", res['code'])
        self.assertEqual('用户所属学校信息为空', res['msg'])

    def test_p1_studentManage_getMyClassList(self):
        """
        title: 获取学生已加入的班级列表信息
        url: /api/eteacherproduct/studentManage/getMyClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.studentManage_getMyClassList()
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(groupid_xingzheng, classIds)
        self.assertIn(groupid_jiaoxue, classIds)

    def test_p1_studentManage_getMySchoolAndGradeClassList(self):
        """
        title: 获取学生所在学校信息和其对应年级的所有班级信息
        url: /api/eteacherproduct/studentManage/getMySchoolAndGradeClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.studentManage_getMySchoolAndGradeClassList()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolInfo']['id'])
        self.assertEqual(expireyear, res['data']['gradeList'][0]['graduationYear'])
        for i in res['data']['gradeList'][0]['adminClasses']:
            if i['classId'] == groupid_xingzheng | i['classId'] == groupid_jiaoxue:
                self.assertTrue(i['ifJoinClass'])

    def test_p1_1_studentManage_getSchoolAndGradeClassList(self):
        """
        title: 未加班学生根据学校ID获取学校信息和该学校所有年级下的班级信息,默认每个年级都至少有一个班级
        url: /api/eteacherproduct/studentManage/getSchoolAndGradeClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.studentManage_getSchoolAndGradeClassList(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['schoolInfo']['id'])
        graduationYears = [i['graduationYear'] for i in res['data']['gradeList']]
        self.assertIn(expireyear, graduationYears)
        self.assertTrue(len(graduationYears) >= 3)
        for j in res['data']['gradeList']:
            self.assertTrue(len(j['adminClasses']) > 0)

    def test_p1_2_studentManage_getSchoolAndGradeClassList(self):
        """
        title: 已加班学生根据学校ID获取学校信息和该学校所有年级下的班级信息，提示错误
        url: /api/eteacherproduct/studentManage/getSchoolAndGradeClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.studentManage_getSchoolAndGradeClassList(schoolId=schoolid)
        print(res)
        self.assertEqual("506", res['code'])
        self.assertEqual("已加入学校，不能加入其它学校", res['msg'])

    def test_p1_studentManage_checkAddSingleStudentToClass(self):
        """
        title: 学生加班校验,根据获取的令牌建议验证班主任信息(班主任名字错误)
        url: /api/eteacherproduct/studentManage/checkAddSingleStudentToClass,/api/eteacherproduct/studentManage/joinClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student00_user['username'], password=student00_user['password']))
        res = teacher_web.studentManage_checkAddSingleStudentToClass(classId=groupid_xingzheng)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data']['hasHeadTeacher'])
        tk = res['data']['token']
        res2 = teacher_web.studentManage_joinClass(token=tk, headMasterName='13435436')
        print(res2)
        self.assertEqual("022620", res2['code'])
        self.assertEqual("班主任姓名不匹配", res2['msg'])

    def test_p1_studentManage_joinClass(self):
        """
        title: 学生加班校验,获取班主任姓名，根据获取的令牌建议验证班主任信息（班主任名字正确）,移除
        url: /api/eteacherproduct/studentManage/checkAddSingleStudentToClass,/api/eteacherproduct/studentManage/joinClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username']))
        res = teacher_web.studentManage_checkAddSingleStudentToClass(classId=groupid_xingzheng)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data']['hasHeadTeacher'])
        tk = res['data']['token']
        res1 = self.oa.oaclass_queryClassInfo(classId=groupid_xingzheng)
        print(res1)
        headTeacherName = res1['data']['headTeacherName']
        res2 = teacher_web.studentManage_joinClass(token=tk, headMasterName=headTeacherName)
        print(res2)
        self.assertEqual("200", res2['code'])
        self.oa.oaclass_kickStudent(classId=groupid_xingzheng, userId=teacher_web.client.user_id, updateUser="zhijun")

    def test_p1_studentManage_joinClass_old(self):
        """
        title: 学生加入班级（旧流程）
        url: /api/eteacherproduct/studentManage/oldJoinClass
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student200_user['username']))
        res1 = self.oa.oaclass_queryClassInfo(classId=groupid_xingzheng)
        print(res1)
        headTeacherName = res1['data']['headTeacherName']
        res = teacher_web.studentManage_oldJoinClass(classId=groupid_xingzheng, headMasterName=headTeacherName,
                                                     userId=teacher_web.client.user_id)
        print(res)
        self.assertEqual("200", res['code'])
        self.oa.oaclass_kickStudent(classId=groupid_xingzheng, userId=teacher_web.client.user_id, updateUser="zhijun")
