from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import TeacherOaClient
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.eteacherprod.teacher_manage_data import *
from common.unittest_v2 import TestCaseV2


class OAManageTeacherTest(TestCaseV2):
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

    def test_p1_1_oateacher_querySchoolInfo(self):
        """
        title: 根据token对应的信息获取学校信息
        url: /api/eteacherproduct/oa/schoolManage/querySchoolInfo
        author: 章志君
        """
        res = self.oa.oateacher_querySchoolInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(schoolid, res['data']['id'])
        self.assertTrue(len(res['data']['name']) > 1)
        self.assertTrue(len(res['data']['provinceName']) > 1)
        self.assertTrue(len(res['data']['cityName']) > 0)
        self.assertTrue(len(res['data']['areaName']) > 1)
        self.assertTrue(res['data']['teacherCount'] > 1)
        self.assertTrue(res['data']['classCount'] > 1)
        self.assertTrue(res['data']['studentCount'] > 1)

    def test_p1_oateacher_addTeacher(self):
        """
        title: OA教师端新增教师, 然后删除老师
        url: /api/eteacherproduct/oa/teacherManage/addTeacher,/api/eteacherproduct/oa/teacherManage/removeTeacher
        author: 章志君
        """
        res2 = self.oa.oateacher_removeTeacher(teacherId=userIdTest1)
        print(res2)
        self.assertEqual("200", res2['code'])
        rolelist = [{"role": 1}, {"role": 2, "manageYear": [expireyear]}, {"role": 5},
                    {"role": 6, "manageClass": [classIdTest]},
                    {"role": 7, "teachInfo": [{"teachSubjectId": 1, "teachClass": [classIdTest]}]}]
        res = self.oa.oateacher_addTeacher(userId=userIdTest1, cellphone=cellphone1, teacherName="hh",
                                           roleList=rolelist)
        print(res)
        self.assertEqual("200", res['code'])
        res3 = self.oa.oateacher_removeTeacher(teacherId=userIdTest1)
        print(res3)
        self.assertEqual("200", res3['code'])

    def test_p1_1_oateacher_queryUserInfoByCellphone(self):
        """
        title: OA教师端 根据手机号获取用户信息_用户信息不存在
        url: /api/eteacherproduct/oa/teacherManage/queryUserInfoByCellphone
        author: 章志君
        """
        res = self.oa.oateacher_queryUserInfoByCellphone(cellphone=cellphone3)
        print(res)
        self.assertEqual("022601", res['code'])
        self.assertEqual("老师信息不存在", res['msg'])

    def test_p1_2_oateacher_queryUserInfoByCellphone(self):
        """
        title: OA教师端 根据手机号获取用户信息，老师身份未添加
        url: /api/eteacherproduct/oa/teacherManage/queryUserInfoByCellphone
        author: 章志君
        """
        res = self.oa.oateacher_queryUserInfoByCellphone(cellphone=cellphone1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(cellphone1), res['data']['cellphone'])
        self.assertEqual(userIdTest1, res['data']['userId'])

    def test_p1_3_oateacher_queryUserInfoByCellphone(self):
        """
        title: OA教师端 根据手机号获取用户信息，老师身份已添加
        url: /api/eteacherproduct/oa/teacherManage/queryUserInfoByCellphone
        author: 章志君
        """
        res = self.oa.oateacher_queryUserInfoByCellphone(cellphone=cellphone)
        print(res)
        self.assertEqual("022603", res['code'])
        self.assertEqual("教师身份已添加", res['msg'])

    def test_p1_1_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下所有教师列表_无条件查询
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'], len(res['data']))

    def test_p1_2_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表_模糊查询老师名字为（）
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, name=teacherNameKeyword)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(0 < len(res['data']) < 20)

    def test_p1_3_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表_根据手机号查询
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, cellphone=cellphone)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, len(res['data']))
        self.assertEqual(userIdTest, res['data'][0]['userId'])

    # 线上无有账号信息的老师
    # def test_p1_4_oateacher_listTeacher(self):
    #     """
    #     title: OA教师端 分页查询学校下教师列表_根据账号查询
    #     url: /api/eteacherproduct/oa/teacherManage/listTeacher
    #     author: 章志君
    #     """
    #     res =  self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, account=teacherAccount)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual(1,len(res['data']))

    def test_p1_5_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表_模糊查询班级名称
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, className=classNameKeyword)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(0 < len(res['data']) < 10)

    def test_p1_6_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表_角色为教学班主任
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, role=4)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) < 10)

    def test_p1_7_oateacher_listTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表_混合查询
        url: /api/eteacherproduct/oa/teacherManage/listTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listTeacher(pageIndex=1, pageSize=200, name=teacherNameKeyword, cellphone=cellphone,
                                            className=classNameKeyword, role=-1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) < 10)

    def test_p1_oateacher_updateTeacher(self):
        """
        title: OA教师端 分页查询学校下教师列表, 然后查询老师的角色信息
        url: /api/eteacherproduct/oa/teacherManage/updateTeacher,/api/eteacherproduct/oa/teacherManage/queryTeacherRoleInfo
        author: 章志君
        """
        rolelist = [{"role": 1}, {"role": 2, "manageYear": [expireyear]}, {"role": 5},
                    {"role": 6, "manageClass": [classIdTest]},
                    {"role": 7, "teachInfo": [{"teachSubjectId": 1, "teachClass": [classIdTest]}]}]
        res = self.oa.oateacher_updateTeacher(userId=userIdTest, cellphone=cellphone, teacherName="hh",
                                              roleList=rolelist)
        print(res)
        self.assertEqual("200", res['code'])
        res1 = self.oa.oateacher_queryTeacherRoleInfo(userId=userIdTest)
        print(res1)
        self.assertEqual("200", res1['code'])
        self.assertEqual(5, len(res1['data']))
        for i in range(0, len(rolelist)):
            print(i)
            self.assertEqual(rolelist[i]['role'], res1['data'][i]['role'])
        res2 = self.oa.oateacher_updateTeacher(userId=userIdTest, cellphone=cellphone, teacherName="hh",
                                               roleList=[{"role": 1}])
        print(res2)
        self.assertEqual("200", res2['code'])
        res4 = self.oa.oateacher_queryTeacherRoleInfo(userId=userIdTest)
        print(res4)
        self.assertEqual("200", res4['code'])
        self.assertEqual(1, len(res4['data']))
        self.assertEqual(1, res4['data'][0]['role'])

    def test_p1_oateacher_listSimpleTeacher(self):
        """
        title: OA教师端 查询学校下所有的教师列表(发送短信)
        url: /api/eteacherproduct/oa/teacherManage/listSimpleTeacher
        author: 章志君
        """
        res = self.oa.oateacher_listSimpleTeacher()
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            self.assertTrue(i['userId'] > 1, i)

    def test_p1_oateacher_sendMessages(self):
        """
        title: 发送短信
        url: /api/eteacherproduct/oa/teacherManage/sendMessages
        author: 章志君
        """
        res = self.oa.oateacher_sendMessages(userIdList=[userIdTest1])
        print(res)
        self.assertEqual("200", res['code'])

    def test_p1_oateacher_queryTeacherRoleInfo(self):
        """
        title: 查询老师的角色信息，无职务
        url: /api/eteacherproduct/oa/teacherManage/queryTeacherRoleInfo
        author: 章志君
        """
        res = self.oa.oateacher_queryTeacherRoleInfo(userId=userIdTest1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual([], res['data'])

    def test_p1_oateacher_querySubjectInfo(self):
        """
        title: 获取科目列表
        url: /api/eteacherproduct/oa/teacherManage/querySubjectInfo
        author: 章志君
        """
        res = self.oa.oateacher_querySubjectInfo()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(subjectlistNeedAll, res['data'])

    def test_p1_oateacher_queryPositionInfo(self):
        """
        title: 获取角色列表_needAll=1, 返回职务中包含全部、其他、教学班主任 职务
        url: /api/eteacherproduct/oa/teacherManage/queryPositionInfo
        author: 章志君
        """
        res = self.oa.oateacher_queryPositionInfo(needAll=1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(rolelistNeedALL, res['data'])

    def test_p1_2_oateacher_queryPositionInfo(self):
        """
        title: 获取角色列表_默认条件，不需要返回全部、其他、教学班主任 职务
        url: /api/eteacherproduct/oa/teacherManage/queryPositionInfo
        author: 章志君
        """
        res = self.oa.oateacher_queryPositionInfo(needAll=0)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(rolelistNotALL, res['data'])
