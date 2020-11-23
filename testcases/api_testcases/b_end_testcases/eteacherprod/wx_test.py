from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.testcases_data import *
from common.unittest_v2 import TestCaseV2
import unittest
from config.config_env import get_env


class ContentsTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_menuall(self):
        """
        title: 验证微信端的/menu/all（获取菜单）接口
        url: /api/eteacherproduct/menu/all
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        token = teacher_web.client.user_token
        res = teacher_web.menuall(token=token)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        self.assertTrue(len(res['data']) > 0)

    def test_p1_get_menuselect(self):
        """
        title: 验证微信端的/menu/select（设置教学进度）接口
        url: /api/eteacherproduct/menu/select
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.menuselect(menuId=menu_menuId, subjectId=menu_subjectId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])

    def test_p1_get_solutionlist_1(self):
        """
        title: 验证微信端的/solution/list（方案列表）接口,check点：非直连方式
        url: /api/eteacherproduct/solution/list
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.solutionlist(menuId=menu_menuId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        # 目录方式
        connectedMode1 = [s['connectedMode'] for s in res['data']['data'] if s['id'] == solutionid1]
        self.assertEqual(1, connectedMode1[0])

    @unittest.skipIf(get_env() == 'prod', '线上暂时跳过（无数据）')
    def test_p1_get_solutionlist_2(self):
        """
        title: 验证微信端的/solution/list（方案列表）接口,check点：直连方式
        url: /api/eteacherproduct/solution/list
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.solutionlist(menuId=menu_menuId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        # 专题直连方式
        connectedMode1 = [s['connectedMode'] for s in res['data']['data'] if s['id'] == solutionid2]
        self.assertEqual(2, connectedMode1[0])

    def test_p1_get_topicdetail(self):
        """
        title: 验证微信端的topicDetail（专题详情）接口,check点：返回url
        url: /api/eteacherproduct/solution/content/topicDetail
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.topicdetail(topicId=Id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        self.assertTrue(len(res['data']['h5url']) > 0)
        self.assertTrue(len(res['data']['pcurl']) > 0)

    @unittest.skipIf(get_env() == 'prod', '线上暂时跳过（数据不一致）')
    def test_p1_get_solutioncontent_test(self):
        """
        title: 验证微信端的contents（内容获取）接口,check点：视频、试卷、专题类型字段
        url: /api/eteacherproduct/solution/contents
        author: 吴丽燕
        """
        # 专题内容获取（验证视频、试卷、专题）
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.solutioncontent(solutionId=solutionid1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        self.assertEqual(1, res['data']['solution']['subList'][2]['content'][1]['contentType'])
        self.assertEqual(2, res['data']['solution']['subList'][2]['content'][0]['contentType'])
        self.assertEqual(3, res['data']['solution']['subList'][3]['content'][1]['contentType'])

    @unittest.skipIf(get_env() != 'prod', '线下暂时跳过（数据不一致）')
    def test_p1_get_solutioncontent_prod(self):
        """
        title: 验证微信端的contents（内容获取）接口,check点：视频、试卷类型字段
        url: /api/eteacherproduct/solution/contents
        author: 吴丽燕
        """
        # 专题内容获取（验证视频、试卷、专题）
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.solutioncontent(solutionId=solutionid1)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])
        self.assertEqual(1, res['data']['solution']['subList'][0]['content'][0]['contentType'])
        self.assertEqual(2, res['data']['solution']['subList'][8]['content'][0]['contentType'])

    def test_p1_get_solutionintroduce(self):
        """
        title: 验证微信端的introduce（内容介绍）接口
        url: /api/eteacherproduct/solution/introduce
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.solutionintroduce(solutionId=Id)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])

    def test_p1_get_papergetquestions(self):
        """
        title: 验证微信端的获取试卷题目接口
        url: /api/homeworkprod/resource/paper/getPaperInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.homeworkprod_getPaperInfo(paperId=paperId, schoolId=schoolid)
        print(res)
        self.assertEqual(res['code'], '200')
        self.assertTrue(len(res['data']['questionList']) > 0)
        self.assertTrue(len(res['data']['questionList'][0]['questionContent']) > 0)

    def test_p1_get_createpaper(self):
        """
        title: 验证微信端的组卷接口
        url: /api/paperlibrary/createpaper
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        questions = teacher_web.homeworkprod_getPaperInfo(paperId=paperId, schoolId=schoolid)
        selectedquestions = []
        selectedquestions.append(questions['data']['questionList'][0]['questionId'])
        selectedquestions.append(questions['data']['questionList'][1]['questionId'])
        post_data = {
            "questionIdList": selectedquestions, "subjectId": 1}
        res = teacher_web.homeworkprod_generatePaperByQuestionList(post_data)
        print(res)
        self.assertEqual(res['code'], '200')
        self.assertTrue(res['success'])
        self.assertTrue(res['data'])

    def test_p1_get_getclasseswithgradeinfo(self):
        """
        title: 验证获取班级接口，check：验证只能获取到行政班+对应学科的教学班，withSpecialTopic字段只是用于前端
        url: /api/services/HomeworkService/weChatHomework/GetClassesWithGradeInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.wxgetclasseswithgradeinfo(subjectId=assign_subjectId, withSpecialTopic="false")
        print(res)
        self.assertTrue(res['code'], 200)
        # 判断返回的是行政班+对应学科的教学班
        for grades in res['data']['grades']:
            for classes in grades['classes']:
                improvedsubject = [0, assign_subjectId]
                self.assertTrue(set([classes['subject']]).issubset(set(improvedsubject)))

    def test_p1_get_assign_gradehomework(self):
        """
        title: 验证年级立即布置视频1、试卷2、专题3作业
        url: /api/services/HomeworkService/weChatHomework/GetClassesWithGradeInfo, /api/eteacherproduct/homework/assignment
        author: 吴丽燕
        """
        # todo 最好通过学生的作业列表来check
        teacher_web = teacher(web_client(username=principal_user['username']))
        arrangeType = 0  # arrangeType立即布置：0；定时布置：1；
        classType = 1  # classType行政班：1；教学班：2
        components = []
        # 试卷信息
        components.append({"title": paper_title, "type": 2, "refIds": paper_refIds, "count": 0})
        # 多个视频作业
        components.append({"title": video_title, "type": 1, "refIds": video_refIds})
        # 专题作业
        components.append({"title": topic_title, "type": 3, "refIds": topic_refIds, "count": 0})
        classinfo = teacher_web.wxgetclasseswithgradeinfo(subjectId=assign_subjectId, withSpecialTopic="false")
        expireYear = classinfo['data']['grades'][0]['classes'][0]['gradeyear']
        classList = classinfo['data']['grades'][0]['classes'][0]['classid']
        isGradeHomework = True
        gradeClasses = []
        currentClass = classinfo['data']['grades'][0]['classes'][0]
        expireYears = [expireYear]
        selectedClass = []
        subject = menu_subjectId
        solutionId = str(solutionid1)
        usetimes = 200
        startTime = int(round(time.time() * 1000))  # 当前时间
        deadline = startTime + 86400000
        res = teacher_web.homeworkassign(arrangeType, classType, components, isGradeHomework, gradeClasses,
                                         currentClass, expireYears, selectedClass, subject, solutionId, usetimes,
                                         startTime, deadline)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])

    def test_p1_get_assign_classhomework_arrangeType0(self):
        """
        title: 验证年级立即布置视频1、试卷2、专题3作业
        url: /api/services/HomeworkService/weChatHomework/GetClassesWithGradeInfo, /api/eteacherproduct/homework/assignment
        author: 吴丽燕
        """
        # todo 最好通过学生的作业列表来check
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        arrangeType = 0  # arrangeType立即布置：0；定时布置：1；
        classType = 1  # classType行政班：1；教学班：2
        components = []
        # 试卷信息
        components.append({"title": paper_title, "type": 2, "refIds": paper_refIds, "count": 0})
        # 多个视频作业
        components.append({"title": video_title, "type": 1, "refIds": video_refIds})
        # 专题作业
        components.append({"title": topic_title, "type": 3, "refIds": topic_refIds, "count": 0})
        classinfo = teacher_web.wxgetclasseswithgradeinfo(subjectId=assign_subjectId, withSpecialTopic="false")
        expireYear = classinfo['data']['grades'][0]['classes'][0]['gradeyear']
        classList = classinfo['data']['grades'][0]['classes'][0]['classid']
        isGradeHomework = False
        gradeClasses = [{"expireYear": expireYear, "classList": [classList]}]
        currentClass = classinfo['data']['grades'][0]['classes'][0]
        expireYears = []
        selectedClass = []
        subject = menu_subjectId
        solutionId = str(solutionid1)
        usetimes = 200
        startTime = int(round(time.time() * 1000))  # 当前时间
        deadline = startTime + 86400000
        res = teacher_web.homeworkassign(arrangeType, classType, components, isGradeHomework, gradeClasses,
                                         currentClass, expireYears, selectedClass, subject, solutionId, usetimes,
                                         startTime, deadline)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])

    def test_p1_get_assign_classhomework_arrangeType1(self):
        """
        title: 验证班级定时布置视频1、试卷2、专题3作业
        url: /api/services/HomeworkService/weChatHomework/GetClassesWithGradeInfo, /api/eteacherproduct/homework/assignment
        author: 吴丽燕
        """
        # todo 最好通过教师的作业列表来check
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        arrangeType = 1  # arrangeType立即布置：0；定时布置：1；
        classType = 1  # classType行政班：1；教学班：2
        components = []
        # 试卷信息
        components.append({"title": paper_title, "type": 2, "refIds": paper_refIds, "count": 0})
        # 多个视频作业
        components.append({"title": video_title, "type": 1, "refIds": video_refIds})
        # 专题作业
        components.append({"title": topic_title, "type": 3, "refIds": topic_refIds, "count": 0})
        classinfo = teacher_web.wxgetclasseswithgradeinfo(subjectId=assign_subjectId, withSpecialTopic="false")
        expireYear = classinfo['data']['grades'][0]['classes'][0]['gradeyear']
        classList = classinfo['data']['grades'][0]['classes'][0]['classid']
        isGradeHomework = False
        gradeClasses = [{"expireYear": expireYear, "classList": [classList]}]
        currentClass = classinfo['data']['grades'][0]['classes'][0]
        expireYears = []
        selectedClass = []
        subject = menu_subjectId
        solutionId = str(solutionid1)
        usetimes = 200
        startTime = int(round(time.time() * 1000) + 43200000)  # 当前时间+12h
        deadline = startTime + 86400000
        res = teacher_web.homeworkassign(arrangeType, classType, components, isGradeHomework, gradeClasses,
                                         currentClass, expireYears, selectedClass, subject, solutionId, usetimes,
                                         startTime, deadline)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual("操作成功", res['msg'])

    # def test_p1_get_fetchuserinfo(self):
    #     """
    #     title: 验证获取用户个人、学校信息
    #     url: /api/eteacherproduct/my/fetchuserinfo
    #     author: 吴丽燕
    #     """
    #     teacher_web = teacher(web_client(username=headteacher_user['username']))
    #     token = teacher_web.client.user_token
    #     res = teacher_web.fetchuserinfo(token=token)
    #     print(res)
    #     self.assertEqual("200", res['code'])
    #     self.assertEqual("操作成功", res['msg'])
    #     # self.assertEqual(headteacher_user['username'], res['data']['mobile'])
    #     self.assertIsNotNone(res['data']['mobile'])
    #     self.assertEqual(schoolid, res['data']['schoolid'])

