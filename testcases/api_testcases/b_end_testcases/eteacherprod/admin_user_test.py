from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.eteacherprod.teacher_manage_data import *
from common.unittest_v2 import TestCaseV2


class StudentManage(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_admin_pageStudentList(self):
        """
        title: 获取已加班学生信息,按userId搜索
        url: /api/eteacherproduct/admin/classManage/pageStudentList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.admin_pageStudentList(schoolId=schoolid, studentName="", userId=teacher_web.client.user_id, classId=groupid_xingzheng, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        time.sleep(5)
        res1 = teacher_web.studentManage_info()
        self.assertEqual(student_user['username'], res['data'][0]['account'])
        self.assertEqual(res1['data']['userName'], res['data'][0]['userName'])

    def test_p1_2_admin_pageStudentList(self):
        """
        title: 获取已加班学生信息,按用户名称搜索
        url: /api/eteacherproduct/admin/classManage/pageStudentList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student07_user['username'], password=student07_user['password']))
        res1 = teacher_web.studentManage_info()
        print(res1)
        res = teacher_web.admin_pageStudentList(schoolId=schoolid, studentName=res1['data']['userName'], userId="", classId=groupid_xingzheng, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)

    def test_p1_1_admin_pageSchoolList(self):
        """
        title: 分页查询学校信息,使用学校名称关键字"测试"搜索
        url: /api/eteacherproduct/admin/schoolManage/pageSchoolList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.admin_pageSchoolList(schoolName="测试", provinceCode="", cityCode="", areaCode="", pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 0)
        for i in res['data']:
            self.assertTrue(i['id'] > 0)
            self.assertIn("测试", i['name'])

    def test_p1_2_admin_pageSchoolList(self):
        """
        title: 分页查询学校信息,使用浙江省份code "330000"搜索学校列表
        url: /api/eteacherproduct/admin/schoolManage/pageSchoolList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.admin_pageSchoolList(schoolName="", provinceCode="330000", pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 10)
        for i in res['data']:
            self.assertTrue(i['id'] > 0)
            self.assertIn("浙江", i['areaFullName'])

    def test_p1_1_admin_pageClasses(self):
        """
        title: 分页查询班级接口， 根据classId获取班级名称，根据获取的班级名称进行精准查询班级列表
        url: /api/eteacherproduct/admin/classesManager/queryClassInfo,/api/eteacherproduct/admin/classManage/pageClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res1 = teacher_web.classesManager_queryClassInfo(classId=groupid_xingzheng)
        print(res1)
        className = res1['data']['className']
        res = teacher_web.admin_pageClasses(schoolId=schoolid, className=className, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, len(res['data']))
        self.assertEqual(res1['data']['type'], res['data'][0]['type'])
        self.assertEqual(res1['data']['gradeName'], res['data'][0]['gradeName'])
        self.assertEqual(res1['data']['headTeacherId'], res['data'][0]['headTeacherId'])

    def test_p1_2_admin_pageClasses(self):
        """
        title: 分页查询班级接口， 根据行政班classId班级列表(#仅按班级名称精准查询，按classId精准查询有效)
        url: /api/eteacherproduct/admin/classManage/pageClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.admin_pageClasses(schoolId=schoolid, classId=groupid_xingzheng, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(groupid_xingzheng, res['data'][0]['classId'])

    def test_p1_3_admin_pageClasses(self):
        """
        title: 分页查询班级接口， 根据教学班classId班级列表
        url: /api/eteacherproduct/admin/classManage/pageClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.admin_pageClasses(schoolId=schoolid, classId=groupid_jiaoxue, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(groupid_jiaoxue, res['data'][0]['classId'])

    def test_p1_admin_updateSchoolConf(self):
        """
        title: 更新学校配置
        url: /api/eteacherproduct/admin/schoolManage/updateSchoolConf
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.admin_updateSchoolConf(schoolId=schoolid, confKey="SCHOOL_BASED_PAPERS_PERMISSION",
                                                 confValue="false")
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        res = teacher_web.admin_updateSchoolConf(schoolId=schoolid, confKey="SCHOOL_BASED_PAPERS_PERMISSION",
                                                 confValue="true")

    # def test_p1_admin_changeClassByExcel(self):
    #     """
    #     title: 批量导入 类型为6
    #     url: /api/eteacherproduct/admin/schoolManage/changeClassByExcel
    #     author: 章志君
    #     """
    #     teacher_web = teacher(web_client(username=principal_user['username']))
    #     files = {'file': open("D:\Backup\Downloads\2020-07-02-20-05-43-312633.xlsx", 'rb')}
    #     res = teacher_web.admin_changeClassByExcel(files=files)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertTrue(res['data'])

    def test_p1_admin_getExcelTemplateInfo(self):
        """
        title: 获取excel导入类型
        url: /api/eteacherproduct/admin/classManage/getExcelTemplateInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.admin_getExcelTemplateInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) > 3)
        self.assertIn("http://", str(res['data'][0]['value']))

    def test_p1_admin_querySchoolInfo(self):
        """
        title: 根据学校id对应的信息获取学校信息
        url: /api/eteacherproduct/admin/schoolManage/querySchoolInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.admin_querySchoolInfo(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(schoolid, res['data']['id'])

    def test_p1_1_admin_queryClassInfo(self):
        """
        title: 根据班级ID获取行政班班级信息
        url: /api/eteacherproduct/admin/classManage/queryClassInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.admin_queryClassInfo(classId=groupid_xingzheng)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, res['data']['type'])
        self.assertEqual(teacher_web.client.user_id, res['data']['headTeacherId'])


    def test_p1_2_admin_queryClassInfo(self):
        """
        title: 根据班级ID获取教学班班级信息
        url: /api/eteacherproduct/admin/classManage/queryClassInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user ['username']))
        res = teacher_web.admin_queryClassInfo(classId=groupid_jiaoxue)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(2, res['data']['type'])
        self.assertEqual(teacher_web.client.user_id, res['data']['headTeacherId'])
