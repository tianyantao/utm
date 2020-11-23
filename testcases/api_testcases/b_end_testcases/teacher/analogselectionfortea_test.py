from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.teacher.analogselectionfortea_data import *
from common.unittest_v2 import TestCaseV2
import datetime
import time
from testcases.api_testcases.b_end_testcases.case_services import CaseServices


class ContentsTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        global homeworkids_type
        homeworkids_type = {}
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_type14_analogtea_getquestionnaireinfo(self):
        """
        title: 验证getquestionnaireinfo获取的模拟选科信息_高一3+1+2
        url: /api/teacher/analogselectionfortea/getquestionnaireinfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=4)
        today = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        title = '%s高一年级模拟选科问卷' % (today)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertEqual(title, res['data']['title'])
        self.assertEqual(6, res['data']['subjectcount'])
        self.assertEqual(subjectlist_312, res['data']['subjectlist'])

    def test_p1_type11_analogtea_getquestionnaireinfo(self):
        """
        title: 验证getquestionnaireinfo获取的模拟选科信息_高一3+3 自由选科
        url: /api/teacher/analogselectionfortea/getquestionnaireinfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=1)
        today = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        title = '%s高一年级模拟选科问卷' % (today)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertEqual(title, res['data']['title'])
        self.assertEqual(6, res['data']['subjectcount'])
        self.assertEqual(subjectlist_33_1, res['data']['subjectlist'])

    def test_p1_type12_analogtea_getquestionnaireinfo(self):
        """
        title: 验证getquestionnaireinfo获取的模拟选科信息_高一3+3 定二走一
        url: /api/teacher/analogselectionfortea/getquestionnaireinfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=2)
        today = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        title = '%s高一年级模拟选科问卷' % (today)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertEqual(title, res['data']['title'])
        self.assertEqual(6, res['data']['subjectcount'])
        # self.assertEqual(subjectlist_33_2, res['data']['subjectlist'])

    def test_p1_type13_analogtea_getquestionnaireinfo(self):
        """
        title: 验证getquestionnaireinfo获取的模拟选科信息_高一3+3 固定套餐
        url: /api/teacher/analogselectionfortea/getquestionnaireinfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=3)
        today = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        title = '%s高一年级模拟选科问卷' % (today)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertEqual(title, res['data']['title'])
        self.assertEqual(6, res['data']['subjectcount'])
        # self.assertEqual(subjectlist_33_3, res['data']['subjectlist'])

    def test_p1_typ24_analogtea_getquestionnaireinfo(self):
        """
        title: 验证getquestionnaireinfo获取的模拟选科信息_高二3+1+2
        url: /api/teacher/analogselectionfortea/getquestionnaireinfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_getquestionnaireinfo(grade=2, type=4)
        today = datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        title = '%s高二年级模拟选科问卷' % (today)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertEqual(title, res['data']['title'])
        self.assertEqual(6, res['data']['subjectcount'])
        self.assertEqual(subjectlist_312, res['data']['subjectlist'])

    def test_p1_step01_type_14_analogtea_submithomework(self):
        """
        title: 验证教师端提交模拟选科问卷，查看布置成功模拟选科信息_高一3+1+2
        url: /api/teacher/analogselectionfortea/submithomework,/api/teacher/analogselectionfortea/getsuccesshomeworkdetail
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = '高一3+1+2模拟选科问卷'
        groups = []
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=4)
        for i in res['data']['subjectlist']:
            groups.append(i['id'])
        res = teacher_web.analogtea_submithomework(grade=1, type=4, title=title, subjectgroups=groups,
                                                   endtime=CaseServices.get_deadlinetime())
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertTrue(res['data'] > 1)
        # homeworkids_type[4] = res['data']
        res2 = teacher_web.analogtea_getsuccesshomeworkdetail(homeworkid=res['data'])
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertEqual("执行成功", res2['msg'])
        self.assertEqual(4, res2['data']['type'])
        self.assertEqual(title, res2['data']['title'])
        # self.assertEqual(tomorrow_time, res2['data']['endtime'])
        self.assertTrue(res2['data']['peoplenum'] >= 2)

    def test_p1_step01_type11_analogtea_submithomework(self):
        """
        title: 验证教师端提交模拟选科问卷，查看布置成功模拟选科信息_高一3+3 自由选科
        url: /api/teacher/analogselectionfortea/submithomework,/api/teacher/analogselectionfortea/getsuccesshomeworkdetail
        author: 章志君
        """
        time.sleep(10)
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = '高一3+3 自由选科模拟选科问卷'
        groups = []
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=1)
        for i in res['data']['subjectlist']:
            groups.append(i['id'])
        res = teacher_web.analogtea_submithomework(grade=1, type=1, title=title, subjectgroups=groups,
                                                   endtime=CaseServices.get_deadlinetime())
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertTrue(res['data'] > 1)
        # homeworkids_type[1] = res['data']
        res2 = teacher_web.analogtea_getsuccesshomeworkdetail(homeworkid=res['data'])
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertEqual("执行成功", res2['msg'])
        self.assertEqual(1, res2['data']['type'])
        self.assertEqual(title, res2['data']['title'])
        self.assertTrue(res2['data']['peoplenum'] >= 2)

    def test_p1_step01_type12_analogtea_submithomework(self):
        """
        title: 验证教师端提交模拟选科问卷，查看布置成功模拟选科信息_高一3+3 定二走一
        url: /api/teacher/analogselectionfortea/submithomework,/api/teacher/analogselectionfortea/getsuccesshomeworkdetail
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = '高一3+3 定二走一模拟选科问卷'
        groups = []
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=2)
        for i in res['data']['subjectlist']:
            groups.append(i['id'])
        res = teacher_web.analogtea_submithomework(grade=1, type=2, title=title, subjectgroups=groups,
                                                   endtime=CaseServices.get_deadlinetime())
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertTrue(res['data'] > 1)
        # homeworkids_type[2] = res['data']
        res2 = teacher_web.analogtea_getsuccesshomeworkdetail(homeworkid=res['data'])
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertEqual("执行成功", res2['msg'])
        self.assertEqual(2, res2['data']['type'])
        self.assertEqual(title, res2['data']['title'])
        # self.assertEqual(tomorrow_time, res2['data']['endtime'])
        self.assertTrue(res2['data']['peoplenum'] >= 2)

    def test_p1_step01_type13_analogtea_submithomework(self):
        """
        title: 验证教师端提交模拟选科问卷，查看布置成功模拟选科信息_高一3+3 固定套餐
        url: /api/teacher/analogselectionfortea/submithomework,/api/teacher/analogselectionfortea/getsuccesshomeworkdetail
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = '高一3+3 固定套餐模拟选科问卷'
        groups = []
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=3)
        for i in res['data']['subjectlist']:
            groups.append(i['id'])
        res = teacher_web.analogtea_submithomework(grade=1, type=3, title=title, subjectgroups=groups,
                                                   endtime=CaseServices.get_deadlinetime())
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("执行成功", res['msg'])
        self.assertTrue(res['data'] > 1)
        # homeworkids_type[3] = res['data']
        res2 = teacher_web.analogtea_getsuccesshomeworkdetail(homeworkid=res['data'])
        print(res2)
        self.assertEqual(200, res2['code'])
        self.assertEqual("执行成功", res2['msg'])
        self.assertEqual(3, res2['data']['type'])
        self.assertEqual(title, res2['data']['title'])
        # self.assertEqual(tomorrow_time, res2['data']['endtime'])
        self.assertTrue(res2['data']['peoplenum'] >= 2)

    def __analogtea_submithomework(self, type):
        teacher_web = teacher(web_client(username=principal_user['username']))
        title = '模拟选科问卷type{}'.format(type)
        groups = []
        res = teacher_web.analogtea_getquestionnaireinfo(grade=1, type=type)
        for i in res['data']['subjectlist']:
            groups.append(i['id'])
        res = teacher_web.analogtea_submithomework(grade=1, type=type, title=title, subjectgroups=groups,
                                                   endtime=CaseServices.get_deadlinetime())
        return res['data']

    def __assert_analogstu_getlist(self, homework_id):
        student_web = teacher(web_client(username=student02_user['username']))
        res = student_web.analogstu_getlist()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn(homework_id, [x['id'] for x in res['data']['list']])
        for i in res['data']['list']:
            if homework_id == i['id']:
                self.assertEqual(2, i['status'])

    def test_p1_step02_type14_analogstu_getlist(self):
        """
        title: 验证getlist获取学生端的模拟选科记录列表_高一3+1+2
        url: /student/subjectsystem/getlist, /api/student/analogselectionforstu/gethomeworkinfo, /api/student/analogselectionforstu/submithomework, /api/teacher/analogselectionfortea/GetListByPage, /api/teacher/analogselectionfortea/gethomeworkstatisticsinfo
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=4)
        time.sleep(10)
        self.__assert_analogstu_getlist(homework_id)
        res = self.__assert_analogstu_gethomeworkinfo(homework_id, type=4)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[], type=4,
                                                   subjectgroupid=res[0]['id'], subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)
        teacher_web = teacher(web_client(username=principal_user['username']))
        self.__assert_analogtea_gethomeworkstatisticsinfo(teacher_web, homework_id, 4)

    def test_p1_step02_type11_analogstu_getlist(self):
        """
        title: 验证getlist获取学生端的模拟选科记录列表_高一3+3 自由选科
        url: /student/subjectsystem/getlist, /api/student/analogselectionforstu/gethomeworkinfo, /api/student/analogselectionforstu/submithomework, /api/teacher/analogselectionfortea/GetListByPage, /api/teacher/analogselectionfortea/gethomeworkstatisticsinfo
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=1)
        time.sleep(10)
        self.__assert_analogstu_getlist(homework_id)
        self.__assert_analogstu_gethomeworkinfo(homework_id, type=1)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[8, 9, 10],
                                                   type=1, subjectgroupid=0, subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        self.__assert_analogtea_gethomeworkstatisticsinfo(teacher_web, homework_id, 1)

    def test_p1_step02_type12_analogstu_getlist(self):
        """
        title: 验证getlist获取学生端的模拟选科记录列表_高一3+3 定二走一
        url: /student/subjectsystem/getlist, /api/student/analogselectionforstu/gethomeworkinfo, /api/student/analogselectionforstu/submithomework, /api/teacher/analogselectionfortea/GetListByPage, /api/teacher/analogselectionfortea/gethomeworkstatisticsinfo
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=2)
        time.sleep(10)
        self.__assert_analogstu_getlist(homework_id)
        res = self.__assert_analogstu_gethomeworkinfo(homework_id, type=2)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[10], type=2,
                                                   subjectgroupid=res[0]['id'], subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        self.__assert_analogtea_gethomeworkstatisticsinfo(teacher_web, homework_id, 2)

    def test_p1_step02_type13_analogstu_getlist(self):
        """
        title: 验证getlist获取学生端的模拟选科记录列表_高一3+3 固定套餐
        url: /student/subjectsystem/getlist, /api/student/analogselectionforstu/gethomeworkinfo, /api/student/analogselectionforstu/submithomework, /api/teacher/analogselectionfortea/GetListByPage, /api/teacher/analogselectionfortea/gethomeworkstatisticsinfo
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=3)
        time.sleep(10)
        self.__assert_analogstu_getlist(homework_id)
        res = self.__assert_analogstu_gethomeworkinfo(homework_id, type=3)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[], type=3,
                                                   subjectgroupid=res[0]['id'], subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)

    def __assert_analogstu_gethomeworkinfo(self, homework_id, type=4):
        student_web = teacher(web_client(username=student02_user['username']))
        res = student_web.analogstu_gethomeworkinfo(homeworkid=homework_id)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(type, res['data']['type'])
        if type in [3, 4]:
            self.assertTrue(len(res['data']['subjectgrouplist']) > 0)
        else:
            self.assertTrue(len(res['data']['subjectlist']) > 0)
        return res['data']['subjectgrouplist']

    def __analogstu_submithomework_and_assert(self, homework_id, type, lastsubjects, subjectgroupid, subject_assert):
        student_web = teacher(web_client(username=student02_user['username']))
        res = student_web.analogstu_submithomework(homeworkid=homework_id, lastsubjects=lastsubjects, type=type,
                                                   subjectgroupid=subjectgroupid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(subject_assert, res['data'])

    def __assert_analogtea_GetListByPage(self, homework_id):
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_GetListByPage(keyword="", starttime="", endtime="", grade=0, type=0, status="1",
                                                  pageindex=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn(homework_id, [x['homeworkid'] for x in res['data']['records']])
        for i in res['data']['records']:
            if homework_id == i['homeworkid']:
                self.assertEqual(1, i['submitcnt'])

    def test_p1_step05_analogtea_GetConditions(self):
        """
        title: 教师端获取查询条件
        url: /api/teacher/analogselectionfortea/GetConditions
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.analogtea_GetConditions()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(conditions, res['data'])

    def __assert_analogtea_gethomeworkstatisticsinfo(self, client, homework_id, type):
        time.sleep(10)
        res = client.analogtea_gethomeworkstatisticsinfo(homeworkid=homework_id)
        self.assertEqual(200, res['code'])
        self.assertEqual("{0}({1}年入学)".format(gradename, expireyear - 3), res['data']['gradename'])
        self.assertEqual(1, res['data']['status'])
        self.assertTrue(res['data']['totalnum'] > 1)
        self.assertEqual(1, res['data']['completenum'])
        self.assertTrue(res['data']['nocompletenum'] > 1)
        self.assertEqual(type, res['data']['electivetype'])
        self.assertEqual(expireyear, res['data']['gradeyear'])

    def test_p1_step08_type14_analogtea_posthomeworkstatistics(self):
        """
        title: 教师端查看3+1+2的模拟选科分析
        url: /api/teacher/analogselectionfortea/posthomeworkstatistics
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=4)
        res = self.__assert_analogstu_gethomeworkinfo(homework_id, type=4)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[], type=4,
                                                   subjectgroupid=res[0]['id'], subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)
        teacher_web = teacher(web_client(username=principal_user['username']))
        self.__assert_analogtea_gethomeworkstatisticsinfo(teacher_web, homework_id, 4)

        res = teacher_web.analogtea_posthomeworkstatistics(homeworkid=homework_id, classId=0)
        print(res)
        self.assertEqual(200, res['code'])
        for i in res['data']['onesubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "生物" or i['subjectname'] == "化学" or i[
                'subjectname'] == "物理" else self.assertEqual("0", i['totalpeople'])
        for i in res['data']['twosubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "化学、生物" else self.assertEqual("0", i[
                'totalpeople'])
        for i in res['data']['threesubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理、化学、生物" else self.assertEqual("0", i[
                'totalpeople'])
        for i in res['data']['physicsorhistorylist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理" else self.assertEqual("0",
                                                                                                      i['totalpeople'])

        self.assertEqual("{0}({1}年入学)".format(gradename, expireyear - 3), res['data']['classname'])
        self.assertTrue(res['data']['totalstudentnum'] >= 2)
        self.assertTrue(res['data']['joinstudentnum'] >= 1)
        self.assertTrue(res['data']['unjoinstudentnum'] >= 1)

    def test_p1_step08_type11_analogtea_posthomeworkstatistics(self):
        """
        title: 教师端查看自由选科的模拟选科分析
        url: /api/teacher/analogselectionfortea/posthomeworkstatistics
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=1)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[8, 9, 10], type=1,
                                                   subjectgroupid=0, subject_assert='物理、化学、生物')
        self.__assert_analogtea_GetListByPage(homework_id)
        teacher_web = teacher(web_client(username=principal_user['username']))

        res = teacher_web.analogtea_posthomeworkstatistics(homeworkid=homework_id, classId=0)
        print(res)
        self.assertEqual(200, res['code'])
        for i in res['data']['onesubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "生物" or i['subjectname'] == "化学" or i[
                'subjectname'] == "物理" else self.assertEqual("0", i['totalpeople'])
        for i in res['data']['twosubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "化学、生物" or i['subjectname'] == "物理、生物" or i[
                'subjectname'] == "物理、化学" else self.assertEqual("0", i['totalpeople'])
        for i in res['data']['threesubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理、化学、生物" else self.assertEqual("0", i[
                'totalpeople'])
        self.assertEqual("{0}({1}年入学)".format(gradename, expireyear - 3), res['data']['classname'])
        self.assertTrue(res['data']['totalstudentnum'] >= 2)
        self.assertTrue(res['data']['joinstudentnum'] >= 1)
        self.assertTrue(res['data']['unjoinstudentnum'] >= 1)

    def test_p1_step08_type12_analogtea_posthomeworkstatistics(self):
        """
        title: 教师端查看定二走一的模拟选科分析
        url: /api/teacher/analogselectionfortea/posthomeworkstatistics
        author: 章志君
        """
        homework_id = self.__analogtea_submithomework(type=2)
        time.sleep(5)
        self.__assert_analogstu_getlist(homework_id)
        res = self.__assert_analogstu_gethomeworkinfo(homework_id, type=2)
        self.__analogstu_submithomework_and_assert(homework_id=homework_id, lastsubjects=[10], type=2,
                                                   subjectgroupid=res[0]['id'], subject_assert='物理、化学、生物')

        teacher_web = teacher(web_client(username=principal_user['username']))

        res = teacher_web.analogtea_posthomeworkstatistics(homeworkid=homework_id, classId=0)
        print(res)
        self.assertEqual(200, res['code'])
        for i in res['data']['twosubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理、化学" else self.assertEqual("0", i[
                'totalpeople'])
        for i in res['data']['threesubjectanalyselist']:
            self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理、化学、生物" else self.assertEqual("0", i[
                'totalpeople'])
        self.assertEqual("{0}({1}年入学)".format(gradename, expireyear - 3), res['data']['classname'])
        self.assertTrue(res['data']['totalstudentnum'] >= 2)
        self.assertTrue(res['data']['joinstudentnum'] >= 1)
        self.assertTrue(res['data']['unjoinstudentnum'] >= 1)
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.analogtea_HomeworkRecordClasses(homeworkid=homework_id)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual("全部", res['data'][0]['classname'])
        self.assertEqual(groupid_xingzheng, res['data'][1]['classid'])

# TODO:
#     @skip_dependon(depend='test_p1_step04_type13_analogstu_submithomework')
#     def test_p1_step08_type13_analogtea_posthomeworkstatistics(self):
#         """
#         title: 教师端查看固定套餐的模拟选科分析
#         url: /api/teacher/analogselectionfortea/posthomeworkstatistics, /api/teacher/analogselectionfortea/HomeworkRecordClasses
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_posthomeworkstatistics(homeworkid=homeworkids_type[3], classId=0)
#         print(res)
#         self.assertEqual(200, res['code'])
#         for i in res['data']['threesubjectanalyselist']:
#             self.assertEqual("1", i['totalpeople']) if i['subjectname'] == "物理、化学、生物" else self.assertEqual("0", i['totalpeople'])
#         self.assertEqual("高一3+3 固定套餐模拟选科问卷", res['data']['homeworktitle'])
#         self.assertEqual("高一(%s年入学)" % current_school_year, res['data']['classname'])
#         self.assertTrue(res['data']['totalstudentnum'] >= 2)
#         self.assertTrue(res['data']['joinstudentnum'] >= 1)
#         self.assertTrue(res['data']['unjoinstudentnum'] >= 1)
#
#     @skip_dependon(depend='test_p1_step04_type11_analogstu_submithomework')
#     def test_p1_step09_type11_analogtea_postselectedsubjectlist(self):
#         """
#         title: 教师端选科明细_自由选科
#         url: /api/teacher/analogselectionfortea/postselectedsubjectlist
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_postselectedsubjectlist(homeworkid=homeworkids_type[1], classid="0", type=1, pageindex=1, pagesize=15, singlesubject="0", subjectgroupid="0")
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual(["物理","化学","生物"], res['data']['records'][0]['singlesubjectlist'])
#         self.assertEqual("物理", res['data']['records'][0]['singlesubjectone'])
#         self.assertEqual("化学", res['data']['records'][0]['singlesubjecttwo'])
#         self.assertEqual("生物", res['data']['records'][0]['singlesubjectthree'])
#         self.assertTrue(len(res['data']['records'][0]['name']) > 0)
#         self.assertTrue(res['data']['totalcount'] >= 1)
#
#     @skip_dependon(depend='test_p1_step04_type12_analogstu_submithomework')
#     def test_p1_step09_type12_analogtea_postselectedsubjectlist(self):
#         """
#         title: 教师端选科明细_定二走一
#         url: /api/teacher/analogselectionfortea/postselectedsubjectlist
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_postselectedsubjectlist(homeworkid=homeworkids_type[2], classid="0", type=2, pageindex=1, pagesize=15, singlesubject="0", subjectgroupid="0")
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("物理、化学、生物", res['data']['records'][0]['subjectgroupname'])
#         self.assertTrue(len(res['data']['records'][0]['name']) > 0)
#         self.assertTrue(res['data']['totalcount'] >= 1)
#
#     @skip_dependon(depend='test_p1_step04_type13_analogstu_submithomework')
#     def test_p1_step09_type13_analogtea_postselectedsubjectlist(self):
#         """
#         title: 教师端选科明_固定套餐
#         url: /api/teacher/analogselectionfortea/postselectedsubjectlist
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_postselectedsubjectlist(homeworkid=homeworkids_type[3], classid="0", type=3, pageindex=1, pagesize=15, singlesubject="0", subjectgroupid="0")
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("物理、化学、生物", res['data']['records'][0]['subjectgroupname'])
#         self.assertTrue(len(res['data']['records'][0]['name']) > 0)
#         self.assertTrue(res['data']['totalcount'] >= 1)
#
#     @skip_dependon(depend='test_p1_step04_type14_analogstu_submithomework')
#     def test_p1_step09_type14_analogtea_postselectedsubjectlist(self):
#         """
#         title: 教师端选科明细_3+1+2
#         url: /api/teacher/analogselectionfortea/postselectedsubjectlist
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_postselectedsubjectlist(homeworkid=homeworkids_type[4], classid="0", type=4, pageindex=1, pagesize=15, singlesubject="0", subjectgroupid="0")
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("物理、化学、生物", res['data']['records'][0]['subjectgroupname'])
#         self.assertTrue(len(res['data']['records'][0]['name']) > 0)
#         self.assertTrue(res['data']['totalcount'] >= 1)
#
#     @skip_dependon(depend='test_p1_step01_type11_analogtea_submithomework')
#     def test_p1_step10_analogtea_HomeworkRecordClasses(self):
#         """
#         title: 教师端选科_获取作业布置到的班级列表
#         url: /api/teacher/analogselectionfortea/HomeworkRecordClasses
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_HomeworkRecordClasses(homeworkid=homeworkids_type[1])
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("全部", res['data'][0]['classname'])
#         self.assertEqual(classinfo['classId'], res['data'][1]['classid'])
#         self.assertEqual(classinfo['className'] + "(%s年入学)"%str(current_school_year), res['data'][1]['classname'])
#
#     @skip_dependon(depend='test_p1_step01_type14_analogtea_submithomework')
#     def test_p1_step11_type14_analogtea_posthomeworkstatisticsdetail(self):
#         """
#         title: 教师端选科明细筛选条件 4
#         url: /api/teacher/analogselectionfortea/posthomeworkstatisticsdetail
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_posthomeworkstatisticsdetail(homeworkid=homeworkids_type[4])
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual(subjectlist_33_1, res['data']['onesubjectanalyselist'])
#         for i in (0, len(subjectlist_312) - 1):
#             self.assertEqual(str(subjectlist_312[i]['id']), res['data']['twoorthreesubjectanalyselist'][i]['id'])
#
#     @skip_dependon(depend='test_p1_step01_type11_analogtea_submithomework')
#     def test_p1_step11_type11_analogtea_posthomeworkstatisticsdetail(self):
#         """
#         title: 教师端选科明细筛选条件自由选科
#         url: /api/teacher/analogselectionfortea/posthomeworkstatisticsdetail
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_posthomeworkstatisticsdetail(homeworkid=homeworkids_type[1])
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual(subjectlist_33_1, res['data']['onesubjectanalyselist'])
#         for i in subjectlist_33_1:
#             self.assertIn(str(i['id']), str(res['data']['twoorthreesubjectanalyselist']))
#
#     @skip_dependon(depend='test_p1_step01_type12_analogtea_submithomework')
#     def test_p1_step11_type12_analogtea_posthomeworkstatisticsdetail(self):
#         """
#         title: 教师端选科明细筛选条件 定二走一
#         url: /api/teacher/analogselectionfortea/posthomeworkstatisticsdetail
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_posthomeworkstatisticsdetail(homeworkid=homeworkids_type[2])
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual(subjectlist_33_1, res['data']['onesubjectanalyselist'])
#         for i in subjectlist_33_2:
#             self.assertIn(str(i['id']), str(res['data']['twoorthreesubjectanalyselist']))
#
#     @skip_dependon(depend='test_p1_step01_type13_analogtea_submithomework')
#     def test_p1_step11_type13_analogtea_posthomeworkstatisticsdetail(self):
#         """
#         title: 教师端选科明细筛选条件 固定套餐
#         url: /api/teacher/analogselectionfortea/posthomeworkstatisticsdetail
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         res = teacher_web.analogtea_posthomeworkstatisticsdetail(homeworkid=homeworkids_type[3])
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual(subjectlist_33_1, res['data']['onesubjectanalyselist'])
#         for i in subjectlist_33_3:
#             self.assertIn(str(i['id']), str(res['data']['twoorthreesubjectanalyselist']))
#
#     def test_p1_step12_analogtea_cancelsubject(self):
#         """
#         title: 教师端，撤回布置的模拟选科作业.且作业撤回列表中有撤回的模拟选科作业
#         url: /api/student/analogselectionfortea/cancelsubject
#         author: 章志君
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         for type in (1,4):
#             res = teacher_web.analogtea_cancelsubject(homeworkid=homeworkids_type[type])
#             print(res)
#             self.assertEqual(200, res['code'])
#             res2 = teacher_web.analogtea_GetListByPage(keyword="", starttime="", endtime="", grade=0, type=0,
#                                                        status="3",
#                                                        pageindex=1)
#             print(res2)
#             self.assertEqual(200, res2['code'])
#             self.assertIn(str(homeworkids_type[type]), str(res2))