#     @unittest.skip("接口弃用")
#     def test_p1_get_myclasslist_principal(self):
#         """
#         title: 验证校长&心理老师获取学科及班级信息
#         url: /api/eteacherproduct/my/classlist
#         author: 吴丽燕
#         """
#         # todo 最好可以和其他的获取班级信息的接口进行数据一起校验
#         principal_web = teacher(web_client(username=principal_user['username']))
#         res_principal = principal_web.myclasslist()
#         psychologicalteacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
#         res_psychologicalteacher = psychologicalteacher_web.myclasslist()
#         print(res_principal)
#         self.assertEqual("200", res_principal['code'])
#         self.assertEqual("操作成功", res_principal['msg'])
#         self.assertEqual([], res_principal['data']['subjects'])
#         self.assertEqual({"id": 1, "name": "行政班"}, res_principal['data']['classtypes'][0])
#         self.assertEqual({"id": 2, "name": "教学班"}, res_principal['data']['classtypes'][1])
#         self.assertTrue(len(res_principal['data']['gradeclasses']) >= 1)
#         self.assertEqual(res_psychologicalteacher['data'], res_principal['data'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_myclasslist_headteacher(self):
#         """
#         title: 验证班主任获取学科及班级信息
#         url: /api/eteacherproduct/my/classlist
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=headteacher_user['username']))
#         res = teacher_web.myclasslist()
#         print(res)
#         self.assertEqual("200", res['code'])
#         self.assertEqual("操作成功", res['msg'])
#         self.assertEqual([], res['data']['subjects'])
#         self.assertTrue(len(res['data']['classtypes']) == 1)
#         self.assertEqual({"id": 1, "name": "行政班"}, res['data']['classtypes'][0])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_myclasslist_classheadteacher(self):
#         """
#         title: 验证教学班班主任获取学科及班级信息
#         url: /api/eteacherproduct/my/classlist
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=classheadteacher_user['username']))
#         res = teacher_web.myclasslist()
#         print(res)
#         self.assertEqual("200", res['code'])
#         self.assertEqual("操作成功", res['msg'])
#         self.assertIsNotNone(res['data']['subjects'])
#         self.assertTrue(len(res['data']['subjects']) >= 1)
#         self.assertTrue(len(res['data']['classtypes']) == 1)
#         self.assertEqual({"id": 2, "name": "教学班"}, res['data']['classtypes'][0])
#
#
# class UserRoleTest(TestCaseV2):
#
#     @classmethod
#     def setUpClass(cls):
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         pass
#
#     def test_p1_get_userrole_principal(self):
#         """
#         title: 验证校长获取角色信息GetUserRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(0, res['data']['role'])  # 0是校长，只要验证这级就好了，因为其他班级层数据容易变动，易导致case失败
#         self.assertEqual(0, res['data']['internalrole'])  # 该字段是排除教学班后的角色，为了支持微信端而增加
#
#     def test_p1_get_user_manager_role_principal(self):
#         """
#         title: 验证校长获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(0, res['data']['role'])
#         self.assertEqual(0, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_principal(self):
#         """
#         title: 验证校长获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=principal_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(0, res['data']['role'])
#         self.assertEqual(0, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     def test_p1_get_userrole_psychologicalteacher(self):
#         """
#         title: 验证心理老师获取角色信息
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(6, res['data']['role'])
#         self.assertEqual(6, res['data']['internalrole'])
#
#     def test_p1_get_user_manager_role_psychologicalteacher(self):
#         """
#         title: 验证心理老师获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])  # 只支持校长和年级主任
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_psychologicalteacher(self):
#         """
#         title: 验证心理老师获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])  # 只支持校长和年级主任
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_userrole_grademaster(self):
#         """
#         title: 验证年级主任获取角色信息
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=grademaster_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(4, res['data']['role'])
#         self.assertEqual(4, res['data']['internalrole'])
#         self.assertEqual(4, res['data']['grades'][0]['role'])
#         self.assertEqual(4, res['data']['grades'][0]['internalrole'])
#
#     def test_p1_get_user_manager_role_grademaster(self):
#         """
#         title: 验证年级主任获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=grademaster_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(4, res['data']['role'])
#         self.assertEqual(4, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(4, res['data']['grades'][0]['role'])
#         self.assertEqual(expireyear, res['data']['grades'][0]['gradeyear'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_grademaster(self):
#         """
#         title: 验证年级主任获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=grademaster_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(4, res['data']['role'])
#         self.assertEqual(4, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(4, res['data']['grades'][0]['role'])
#         self.assertEqual(expireyear, res['data']['grades'][0]['gradeyear'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_userrole_headteacher(self):
#         """
#         title: 验证（行政班）班主任获取角色信息
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=headteacher_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(5, res['data']['role'])
#         self.assertEqual(5, res['data']['internalrole'])
#         self.assertEqual(5, res['data']['grades'][0]['role'])
#         self.assertEqual(5, res['data']['grades'][0]['internalrole'])
#         self.assertEqual(1, res['data']['grades'][0]['classes'][0]['role'])
#
#     def test_p1_get_user_manager_role_headteacher(self):
#         """
#         title: 验证班主任获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=headteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_headteacher(self):
#         """
#         title: 验证班主任获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=headteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(5, res['data']['grades'][0]['role'])
#         self.assertEqual(expireyear, res['data']['grades'][0]['gradeyear'])
#         self.assertEqual(groupid_xingzheng, res['data']['grades'][0]['classes'][0]['groupid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_userrole_classheadteacher(self):
#         """
#         title: 验证教学班班主任获取角色信息
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=classheadteacher_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(5, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(5, res['data']['grades'][0]['role'])
#         self.assertEqual(-1, res['data']['grades'][0]['internalrole'])
#         self.assertEqual(1, res['data']['grades'][0]['classes'][0]['role'])
#
#     def test_p1_get_user_manager_role_classheadteacher(self):
#         """
#         title: 验证教学班班主任获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=classheadteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_classheadteacher(self):
#         """
#         title: 验证教学班班主任获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=classheadteacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(5, res['data']['grades'][0]['role'])
#         self.assertEqual(expireyear, res['data']['grades'][0]['gradeyear'])
#         self.assertEqual(groupid_jiaoxue, res['data']['grades'][0]['classes'][0]['groupid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_userrole_teacher(self):
#         """
#         title: 验证学科老师获取角色信息
#         url: /api/services/EduOrgan/schoolStaff/GetUserRole
#         author: 吴丽燕
#         """
#         teacher_web = teacher(web_client(username=teacher_user['username']))
#         token = teacher_web.client.user_token
#         res = teacher_web.getuserrole(ettoken=token)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(-1, res['data']['grades'][0]['role'])
#         self.assertEqual(-1, res['data']['grades'][0]['internalrole'])
#         self.assertTrue(res['data']['grades'][0]['classes'][0]['role'] % 2 == 0)
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_role_teacher(self):
#         """
#         title: 验证学科老师获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=teacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_teacher(self):
#         """
#         title: 验证学科老师获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=teacher_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(-1, res['data']['role'])
#         self.assertEqual(-1, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(-1, res['data']['grades'][0]['role'])
#         self.assertEqual(expireyear, res['data']['grades'][0]['gradeyear'])
#         self.assertEqual(groupid_xingzheng, res['data']['grades'][0]['classes'][0]['groupid'])
#
#     def test_p1_get_user_manager_role_mixteacher(self):
#         """
#         title: 验证混合角色获取角色信息GetUserManagerRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=teacher_mix_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(0, res['data']['role'])
#         self.assertEqual(0, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#
#     @unittest.skip("接口弃用")
#     def test_p1_get_user_manager_and_class_role_mixteacher(self):
#         """
#         title: 验证混合角色老师获取角色信息GetUserManagerAndClassRole
#         url: /api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole
#         author: 田彦涛
#         """
#         teacher_web = teacher(web_client(username=teacher_mix_user['username']))
#         userid = teacher_web.client.user_id
#         res = teacher_web.get_user_manager_and_class_role(userid=userid)
#         print(res)
#         self.assertEqual(200, res['code'])
#         self.assertEqual("执行成功", res['msg'])
#         self.assertEqual(0, res['data']['role'])
#         self.assertEqual(0, res['data']['internalrole'])
#         self.assertEqual(schoolid, res['data']['schoolid'])
#         self.assertEqual(5, res['data']['grades'][0]['role'])
