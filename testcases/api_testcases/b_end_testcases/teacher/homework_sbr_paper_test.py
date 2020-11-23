from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import AppClient as app_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2
from testcases.api_testcases.b_end_testcases.homework_data import *
from testcases.api_testcases.b_end_testcases.teacher.homework_sbr_paper_data import *
from config.config_case import ConfigCase
from testcases.api_testcases.b_end_testcases.case_services import *
import unittest


allgrade = ['全部', '高一', '高二', '高三']
allsubject = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']


class HomeworkSbrExerciseWithoutPublishTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_sbrpaperfilter_principal(self):
        """
        title: 验证校长的学科年级返回
        url: /api/teacher/homework/sbrpaper/GetSbrPaperFilter
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.get_SbrPaperFilter()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(set(allgrade).issubset([item['key'] for item in res['data']['gradelist']]))
        self.assertTrue(set(allsubject).issubset([item['Name'] for item in res['data']['kemulist']]))

    def test_p1_get_sbrpaperfilter_grademaster(self):
        """
        title: 验证年级主任的学科年级返回（检查点同校长）
        url: /api/teacher/homework/sbrpaper/GetSbrPaperFilter
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_web.get_SbrPaperFilter()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(set(allgrade).issubset([item['key'] for item in res['data']['gradelist']]))
        self.assertTrue(set(allsubject).issubset([item['Name'] for item in res['data']['kemulist']]))

    def test_p1_get_sbrpaperfilter_headteacher(self):
        """
        title: 验证班主任的学科年级返回（检查点同校长）?班主任对应所有年级这个业务逻辑上有问题
        url: /api/teacher/homework/sbrpaper/GetSbrPaperFilter
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_web.get_SbrPaperFilter()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(set(allgrade).issubset([item['key'] for item in res['data']['gradelist']]))
        self.assertTrue(set(allsubject).issubset([item['Name'] for item in res['data']['kemulist']]))

    def test_p1_get_sbrpaperfilter_classheadteacher(self):
        """
        title: 验证教学班班主任的学科年级：返回对应学科，对应年级
        url: /api/teacher/homework/sbrpaper/GetSbrPaperFilter
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username'],
                                         password=classheadteacher_user['password']))
        res = teacher_web.get_SbrPaperFilter()
        print(res)
        self.assertEqual(200, res['code'])
        # 老接口弃用，暂时去掉以下断言
        # # 取出角色管理的年级
        # classmanagegrades = [item['text'] for item in teacher_web.classmanagegrades()['data']]
        # gradename = list(map(lambda x: re.findall(".*(?=\\()", x)[0], classmanagegrades))
        # gradename.append('全部')
        # # 为了防止有过期年份，取出交集(gradename&高一~高三)
        # gradelist1 = set(gradename).intersection(set(allgrade))
        # gradelist2 = set([item['key'] for item in res['data']['gradelist']])
        # self.assertEqual([], list(gradelist1 - gradelist2))
        # # 老接口弃用，暂时先去掉以下断言
        # subject = [item['subjectname'] for item in teacher_web.get_classlist()['data']['classlist']]
        # subject1 = set(subject)
        # subject2 = set([item['Name'] for item in res['data']['kemulist']])
        # self.assertEqual([], list(subject1 - subject2))
        self.assertEqual(['语文'], [item['Name'] for item in res['data']['kemulist']])
        self.assertTrue(len(res['data']['gradelist']) == 2)

    def test_p2_get_sbrpaperfilter_teacher(self):
        """
        title: 验证学科老师的学科年级：返回对应学科，对应年级
        url: /api/teacher/homework/sbrpaper/GetSbrPaperFilter
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_web.get_SbrPaperFilter()
        print(res)
        self.assertEqual(200, res['code'])
        # 老接口弃用，暂时去掉以下断言
        # 取出角色管理的年级
        # classmanagegrades = [item['text'] for item in teacher_web.classmanagegrades()['data']]
        # gradename = list(map(lambda x: re.findall(".*(?=\\()", x)[0], classmanagegrades))
        # gradename.append('全部')
        # # 为了防止有过期年份，取出交集(gradename&高一~高三)
        # gradelist1 = set(gradename).intersection(set(allgrade))
        # gradelist2 = set([item['key'] for item in res['data']['gradelist']])
        # self.assertEqual(200, res['code'])
        # self.assertEqual([], list(gradelist1 - gradelist2))
        self.assertEqual(['语文'], [item['Name'] for item in res['data']['kemulist']])
        self.assertTrue(len(res['data']['gradelist']) == 2)

    def test_p1_get_sbrpaper_g1_principal(self):
        """
        title: 获取校本试卷验证getSbrPaperPagingList接口，验证校长的语文&高一年级 条件下的返回
        url: /api/teacher/homework/sbrpaper/getSbrPaperPagingList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.get_SbrPaper(grades=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['datalist']) > 0)

    def test_p1_get_sbrpaper_all_teacher(self):
        """
        title: 获取校本试卷验证getSbrPaperPagingList接口，验证学科老师的 语文&全部年级 条件下的返回
        url: /api/teacher/homework/sbrpaper/getSbrPaperPagingList
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_web.get_SbrPaper()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['datalist']) > 0)

    def test_p2_get_classtype(self):
        """
        title: 获取布置窗口的班级类型
        url: /api/teacher/SelectOptions
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.classtypeoptions()
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(['行政班', '教学班'], [item['text'] for item in res['data']])


class HomeworkSbrExercisePublishTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_set_sbrpaperhomework__xingzheng_principal(self):
        """
        title: 校长布置行政班&年级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])
        return res['data']['homeworkid']

    def test_p1_set_sbrpaperhomework_jiaoxue_principal(self):
        """
        title: 校长布置教学班&年级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=2, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=paperids, title=title)
        print(res)
        self.assertEqual(200, res['code'])
        time.sleep(5)
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])
        return res['data']['homeworkid']

    def test_p1_set_sbrpaperhomework_xingzheng_grademaster(self):
        """
        title: 年级主任布置行政班&年级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])

    def test_p1_set_sbrpaperhomework_jiaoxue_grademaster(self):
        """
        title: 年级主任布置教学班&年级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=2, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])

    def test_p1_set_sbrpaperhomework_headteacher(self):
        """
        title: 班主任布置行政班&班级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[], grade=grade, expireyear=expireyear,
                                              classlist=[groupid_xingzheng], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=False, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])

    def test_p1_set_sbrpaperhomework_classheadteacher(self):
        """
        title: 教学班班主任布置教学班&班级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[], grade=grade, expireyear=expireyear,
                                              classlist=[groupid_jiaoxue], classtype=2, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=False, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])

    def test_p1_set_sbrpaperhomework_teacher(self):
        """
        title: 学科老师布置行政班&班级作业
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[], grade=grade, expireyear=expireyear,
                                              classlist=[groupid_xingzheng], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=False, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkrecordlist = teacher_web.get_homeworkrecord(type=8, HomeworkStatus=0)
        self.assertIn(res['data']['homeworkid'],
                      [item['homeworkid'] for item in homeworkrecordlist['data']['homeworklist']])


@unittest.skip
class HomeworkSbrExerciseSubmitAndReport(TestCaseV2):


    @classmethod
    def setUpClass(self):
        self.maxDiff = None
        print("# 初始化数据，先删除校本试卷作业旧数据， 再布置一个新的校本试卷作业")
        for i in teacher_user_list:
            teacher_web = teacher(web_client(username=teacher_user_list[i]['username'], password=teacher_user_list[i]['password']))
            res = teacher_web.get_homeworkrecord(HomeworkStatus=1, type=8, PageSize=40)
            homework_list = [h['homeworkid'] for h in res['data']['homeworklist'] if h['candelete'] and h['sourcehomeworktype'] == 7]
            if len(homework_list) > 0:
                teacher_web.deletehomework(homeworkids=homework_list)

        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=[sbr_paperid], title=title)
        self.homeworkid = res['data']['homeworkid']
        print(self.homeworkid)
        time.sleep(5)  # 等待作业分发
        # self.homeworkid = 335983
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def submit_sbr_paper(self, client1):
        # 单题提交客观题
        for i in syllabuses_expect:
            for j in i['details']:
                questionid = j['questionid']
                question_type = j['type']
                if question_type in [1, 2]:
                    data = {"answers": [{"answerindexes": [0], "questionId": questionid}],
                            "homeworkId": self.homeworkid,
                            "isFinalSubmit": False, "paperId": sbr_paperid, "timespend": 2000}
                    res = client1.sbr_submitQuestionAnswers(data=data)
                    print(res)
                    self.assertEqual(200, res['code'])
                    time.sleep(4)
        # 客观题交卷
        data = {"answers": [], "homeworkId": self.homeworkid, "isFinalSubmit": True, "paperId": sbr_paperid,
                "timespend": 2500}
        res = client1.sbr_submitQuestionAnswers(data=data)
        print(res)
        self.assertEqual(200, res['code'])
        # 校对主观题
        answers = []
        for i in syllabuses_expect:
            for j in i['details']:
                questionid = j['questionid']
                question_type = j['type']
                if question_type in [3, 4]:
                    answers.append({"score": 9.0, "questionId": questionid})
        # 校对完交卷
        data = {"answers": answers, "homeworkId": self.homeworkid, "isFinalSubmit": True, "paperId": sbr_paperid}
        time.sleep(4)
        res = client1.sbr_SubmitQuestionAnswerRating(data=data)
        print(res)
        self.assertEqual(200, res['code'])


    def test_p1_get_app_myhomework_new_version(self):
        """
        title: 非注册会员在app作业列表可以收到校本试卷作业
        url: /app/v1/homework/myhomework
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=1, tid=8, pagesize=40)
        print(res)
        self.assertTrue(res['code'] == 200)
        self.assertTrue(res['data']['list'][0]['homeworkid'] > 0)
        homeworkids = [i['homeworkid'] for i in res['data']['list']]
        self.assertIn(self.homeworkid, homeworkids)

    # @unittest.skip # 低版本app已做强制升级，不考虑了
    # def test_p1_get_app_myhomework_version_5_0_0(self):
    #     """
    #     title: 非注册会员在低版本的app作业列表不能收到校本试卷作业
    #     url: /app/v1/homework/myhomework
    #     author: 田彦涛
    #     """
    #     student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
    #     res = student_app.get_app_myhomework(status=1, tid=8, pagesize=40, version="5.0.0")
    #     print(res)
    #     self.assertTrue(res['code'] == 200)
    #     homeworkids = [i['homeworkid'] for i in res['data']['list']]
    #     self.assertNotIn(self.homeworkid, homeworkids)

    def test_p1_get_app_myhomework_version_type99(self):
        """
        title: 非注册会员在app作业列表可以收到校本试卷作业
        url: /app/v1/homework/myhomework
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student02_user['username'], password=student02_user['password']))
        res = student_app.get_app_myhomework(status=1, tid=8, pagesize=40)
        print(res)
        self.assertTrue(res['code'] == 200)
        self.assertTrue(res['data']['list'][0]['homeworkid'] > 0)
        homeworkids = [i['homeworkid'] for i in res['data']['list']]
        self.assertIn(self.homeworkid, homeworkids)

    def test_p1_get_app_homeworkinfo(self):
        """
        title: app校本试卷作业的/homework/info
        url: /app/v1/homework/info
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_homework_info(cid=groupid_xingzheng, hid=self.homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        self.assertEqual(8, res['data']['type'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['url'])

    def test_p1_get_app_getsbrpaperquestioncard(self):
        """
        title: app校本试卷作业答题卡获取
        url: /api/services/HomeworkService/homework/getSbrHomeworkInfo4Answer
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.sbr_getSbrHomeworkInfo4Answer(homeworkid=self.homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        print(res['data']['syllabuses'])
        self.assertEqual(syllabuses_expect, res['data']['syllabuses'])
        self.assertEqual(sbr_paperid, res['data']['paperid'])

    def test_p1_app_submit_sbr_homework(self):
        """
        title: app提交校本试卷
        url: /api/services/HomeworkService/homework/submitQuestionAnswers, /api/services/HomeworkService/homework/SubmitQuestionAnswerRating
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student03_user['username'], password=student03_user['password']))
        self.submit_sbr_paper(client1=student_app)

    def test_p1_web_homeworklist_sbr(self):
        """
        title: 验证web上非注册会员可以正常收到校本试卷作业
        url: /api/student/homework/homeworklist
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = student_web.get_homeworklist_student_pc(homeworktype=8, homeworkstatus=1, pagesize=40)
        print(res)
        self.assertTrue(res['code'] == 200)
        self.assertTrue(len(res['data']['list']) > 0)
        homeworkids = [i['homeworkid'] for i in res['data']['list']]
        self.assertIn(self.homeworkid, homeworkids)
        redirecturl = [i['redirecturl'] for i in res['data']['list'] if i['homeworkid'] == self.homeworkid][0]
        apphomeworkstatus = [i['apphomeworkstatus'] for i in res['data']['list'] if i['homeworkid'] == self.homeworkid][0]
        self.assertEqual("/ewtbend/bend/index/index.html#/student/answersheet?homeworkflag=1&homeworkId={}"
                         .format(self.homeworkid), redirecturl)
        self.assertEqual(1, apphomeworkstatus)

    def test_p1_get_sbrHomeworkInfo4SelfRating(self):
        """
        title: 获取答题卡主观题，客观题未作答时
        url: /api/services/HomeworkService/homework/GetSbrHomeworkInfo4SelfRating
        author: 田彦涛
        """
        student_app = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = student_app.sbr_GetSbrHomeworkInfo4SelfRating(homeworkid=self.homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['paperurl'])
        self.assertFalse(res['data']['analysisurl'])
        self.assertEqual(0, res['data']['progress'])
        self.assertEqual(0, res['data']['ratingstate'])
        # self.assertEqual(syllabuses_expect[2:], res['data']['syllabuses'])
        self.assertEqual(sbr_paperid, res['data']['paperid'])

    def test_p1_get_sbrHomeworkInfo4SelfRating_2(self):
        """
        title: 获取答题卡主观题，客观题已作答时
        url: /api/services/HomeworkService/homework/GetSbrHomeworkInfo4SelfRating
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student07_user['username'], password=student07_user['password']))
        # 单题提交客观题
        for i in syllabuses_expect:
            for j in i['details']:
                questionid = j['questionid']
                question_type = j['type']
                if question_type in [1, 2]:
                    data = {"answers": [{"answerindexes": [0], "questionId": questionid}],
                            "homeworkId": self.homeworkid,
                            "isFinalSubmit": False, "paperId": sbr_paperid, "timespend": 2000}
                    res = student_web.sbr_submitQuestionAnswers(data=data)
                    print(res)
                    self.assertEqual(200, res['code'])
                    time.sleep(1)
        # 客观题交卷
        data = {"answers": [], "homeworkId": self.homeworkid, "isFinalSubmit": True, "paperId": sbr_paperid,
                "timespend": 2500}
        res = student_web.sbr_submitQuestionAnswers(data=data)
        print(res)
        res = student_web.sbr_GetSbrHomeworkInfo4SelfRating(homeworkid=self.homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['paperurl'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['analysisurl'])
        self.assertEqual(2, res['data']['progress'])
        self.assertEqual(0, res['data']['ratingstate'])
        self.assertEqual(rating_expect, res['data']['syllabuses'])
        self.assertEqual(sbr_paperid, res['data']['paperid'])

    def test_p1_web_homeworklist_sbr_type99(self):
        """
        title: 验证web上注册会员可以正常收到校本试卷作业
        url: /api/student/homework/homeworklist
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student02_user['username'], password=student02_user['password']))
        res = student_web.get_homeworklist_student_pc(homeworktype=8, homeworkstatus=1, pagesize=40)
        print(res)
        self.assertTrue(res['code'] == 200)
        self.assertTrue(len(res['data']['list']) > 0)
        homeworkids = [i['homeworkid'] for i in res['data']['list']]
        self.assertIn(self.homeworkid, homeworkids)
        redirecturl = [i['redirecturl'] for i in res['data']['list'] if i['homeworkid'] == self.homeworkid][0]
        apphomeworkstatus = [i['apphomeworkstatus'] for i in res['data']['list'] if i['homeworkid'] == self.homeworkid][
            0]
        self.assertEqual("/ewtbend/bend/index/index.html#/student/answersheet?homeworkflag=1&homeworkId={}"
                         .format(self.homeworkid), redirecturl)
        self.assertEqual(1, apphomeworkstatus)

    def test_p1_web_get_SbrPaperExam(self):
        """
        title: web获取校本试卷作业详情
        url: /api/services/HomeworkService/homework/getSbrHomeworkInfo4Answer
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = student_web.sbr_getSbrHomeworkInfo4Answer(homeworkid=self.homeworkid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        print(res['data']['syllabuses'])
        self.assertEqual(syllabuses_expect, res['data']['syllabuses'])
        self.assertEqual(sbr_paperid, res['data']['paperid'])

    def test_p1_web_submit_sbr_homework(self):
        """
        title: web提交校本试卷
        url: /api/services/HomeworkService/homework/submitQuestionAnswers, /api/services/HomeworkService/homework/SubmitQuestionAnswerRating
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student04_user['username'], password=student04_user['password']))
        self.submit_sbr_paper(student_web)

    def test_p1_getreport_after_submit_sbr_homework(self):
        """
        title: 提交校本试卷后查看试卷报告
        url: /api/services/HomeworkService/homework/submitQuestionAnswers, /api/services/HomeworkService/homework/SubmitQuestionAnswerRating, /api/services/HomeworkService/homework/GetStudentSbrHomeworkReport
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student09_user['username'], password=student09_user['password']))
        student_app = teacher(app_client(username=student09_user['username'], password=student09_user['password']))
        self.submit_sbr_paper(student_web)
        time.sleep(3)
        res = student_web.sbr_GetStudentSbrHomeworkReport(homeworkid=self.homeworkid)
        res2 = student_app.sbr_GetStudentSbrHomeworkReport(homeworkid=self.homeworkid)
        print(res)
        print(res2)
        self.assertEqual(res, res2)
        self.assertEqual(200, res['code'])
        self.assertEqual(self.homeworkid, res['data']['homeworkid'])
        self.assertEqual(sbr_paperid, res['data']['paperid'])
        self.assertEqual(47, res['data']['score'])
        self.assertEqual(2, res['data']['progress'])
        self.assertEqual(2, res['data']['ratingstate'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['paperurl'])
        self.assertIn('{}://'.format(ConfigCase.PROTOCOL), res['data']['analysisurl'])
        print(res['data']['syllabuses'])
        print(report_expect)
        self.assertEqual(report_expect, res['data']['syllabuses'])

    def test_p1_appcontent_unclosed_homework(self):
        """
        title: 验证app首页调用的学生未截止的作业列表数据正常
        url: /api/services/HomeworkService/studentHomework/StudentUnClosedHomeworks
        author: 田彦涛
        """
        student_web = teacher(web_client(username=student04_user['username'], password=student04_user['password']))
        res = student_web.student_unclosed_homeworks(pagesize=100)
        print(res)
        self.assertTrue(res['data']['totalcnt'] > 0)
        # self.assertTrue(len(res['data']['records']) > 0)
        # homeworkids = [i['homeworkid'] for i in res['data']['records']]
        # self.assertIn(self.homeworkid, homeworkids)
        # self.assertEqual(8, [i['homeworktype'] for i in res['data']['records'] if i['homeworkid'] == self.homeworkid][0])
        # self.assertEqual(7, [i['sourcehomeworktype'] for i in res['data']['records'] if i['homeworkid'] == self.homeworkid][0])
        # # self.assertTrue([i['access'] for i in res['data']['records'] if i['homeworkid'] == self.homeworkid][0])


class MonitorHomework(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_my_homework(self):
        """
        title: 学生获取作业列表
        url: /app/v1/homework/myhomework
        author: 田彦涛
        """
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=0)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['list']) > 0)

    def test_publish_homework_and_get_count(self):
        """
        title: 作业分发稳定性测试-布置作业，获取作业分发人数
        url: /api/teacher/homework/sbrpaper/SetSbrPaperHomework, /api/services/HomeworkService/homework/GetHomeworkDetailInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        paperids = []
        paperids.append(teacher_web.get_SbrPaper()['data']['datalist'][0]['id'])
        title = "Sbr试卷{}".format(CaseServices.get_deadlinetime())
        res = teacher_web.setsbrpaperhomework(expireyears=[expireyear], grade=grade, expireyear=expireyear,
                                              classlist=[], classtype=1, deadline=CaseServices.get_deadlinetime(),
                                              iscgradehomework=True, kemu=1, paperids=paperids, title=title)
        print(res)
        time.sleep(5)
        self.assertEqual(200, res['code'])
        homeworkid = res['data']['homeworkid']
        res = teacher_web.get_homework_detail(homeworkId=homeworkid, schoolId=schoolid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(res['data']['homeworkstudents'] >= 30, "作业分发人数不足30")


@unittest.skip
class Test(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def get_answerCardId_and_paperId(self, homeworkid):
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.sbr_getSbrHomeworkInfo4Answer(homeworkid=homeworkid)
        answercardid = res['data']['answercardid']
        paperid = res['data']['paperid']
        return answercardid, paperid

    def test_SubmitSubjectiveFileUrls(self):
        """
        title: 提交校本试卷主观题图片
        url: /api/services/HomeworkService/homework/SubmitSubjectiveFileUrls
        author: 田彦涛
        """
        tmp = self.get_answerCardId_and_paperId(homeworkid=337437)
        answercardid = tmp[0]
        paperid = tmp[1]
        questionAnswers = [{"questionId": 1466, "fileUrls": ["study.ewt360.com/UpLoadFile/Course/2016/1/1452528392.jpg",
                                                             "static.test.mistong.com/pic/384961595233353728"]}]
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.sbr_SubmitSubjectiveFileUrls(answerCardId=answercardid, paperId=paperid, questionAnswers=questionAnswers)
        print(res)

