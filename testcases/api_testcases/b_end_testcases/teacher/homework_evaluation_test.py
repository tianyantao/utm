from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import AppClient as app_client
from testcases.api_testcases.b_end_testcases.case_services import *
from common.unittest_v2 import TestCaseV2
from common.helper import skip_dependon
import requests
from testcases.api_testcases.b_end_testcases.teacher.homework_evaluation_data import *
import json
import random
import re
import logging


class EvalutionTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_evaluationlist_by_principal(self):
        """
        title: 校长获取心理测评列表
        url: /api/services/HomeworkService/evaluation/GetEvaluationList
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.evaluation_GetEvaluationList()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertTrue(res['data'][-1]['grade'] == 3)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['grade'] == 3)
        self.assertTrue(int(res['data'][-1]['evaluationlist'][0]['id']) > 0)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['img'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['intro'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['tag'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['title'])

    def test_p1_evaluationlist_by_psychologicalteacher(self):
        """
        title: 心理老师获取心理测评列表
        url: /api/services/HomeworkService/evaluation/GetEvaluationList
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.evaluation_GetEvaluationList()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertTrue(res['data'][-1]['grade'] == 3)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['grade'] == 3)
        self.assertTrue(int(res['data'][-1]['evaluationlist'][0]['id']) > 0)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['img'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['intro'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['tag'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['title'])

    def test_p1_evaluationlist_by_headteacher(self):
        """
        title: 班主任获取心理测评列表
        url: /api/services/HomeworkService/evaluation/GetEvaluationList
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.evaluation_GetEvaluationList()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertTrue(res['data'][-1]['grade'] == 3)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['grade'] == 3)
        self.assertTrue(int(res['data'][-1]['evaluationlist'][0]['id']) > 0)
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['img'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['intro'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['tag'])
        self.assertTrue(res['data'][-1]['evaluationlist'][0]['title'])

    def test_p1_evaluationdetail(self):
        """
        title: 获取测评详情
        url: /api/services/HomeworkService/evaluation/GetEvaluationDetail
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.evaluation_GetEvaluationDetail(evaluationId=new_evalution_id)
        print(res)
        # 新测评详情不展示内容
        self.assertEqual(200, res['code'])
        self.assertEqual('执行成功', res['msg'])


def delete_new_evaluation(user=principal_user):
    teacher_web = teacher(web_client(username=user['username'], password=user['password']))
    homeworklist = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1)
    homework_delete_list = [i['homeworkid'] for i in homeworklist['data']['records'] if
                            i['evaluationid'] == new_evalution_id and i['iscandeletehomework']]
    for homeworkid in homework_delete_list:
        teacher_web.evaluation_deletehomework(homeworkid=homeworkid)


class NewEvalutionTest(TestCaseV2):

    homeworkids = []

    @classmethod
    def setUpClass(cls):
        pass
        for user in (principal_user, grademaster_user, psychologicalteacher_user, headteacher_user):
            delete_new_evaluation(user=user)

    @classmethod
    def tearDownClass(cls):
        pass

    def __get_new_evaluation_question_list(self, user, orderNo):
        url = question_list_url
        url = url + '?orderNo=' + str(orderNo)
        user_web = teacher(web_client(username=user['username'], password=user['password']))
        token = user_web.client.user_token
        headers = {"token": token}
        res = requests.get(url=url, headers=headers).content.decode('utf-8')
        return res

    def __submit_new_evaluation(self, user, orderNo):
        res = self.__get_new_evaluation_question_list(user=user, orderNo=orderNo)
        res = json.loads(res)
        # logging.info('__get_new_evaluation_question_list:{}'.format(res))
        data = \
            {
                "answerList": [],
                "answerTime": 118,
                "orderNo": orderNo
            }
        try:
            for i in res['data']:
                if i['type'] == 'radio_text':
                    answer = {"question_id": i['id'], "option_ids": [i['options'][random.randint(0,len(i['options'])-1)]['id']], "type": "radio_text"}
                    data['answerList'].append(answer)
        except Exception as e:
            print(res)
            raise e
        user_web = teacher(web_client(username=user['username'], password=user['password']))
        token = user_web.client.user_token
        headers = {
            "token": token,
            "Content-Type": "application/json"
        }
        res = requests.post(url=submit_url, headers=headers, json=data)
        return res.content.decode('utf-8')

    def __get_new_evaluation_orderno(self, user=student_user):
        teacher_web = teacher(web_client(username=user['username'], password=user['password']))
        # res = teacher_web.get_psychology_html()
        # orderno = re.findall('(?<=evalid={}&amp;orderNo=).*?(?=")'.format(new_evalution_id), res)
        res = teacher_web.getpsychologyhomework(schoolId=schoolid)
        link = [x['link'] for x in res['data']['records'] if int(x['evaluationid']) == new_evalution_id and x['step'] == 0]
        orderno = re.findall("(?<=evalid={}&orderNo=).*?(?=')".format(new_evalution_id), str(link))
        return orderno

    def test_p1_step00_gradeclassstateinfo(self):
        """
        title: 校长获取可布置的班级年级范围（布置新测评）
        url: /api/services/HomeworkService/evaluation/GradeClassStateInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_GradeClassStateInfo(evaluationId=new_evalution_id)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertIn(str(groupid_xingzheng), str(res))
        self.assertNotIn(str(groupid_jiaoxue), str(res))
        self.assertNotIn(str(groupid_isdeleted), str(res))
        for i in res['data']:
            for j in i['classlist']:
                if j['classid'] == groupid_xingzheng:
                    self.assertEqual(1, j['homeworksetstate'])

    def test_p1_step01_set_evaluation_homework_by_headteacher_scope2(self):
        """
        title: 行政班班主任布置班级心理测评（布置新测评）
        url: /api/services/HomeworkService/evaluation/SetHomework
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.evaluation_sethomework(evaluationid=new_evalution_id, scopetype=2,
                                                 gradescope=expireyear, classscope=[groupid_xingzheng], title='新测评test')
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data'])

    def test_p1_step02_gradeclassstateinfo(self):
        """
        title: 校长再次获取可布置的年级班级范围（布置一次之后，homeworksetstate变为2）
        url: /api/services/HomeworkService/evaluation/GradeClassStateInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        time.sleep(5)
        res = teacher_web.evaluation_GradeClassStateInfo(evaluationId=new_evalution_id)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertIn(str(groupid_xingzheng), str(res))
        self.assertNotIn(str(groupid_jiaoxue), str(res))
        self.assertNotIn(str(groupid_isdeleted), str(res))
        for i in res['data']:
            for j in i['classlist']:
                if j['classid'] == groupid_xingzheng:
                    self.assertEqual(2, j['homeworksetstate'])

    def test_p1_step03_set_evaluation_homework_by_principal_scope1(self):
        """
        title: 校长布置年级心理测评（布置新测评）
        url: /api/services/HomeworkService/evaluation/SetHomework
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_sethomework(evaluationid=new_evalution_id, scopetype=1,
                                                 gradescope=expireyear, classscope=[], title='新测评test')
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data'])

    # @unittest.skipIf(1 == 1, '暂时跳过')
    def test_p1_step04_set_evaluation_homework_by_headteacher_scope1(self):
        """
        title: 校长再次布置班级心理测评，会提示当前班级正在进行测评
        url: /api/services/HomeworkService/evaluation/SetHomework
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_sethomework(evaluationid=new_evalution_id, scopetype=1,
                                                 gradescope=expireyear,
                                                 classscope=[], title='新测评test')
        print(res)
        self.assertEqual(112, res['code'])
        self.assertEqual('当前年级正在进行此测评，无法重复布置', res['msg'])

    def test_p1_step05_summit_by_pc(self):
        """
        title: 学生在pc页面找到order no，然后提交年级测评和班级测评（先完成9个学生）
        url: /api/services/HomeworkService/evaluation/SetHomework
        author: 田彦涛
        """
        time.sleep(15)
        for user in (
        student_user, student02_user, student03_user, student04_user, student05_user, student06_user, student07_user,
        student08_user, student09_user):
            ordernos = ['']
            i = 0
            while i < 10 and ordernos[0] == '':
                ordernos = self.__get_new_evaluation_orderno(user=user)
                if i > 0:
                    time.sleep(5)
                    logging.warning("第{}次重试获取orderNo".format(i))
                i += 1
            if ordernos[0] == '':
                print('重试了10次之后页面上的orderNo还是为空')
                self.assertTrue(ordernos[0] != '')
            else:
                for orderno in ordernos:
                    self.__submit_new_evaluation(user=student_user, orderNo=orderno)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step06_get_by_app(self):
        """
        title: 学生在app上作业列表收到此测评
        url: /app/v1/homework/myhomework
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student10_user['username'], password=student10_user['password']))
        res = student_app.get_app_myhomework(status=1, tid=6)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("新测评test", str(res))
        global homeworkids
        homeworkids = [i['homeworkid'] for i in res['data']['list'] if i['title'] == '新测评test']
        homeworkids = sorted(homeworkids)
        self.assertTrue(len(homeworkids) > 1)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step07_homeworklist_by_principal_when_participatecount9(self):
        """
        title: 校长查看测评作业列表，小于10人完成时，不能查看班级报告和集体报告
        url: /api/services/HomeworkService/evaluation/GetHomeworkLogList
        author: 田彦涛
        """
        time.sleep(10)
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1, pagesize=50)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("新测评test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertTrue(len(homeworkids) > 1)
        # todo: 线下有个bug：
        # iscanreadreport = [i['iscanreadreport'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        # self.assertEqual([False, False], iscanreadreport)
        participatecount = [i['participatecount'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([9, 9], participatecount)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step08_submit_by_app(self):
        """
        title: 学生在app上获取新测评的作业id并且提交测评（第10个学生）
        url: /app/v1/homework/info
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student10_user['username'], password=student10_user['password']))
        for homeworkid in homeworkids:
            res = student_app.get_app_homework_info(cid=groupid_xingzheng, hid=homeworkid)
            print(res)
            self.assertEqual(200, res['code'])
            self.assertIn('orderNo=', str(res))
            orderNo = re.findall("(?<=orderNo=).*?(?=&)", res['data']['psydata']['newevaluationlink'])[0]
            self.__submit_new_evaluation(user=student10_user, orderNo=orderNo)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step09_homeworklist_by_principal_when_participatecount10(self):
        """
        title: 校长再次查看测评作业列表，10人完成时，可以查看班级报告和集体报告
        url: /api/services/HomeworkService/evaluation/GetHomeworkLogList
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1, pagesize=50)
        print(res)
        self.assertIn("新测评test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertTrue(len(homeworkids) > 1)
        iscanreadreport = [i['iscanreadreport'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([True, True], iscanreadreport)
        participatecount = [i['participatecount'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([10, 10], participatecount)
        return [i['reporturl'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step09_homeworklist_by_headteacher(self):
        """
        title: 行政班班主任查看心理测评作业列表
        url: /api/services/HomeworkService/evaluation/GetHomeworkLogList
        author: 田彦涛
        """
        time.sleep(3)  # 主从同步等待
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1, pagesize=50)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("新测评test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertTrue(len(homeworkids) > 1)
        iscanreadreport = [i['iscanreadreport'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        # self.assertEqual([True, False], iscanreadreport)
        # self.assertEqual([False, True], iscanreadreport)
        participatecount = [i['participatecount'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([10, 10], participatecount)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_step09_homeworklist_by_psychologicalteacher(self):
        """
        title: 心理老师查看心理测评作业列表
        url: /api/services/HomeworkService/evaluation/GetHomeworkLogList
        author: 田彦涛
        """
        teacher_web = teacher(
            web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        res = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1, pagesize=50)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("新测评test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertTrue(len(homeworkids) > 1)
        iscanreadreport = [i['iscanreadreport'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([True, True], iscanreadreport)
        participatecount = [i['participatecount'] for i in res['data']['records'] if i['homeworkname'] == '新测评test']
        self.assertEqual([10, 10], participatecount)

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test10_get_gateway_and_assert_reporturl(self):
        """
        title: 解析报告地址参数，通过网关接口查询该报告是否有效
        url: /api/services/HomeworkService/evaluation/GetHomeworkLogList
        author: 田彦涛
        """
        reporturl_list = self.test_p1_step09_homeworklist_by_principal_when_participatecount10()
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        token = teacher_web.client.user_token
        for reporturl in reporturl_list:
            decodeStr = re.findall("(?<=decodeStr=).*?(?=&)", reporturl)[0]
            type_ = re.findall("(?<=type=).*?(?=&)", reporturl)[0]
            clientId = re.findall("(?<=clientId=)[0-9]", reporturl)[0]
            url = report_url + '?clientId={0}&type={1}&decodeStr={2}'.format(clientId, type_, decodeStr)
            res = requests.get(url=url, headers={"token": token}).content.decode('utf-8')
            res = json.loads(res)
            print(res)
            self.assertEqual(200, int(res['code']))
            self.assertIn('http', res['data']['reportUrl'])

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test11_get_homeworkinfo_by_principal(self):
        """
        title: 校长获取心理测评作业info
        url: /api/teacher/homework/homeworkinfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        for homework in homeworkids:
            res = teacher_web.get_homeworkinfo_teacher(homeworkid=homework)
            print(res)
            self.assertEqual(200, res['code'])
            self.assertEqual(1, res['data']['homeworkstatus'])
            self.assertEqual(0, res['data']['kemu'])
            self.assertEqual(10, res['data']['participatedcount'])
            self.assertEqual(4, res['data']['type'])
            # self.assertIn('测评', res['data']['subject'])
            self.assertIn('心灵', res['data']['subject'])
            self.assertEqual('新测评test', res['data']['title'])

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test11_get_homeworkinfo_by_headteacher(self):
        """
        title: 行政班班主任获取心理测评作业info
        url: /api/teacher/homework/homeworkinfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        for homework in homeworkids:
            res = teacher_web.get_homeworkinfo_teacher(homeworkid=homework)
            print(res)
            self.assertEqual(200, res['code'])
            self.assertEqual(1, res['data']['homeworkstatus'])
            self.assertEqual(0, res['data']['kemu'])
            self.assertEqual(10, res['data']['participatedcount'])
            self.assertEqual(4, res['data']['type'])
            # self.assertIn('测评', res['data']['subject'])
            self.assertIn('心灵', res['data']['subject'])
            self.assertEqual('新测评test', res['data']['title'])

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test11_get_homeworkinfo_by_psychologicalteacher(self):
        """
        title: 心理老师获取心理测评作业info
        url: /api/teacher/homework/homeworkinfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        for homework in homeworkids:
            res = teacher_web.get_homeworkinfo_teacher(homeworkid=homework)
            print(res)
            self.assertEqual(200, res['code'])
            self.assertEqual(1, res['data']['homeworkstatus'])
            self.assertEqual(0, res['data']['kemu'])
            self.assertEqual(10, res['data']['participatedcount'])
            self.assertEqual(4, res['data']['type'])
            # self.assertIn('测评', res['data']['subject'])
            self.assertIn('心灵', res['data']['subject'])
            self.assertEqual('新测评test', res['data']['title'])

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test12_getclasscompletion_scope1(self):
        """
        title: 获取年级测评作业的班级完成情况
        url: /api/services/HomeworkService/evaluation/GetClassCompletion
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_GetClassCompletion(homeworkid=homeworkids[1], pagesize=40)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['records']) > 1)
        self.assertIn(str(groupid_xingzheng), str(res))
        self.assertNotIn(str(groupid_jiaoxue), str(res))
        self.assertNotIn(str(groupid_isdeleted), str(res))
        # 需求修改为已解散的班级也显示
        # self.assertIn(str(groupid_isdeleted), str(res))
        for i in res['data']['records']:
            if i['classid'] == groupid_xingzheng:
                self.assertTrue(i['iscanreadreport'])
                self.assertEqual(10, i['completestudentcount'])
                self.assertIn('decodeStr', i['reporturl'])

    @skip_dependon(depend='test_p1_step05_summit_by_pc')
    def test_p1_test12_getclasscompletion_scope2(self):
        """
        title: 获取班级测评作业的班级完成情况
        url: /api/services/HomeworkService/evaluation/GetClassCompletion
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.evaluation_GetClassCompletion(homeworkid=homeworkids[0], pagesize=40)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['records']) == 1)
        self.assertEqual(groupid_xingzheng, res['data']['records'][0]['classid'])
        self.assertTrue(res['data']['records'][0]['iscanreadreport'])
        self.assertEqual(10, res['data']['records'][0]['completestudentcount'])
        self.assertIn('decodeStr', res['data']['records'][0]['reporturl'])


class NewEvalutionTestForMonitor(TestCaseV2):

    homeworkids = []

    @classmethod
    def setUpClass(cls):
        pass
        for user in (principal_user, grademaster_user, psychologicalteacher_user, headteacher_user):
            delete_new_evaluation(user=user)

    @classmethod
    def tearDownClass(cls):
        pass

    def __get_new_evaluation_question_list(self, user, orderNo):
        url = question_list_url
        url = url + '?orderNo=' + str(orderNo)
        user_web = teacher(web_client(username=user['username'], password=user['password']))
        token = user_web.client.user_token
        headers = {"token": token}
        res = requests.get(url=url, headers=headers).content.decode('utf-8')
        return res

    def __submit_new_evaluation(self, user, orderNo):
        res = self.__get_new_evaluation_question_list(user=user, orderNo=orderNo)
        res = json.loads(res)
        # logging.info('__get_new_evaluation_question_list:{}'.format(res))
        data = \
            {
                "answerList": [],
                "answerTime": 118,
                "orderNo": orderNo
            }
        try:
            for i in res['data']:
                if i['type'] == 'radio_text':
                    answer = {"question_id": i['id'], "option_ids": [i['options'][random.randint(0,len(i['options'])-1)]['id']], "type": "radio_text"}
                    data['answerList'].append(answer)
        except Exception as e:
            print(res)
            raise e
        user_web = teacher(web_client(username=user['username'], password=user['password']))
        token = user_web.client.user_token
        headers = {
            "token": token,
            "Content-Type": "application/json"
        }
        res = requests.post(url=submit_url, headers=headers, json=data)
        return res.content.decode('utf-8')

    def __get_new_evaluation_orderno(self, user=student_user):
        teacher_web = teacher(web_client(username=user['username'], password=user['password']))
        res = teacher_web.getpsychologyhomework(schoolId=schoolid)
        link = [x['link'] for x in res['data']['records'] if x['evaluationid'] == new_evalution_id and x['step'] == 0]
        orderno = re.findall("(?<=evalid={}&orderNo=).*?(?=')".format(new_evalution_id), str(link))
        return orderno

    def test_p1_evaluation_homework_for_monitor(self):
        """
        title: 心理老师布置测评作业，学生app收到并作答，老师查看完成情况
        url: /api/services/HomeworkService/evaluation/GradeClassStateInfo, /api/services/HomeworkService/evaluation/SetHomework
        author: 田彦涛
        """
        # 心理老师获取测评作业可布置范围
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username'], password=psychologicalteacher_user['password']))
        res = teacher_web.evaluation_GradeClassStateInfo(evaluationId=new_evalution_id)
        # print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 2)
        self.assertIn(str(groupid_xingzheng), str(res))
        self.assertNotIn(str(groupid_jiaoxue), str(res))
        self.assertNotIn(str(groupid_isdeleted), str(res))
        for i in res['data']:
            for j in i['classlist']:
                if j['classid'] == groupid_xingzheng:
                    self.assertEqual(1, j['homeworksetstate'])
        # 心理老师布置测评作业到班级
        res = teacher_web.evaluation_sethomework(evaluationid=new_evalution_id, scopetype=2, deadlinetime=CaseServices.get_deadlinetime(),
                                                 gradescope=expireyear, classscope=[groupid_xingzheng], title='monitor_test')
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data'])
        # 学生从app作业列表获取测评作业
        time.sleep(10)
        student_app = teacher(app_client(username=student10_user['username'], password=student10_user['password']))
        res = student_app.get_app_myhomework(status=1, tid=6)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("monitor_test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['list'] if i['title'] == 'monitor_test']
        homeworkids = sorted(homeworkids)
        self.assertTrue(len(homeworkids) > 0)
        homeworkid = homeworkids[-1]
        # 学生获取心理测评作业info
        res = student_app.get_app_homework_info(cid=groupid_xingzheng, hid=homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn('orderNo=', str(res))
        orderNo = re.findall("(?<=orderNo=).*?(?=&)", res['data']['psydata']['newevaluationlink'])[0]
        # 学生提交测评作业
        self.__submit_new_evaluation(user=student10_user, orderNo=orderNo)
        # 行政班班主任查看测评作业记录
        time.sleep(3)  # 主从同步等待
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1, pagesize=50)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertIn("monitor_test", str(res))
        homeworkids = [i['homeworkid'] for i in res['data']['records'] if i['homeworkname'] == 'monitor_test']
        self.assertIn(homeworkid, homeworkids)
        participatecount = [i['participatecount'] for i in res['data']['records'] if i['homeworkid'] == homeworkid]
        self.assertEqual([1], participatecount)
