from common.unittest_v2 import TestCaseV2
import unittest
from testcases.api_testcases.b_end_testcases.eteacherprod.plan_homework_data import *
from testcases.api_testcases.b_end_testcases.schooluser_data import *


def scenes_id():
    """
    获取场景
    """
    teacher_principal = teacher(
        web_client(username=principal_user['username'], password=principal_user['password']))
    res = teacher_principal.getSchoolUserInfo()
    userId = res['data']['userId']
    schoolId = res['data']['schoolId']
    userhomeworkscenes = teacher_principal.getuserhomeworkscenes(userId=userId, schoolId=schoolId)
    scene_num = len(userhomeworkscenes['data'])
    if scene_num > 0:
        scene_id = userhomeworkscenes['data'][0]['id']
    else:
        scene_id = 0
    return scene_id


@unittest.skipIf(scenes_id() == 0, '无有效场景，跳过')
class PlanHomeworkTeacher(TestCaseV2):
    globals()['firstsceneid'] = scenes_id()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_user_homeworkscenes(self):
        """
        title: 获取用户的场景
        url: /api/eteacherproduct/scene/getUserHomeworkScenes
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.getSchoolUserInfo()
        userId = res['data']['userId']
        schoolId = res['data']['schoolId']
        userhomeworkscenes = teacher_web.getuserhomeworkscenes(userId=userId, schoolId=schoolId)
        print(userhomeworkscenes)
        self.assertEqual("200", userhomeworkscenes['code'])
        self.assertTrue(userhomeworkscenes['data'][0]['id'])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_get_scenesinfo(self):
        """
        title: 获取场景信息
        url: /api/eteacherproduct/scene/getHomeworkScene
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        sceneinfo = teacher_web.gethomeworksceneinfo(sceneId=globals()['firstsceneid'])
        print(sceneinfo)
        self.assertEqual("200", sceneinfo['code'])
        self.assertTrue(sceneinfo['data']['status'] == 2)
        self.assertTrue(sceneinfo['data']['name'])
        self.assertTrue(sceneinfo['data']['title'])

    def test_p1_get_defaultsubject(self):
        """
        title: 获取场景信息
        url: /api/eteacherproduct/scene/getDefaultSubject
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        defaultsubject = teacher_web.getDefaultSubject()
        print(defaultsubject)
        self.assertEqual("200", defaultsubject['code'])
        self.assertTrue(defaultsubject['data'] == 1)

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_VIDEO(self):
        """
        title: 添加学科视频到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_VIDEO['resourceType'],
                                                       resourceId=resourceId_VIDEO['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_VIDEO['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_VIDEO['id'][0], BasketItems_Add['data'][str(resourceId_VIDEO['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_VIDEO['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_EXAM_PAPER(self):
        """
        title: 添加学科试卷到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_EXAM_PAPER['resourceType'],
                                                       resourceId=resourceId_EXAM_PAPER['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_EXAM_PAPER['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_EXAM_PAPER['id'][0],
                      BasketItems_Add['data'][str(resourceId_EXAM_PAPER['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_EXAM_PAPER['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_XB_VIDEO(self):
        """
        title: 添加校本视频到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_XB_VIDEO['resourceType'],
                                                       resourceId=resourceId_XB_VIDEO['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_XB_VIDEO['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_XB_VIDEO['id'][0],
                      BasketItems_Add['data'][str(resourceId_XB_VIDEO['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_XB_VIDEO['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_XB_PAPER(self):
        """
        title: 添加校本试卷到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_XB_PAPER['resourceType'],
                                                       resourceId=resourceId_XB_PAPER['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_XB_PAPER['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_XB_PAPER['id'][0],
                      BasketItems_Add['data'][str(resourceId_XB_PAPER['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_XB_PAPER['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_FM(self):
        """
        title: 添加FM到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_FM['resourceType'],
                                                       resourceId=resourceId_FM['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_FM['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_FM['id'][0],
                      BasketItems_Add['data'][str(resourceId_FM['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_FM['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_CAREER_NEWS(self):
        """
        title: 添加资讯到作业篮
        url:/api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_CAREER_NEWS['resourceType'],
                                                       resourceId=resourceId_CAREER_NEWS['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_CAREER_NEWS['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_CAREER_NEWS['id'][0],
                      BasketItems_Add['data'][str(resourceId_CAREER_NEWS['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_CAREER_NEWS['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_SYCHOLOGY_REPORT(self):
        """
        title: 添加板报到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_SYCHOLOGY_REPORT['resourceType'],
                                                       resourceId=resourceId_SYCHOLOGY_REPORT['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_SYCHOLOGY_REPORT['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_SYCHOLOGY_REPORT['id'][0],
                      BasketItems_Add['data'][str(resourceId_SYCHOLOGY_REPORT['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_SYCHOLOGY_REPORT['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_FUN_TEST(self):
        """
        title: 添加测评到作业篮
        url: /api/eteacherproduct/basket/addBasketContent,/api/eteacherproduct/basket/listBigHomeworkItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Add = teacher_web.addBasketContent(resourceType=resourceId_FUN_TEST['resourceType'],
                                                       resourceId=resourceId_FUN_TEST['id'],
                                                       sceneId=globals()['firstsceneid'],
                                                       category=resourceId_FUN_TEST['category'])
        print(BasketItems_Add)
        self.assertEqual("200", BasketItems_Add['code'])
        self.assertIn(resourceId_FUN_TEST['id'][0],
                      BasketItems_Add['data'][str(resourceId_FUN_TEST['resourceType'])])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        self.assertIn(resourceId_FUN_TEST['id'][0], [item['resourceId'] for item in BasketItems_Items['data']])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_remove(self):
        """
        title: 从作业篮中移除资源
        url: /api/eteacherproduct/basket/removeBasketContent
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items_before = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        if len(BasketItems_Items_before['data']) == 0:
            teacher_web.addBasketContent(resourceType=resourceId_VIDEO['resourceType'],
                                         resourceId=resourceId_VIDEO['id'], sceneId=globals()['firstsceneid'],
                                         category=resourceId_VIDEO['category'])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        remove = teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        print(remove)
        self.assertEqual("200", remove['code'])
        Basket_summary = teacher_web.listBigHomeworkSummary(sceneId=globals()['firstsceneid'])
        self.assertEqual("200", Basket_summary['code'])
        self.assertEqual([], Basket_summary['data'])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_basketcontent_summary(self):
        """
        title: 获取大作业作业篮概览
        url: /api/eteacherproduct/basket/listBigHomeworkSummary
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        teacher_web.addBasketContent(resourceType=resourceId_XB_PAPER['resourceType'],
                                     resourceId=resourceId_XB_PAPER['id'],
                                     sceneId=globals()['firstsceneid'],
                                     category=resourceId_XB_PAPER['category'])
        Basket_summary = teacher_web.listBigHomeworkSummary(sceneId=globals()['firstsceneid'])
        print(Basket_summary)
        self.assertEqual("200", Basket_summary['code'])
        self.assertTrue(len(Basket_summary['data']) == 1)
        self.assertEqual(resourceId_XB_PAPER['category'], Basket_summary['data'][0]['subjectId'])
        self.assertEqual(resourceId_XB_PAPER['id'], [Basket_summary['data'][0]['items'][0]['resourceId']])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_saveassigncontents(self):
        """
        title: 作业篮资源圈定
        url: /api/eteacherproduct/scene/saveAssignContents,/api/eteacherproduct/scene/getAssignData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        teacher_web.addBasketContent(resourceType=resourceId_XB_PAPER['resourceType'],
                                     resourceId=resourceId_XB_PAPER['id'],
                                     sceneId=globals()['firstsceneid'],
                                     category=resourceId_XB_PAPER['category'])
        contents = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0]
        contents['checked'] = True
        saveAssignContents = teacher_web.saveAssignContents(sceneId=globals()['firstsceneid'], contents=contents)
        self.assertEqual("200", saveAssignContents['code'])
        self.assertEqual("操作成功", saveAssignContents['msg'])
        getAssignData = teacher_web.getAssignData(sceneId=globals()['firstsceneid'], schoolId=schoolid)
        print(getAssignData)
        self.assertEqual("200", getAssignData['code'])
        self.assertTrue(len(getAssignData['data']['resources']) > 0)

    def test_p1_saveassigncontents_principal(self):
        """
        title: 获取老师管辖范围内班级_校长
        url: /api/eteacherproduct/teacher/manage/queryTeacherClasses
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        userid = int(teacher_web.client.user_id)
        res = teacher_web.queryTeacherClasses(userId=userid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']['gradeClasses']) >= 3)
        for i in res['data']['gradeClasses']:
            self.assertTrue(i['isGradeLeader'])

    def test_p1_saveassigncontents_headteacher(self):
        """
        title: 获取老师管辖范围内班级_行政班班主任
        url: /api/eteacherproduct/teacher/manage/queryTeacherClasses
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        userid = int(teacher_web.client.user_id)
        res = teacher_web.queryTeacherClasses(userId=userid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']['gradeClasses']) == 1)
        for i in res['data']['gradeClasses']:
            self.assertFalse(i['isGradeLeader'])
        self.assertIn(groupid_xingzheng,
                      [item['classInfoList'][0]['classId'] for item in res['data']['gradeClasses']])

    def test_p1_saveassigncontents_classheadteacher(self):
        """
        title: 获取老师管辖范围内班级_教学班班主任
        url: /api/eteacherproduct/teacher/manage/queryTeacherClasses
        author: 吴丽燕
        """
        teacher_web = teacher(
            web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        userid = int(teacher_web.client.user_id)
        TeacherClasses = teacher_web.queryTeacherClasses(userId=userid)
        print(TeacherClasses)
        self.assertEqual("200", TeacherClasses['code'])
        self.assertTrue(len(TeacherClasses['data']['gradeClasses']) == 1)
        for i in TeacherClasses['data']['gradeClasses']:
            self.assertFalse(i['isGradeLeader'])
        self.assertIn(groupid_jiaoxue,
                      [item['classInfoList'][0]['classId'] for item in TeacherClasses['data']['gradeClasses']])

    def test_p1_saveassigncontents_teacher(self):
        """
        title: 获取老师管辖范围内班级_学科老师
        url: /api/eteacherproduct/teacher/manage/queryTeacherClasses
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username'], password=teacher_user['password']))
        userid = int(teacher_web.client.user_id)
        TeacherClasses = teacher_web.queryTeacherClasses(userId=userid)
        print(TeacherClasses)
        self.assertEqual("200", TeacherClasses['code'])
        self.assertTrue(len(TeacherClasses['data']['gradeClasses']) == 1)
        for i in TeacherClasses['data']['gradeClasses']:
            self.assertFalse(i['isGradeLeader'])
        self.assertTrue(
            len([item['classInfoList'][0]['classId'] for item in TeacherClasses['data']['gradeClasses']]) > 0)
        self.assertTrue(len(TeacherClasses['data']['subjects']) > 0)

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_makestudyplan(self):
        """
        title: 获取系统排课结果、布置
        url: /api/eteacherproduct/scene/makeStudyPlan,/api/eteacherproduct/scene/assignHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        userid = int(teacher_web.client.user_id)
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        teacher_web.addBasketContent(resourceType=resourceId_XB_PAPER['resourceType'],
                                     resourceId=resourceId_XB_PAPER['id'],
                                     sceneId=globals()['firstsceneid'],
                                     category=resourceId_XB_PAPER['category'])
        contents = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0]
        contents['checked'] = True
        teacher_web.saveAssignContents(sceneId=globals()['firstsceneid'], contents=contents)
        getAssignData = teacher_web.getAssignData(sceneId=globals()['firstsceneid'], schoolId=schoolid)
        theresource = getAssignData['data']['resources']
        today = time.strftime("%Y-%m-%d", time.localtime())
        makeStudyPlan = teacher_web.makeStudyPlan(sceneId=globals()['firstsceneid'], schoolId=schoolid, startTime=today,
                                                  endTime=today, restDates=[], resources=theresource)
        print(makeStudyPlan)
        self.assertEqual("200", makeStudyPlan['code'])
        self.assertTrue(len(makeStudyPlan['data']) == 1)
        assignresource = makeStudyPlan['data']
        userId = teacher_web.client.user_id
        res = teacher_web.manageteacher_queryTeacherRoleAndSchoolInfo(userId=userId)
        teacherId = res['data']['userId']
        teacherName = res['data']['userName']
        TeacherClasses = teacher_web.queryTeacherClasses(userId=userid)
        classexpireyear = TeacherClasses['data']['gradeClasses'][-1]['graduationYear']
        classlist = [TeacherClasses['data']['gradeClasses'][-1]['classInfoList'][0]['classId']]  # todo 最好布置到那个行政班
        classes = []
        classes.append({"expireYear": expireyear, "allClass": 1, "classList": []})
        classes.append({"expireYear": classexpireyear, "allClass": 0, "classList": classlist})
        assignHomework = teacher_web.assignHomework(sceneId=globals()['firstsceneid'], schoolId=schoolid,
                                                    teacherId=teacherId, teacherName=teacherName, title="测试plan作业",
                                                    resources=assignresource, classType=1, classes=classes)
        print(assignHomework)
        self.assertEqual("200", assignHomework['code'])
        self.assertTrue(len(assignHomework['data']) == 2)

    def test_p1_revokeHomework(self):
        """
        title: 计划性作业撤回
        url: /api/eteacherproduct/scene/revokeHomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_web.get_homeworkrecord(HomeworkStatus=1, type=13, PageSize=40)
        homework_list = [h['homeworkid'] for h in res['data']['homeworklist'] if h['homeworktypename'] == "学习计划"]
        res_revokeHomework = teacher_web.revokeHomework(homeworkId=homework_list[0])
        print(res_revokeHomework)
        self.assertEqual("200", res_revokeHomework['code'])
        self.assertEqual("操作成功", res_revokeHomework['msg'])

    def test_p1_get_SceneHomeworks(self):
        """
        title: 学生大作业列表
        url: /api/eteacherproduct/scene/getSceneHomeworks
        author: 吴丽燕
        """
        student_web = teacher(web_client(username=student02_user['username'], password=student02_user['password']))
        SceneHomeworks = student_web.getSceneHomeworks()
        print(SceneHomeworks)
        self.assertEqual("200", SceneHomeworks['code'])
        self.assertTrue(SceneHomeworks['data'][0]['detailUrl'])
        self.assertTrue(len(SceneHomeworks['data'][0]['subjects']) > 0)
        self.assertTrue(SceneHomeworks['data'][0]['totalCount'] > 0)

    def test_p1_get_SceneStatInfo_01(self):
        """
        title: 学生端大作业详情接口（teacher域名）
        url: /api/eteacherproduct/scene/getSceneStatInfo
        author: 吴丽燕
        """
        # todo 最好可以根据各类型作业进行断言
        student_web = teacher(web_client(username=student02_user['username'], password=student02_user['password']))
        SceneStatInfo = student_web.getSceneStatInfo(sceneId=globals()['firstsceneid'])
        print(SceneStatInfo)
        self.assertEqual("200", SceneStatInfo['code'])
        self.assertTrue(SceneStatInfo['data']['totalCount'] > 0)
        self.assertTrue(len(SceneStatInfo['data']['assignList']) > 0)
        self.assertTrue(len(SceneStatInfo['data']['contents']) > 0)
        self.assertTrue(len(SceneStatInfo['data']['contents'][0]['contents']) > 0)

    def test_p1_get_SceneStatInfo_02(self):
        """
        title: 学生端大作业详情接口（wx域名）
        url: /api/eteacherproduct/scene/getSceneStatInfo
        author: 吴丽燕
        """
        # todo 最好可以根据各类型作业进行断言
        student_web = teacher(web_client(username=student02_user['username'], password=student02_user['password']))
        SceneStatInfo = student_web.getSceneStatInfo_wx(sceneId=globals()['firstsceneid'])
        print(SceneStatInfo)
        self.assertEqual("200", SceneStatInfo['code'])
        self.assertTrue(SceneStatInfo['data']['totalCount'] > 0)
        self.assertTrue(len(SceneStatInfo['data']['assignList']) > 0)
        self.assertTrue(len(SceneStatInfo['data']['contents']) > 0)
        self.assertTrue(len(SceneStatInfo['data']['contents'][0]['contents']) > 0)

    @unittest.skipIf(get_env() == 'test', '线下环境跳过')
    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_addBasketItems(self):
        """
        title: 批量添加资源信息到作业篮(for专题用)
        url: /api/eteacherproduct/scene/addBasketItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        contents = []
        contents.append({"contentType": resourceId_VIDEO['resourceType'], "contentId": resourceId_VIDEO['id'][0],
                         "subject": resourceId_VIDEO['category']})
        contents.append(
            {"contentType": resourceId_EXAM_PAPER['resourceType'], "contentId": resourceId_EXAM_PAPER['id'][0],
             "subject": resourceId_EXAM_PAPER['category']})
        contents.append({"contentType": resourceId_XB_VIDEO['resourceType'], "contentId": resourceId_XB_VIDEO['id'][0],
                         "subject": resourceId_XB_VIDEO['category']})
        contents.append({"contentType": resourceId_XB_PAPER['resourceType'], "contentId": resourceId_XB_PAPER['id'][0],
                         "subject": resourceId_XB_PAPER['category']})
        contents.append({"contentType": resourceId_FM['resourceType'], "contentId": resourceId_FM['id'][0],
                         "subject": resourceId_FM['category']})
        contents.append(
            {"contentType": resourceId_CAREER_NEWS['resourceType'], "contentId": resourceId_CAREER_NEWS['id'][0],
             "subject": resourceId_CAREER_NEWS['category']})
        contents.append({"contentType": resourceId_SYCHOLOGY_REPORT['resourceType'],
                         "contentId": resourceId_SYCHOLOGY_REPORT['id'][0],
                         "subject": resourceId_SYCHOLOGY_REPORT['category']})
        contents.append({"contentType": resourceId_FUN_TEST['resourceType'], "contentId": resourceId_FUN_TEST['id'][0],
                         "subject": resourceId_FUN_TEST['category']})
        addBasketItems = teacher_web.addBasketItems(contents=contents, sceneId=globals()['firstsceneid'])
        print(addBasketItems)
        self.assertEqual("200", addBasketItems['code'])
        self.assertTrue(len(addBasketItems['data']) == 8)
        self.assertIn(resourceId_VIDEO['id'][0], [item['contentId'] for item in addBasketItems['data']])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_addBasketItems(self):
        """
        title: 批量移除作业篮资源信息(for专题用)
        url: /api/eteacherproduct/scene/removeBasketItems
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items_before = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        if len(BasketItems_Items_before['data']) == 0:
            contents = []
            contents.append({"contentType": resourceId_VIDEO['resourceType'], "contentId": resourceId_VIDEO['id'][0],
                             "subject": resourceId_VIDEO['category']})
            teacher_web.addBasketItems(contents=contents, sceneId=globals()['firstsceneid'])
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        contents_remove = [{"contentId": item['resourceId'], "contentType": item['resourceType']} for item in
                           BasketItems_Items['data']]
        remove = teacher_web.removeBasketItems(sceneId=globals()['firstsceneid'], contents=contents_remove)
        print(remove)
        self.assertEqual("200", remove['code'])
        Basket_summary = teacher_web.listBigHomeworkSummary(sceneId=globals()['firstsceneid'])
        self.assertEqual("200", Basket_summary['code'])
        self.assertEqual([], Basket_summary['data'])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_getBasketInfo(self):
        """
        title: 暑期作业篮信息读取(for专题用)
        url: /api/eteacherproduct/scene/getBasketInfo
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketInfo = teacher_web.getBasketInfo(sceneId=globals()['firstsceneid'])
        print(BasketInfo)
        self.assertEqual("200", BasketInfo['code'])
        self.assertTrue(BasketInfo['data']['basketName'])
        self.assertTrue(BasketInfo['data']['sceneId'])

    @unittest.skipIf(globals()['firstsceneid'] == 0, '无有效场景，跳过')
    def test_p1_saveHomeworkData(self):
        """
        title: 标准课表数据暂存
        url: /api/eteacherproduct/scene/saveHomeworkData,/api/eteacherproduct/scene/getHomeworkData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username'], password=principal_user['password']))
        BasketItems_Items = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])
        basketItemId = [item['basketItemId'] for item in BasketItems_Items['data']]
        teacher_web.removeBasketContent(basketItemIds=basketItemId, schoolId=schoolid)
        teacher_web.addBasketContent(resourceType=resourceId_XB_PAPER['resourceType'],
                                     resourceId=resourceId_XB_PAPER['id'],
                                     sceneId=globals()['firstsceneid'],
                                     category=resourceId_XB_PAPER['category'])
        contents = {}
        contents['checked'] = True
        contents['contentId'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'resourceId']
        contents['contentType'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'resourceType']
        contents['duration'] = 1500
        contents['imgUrl'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0]['picture']
        contents['itemCount'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'questionCount']
        contents['parentContentId'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'parentContentId']
        contents['resourseLink'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'previewUrl']
        contents['subject'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'subjectId']
        contents['subjectName'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0][
            'subjectName']
        contents['title'] = teacher_web.listBigHomeworkItems(sceneId=globals()['firstsceneid'])['data'][0]['title']
        saveHomeworkData = teacher_web.saveHomeworkData(sceneId=globals()['firstsceneid'], activityId=activityId,
                                                        contents=contents)
        self.assertEqual("200", saveHomeworkData['code'])
        self.assertEqual("操作成功", saveHomeworkData['msg'])
        getAssignData = teacher_web.getHomeworkData(sceneId=globals()['firstsceneid'])
        print(getAssignData)
        self.assertEqual("200", getAssignData['code'])
        self.assertTrue(len(getAssignData['data']['resources']) == 1)
