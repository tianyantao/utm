from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from common.unittest_v2 import TestCaseV2


class NewSenior2020Test(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_new_getTextbookVersion(self):
        """
        title: 获取用户新老教程版本--新教程
        url: /student/getTextbookVersion
        author: 张水琴
        """

        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.student_getTextbookVersion()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(1, res['data']['textbookVersion'])

    def test_p1_old_getTextbookVersion(self):
        """
        title: 获取用户新老教程版本--老教程
        url: /student/getTextbookVersion
        author: 张水琴
        """

        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.student_getTextbookVersion()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(2, res['data']['textbookVersion'])

    def test_p1_vip_getNotice(self):
        """
        title:公告栏、是否显示成为会员--是会员
        url:/student/getNotice
        author:张水琴
        """

        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.student_getNotice()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(0, res['data']['vipStatus'])

    def test_p1_novip_getNotice(self):
        """
        title:公告栏、是否显示成为会员--不是会员
        url:/student/getNotice
        author:张水琴
        """

        student_web = teacher(
            web_client(username=novip_student['username'], password=novip_student['password']))
        res = student_web.student_getNotice()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(1, res['data']['vipStatus'])

    def test_p1_novip_getMemberDetailsPage(self):
        """
        title:会员详情页--不是会员
        url:/student/getMemberDetailsPage
        author:张水琴
        """
        student_web = teacher(
            web_client(username=novip_student['username'], password=novip_student['password']))
        res = student_web.student_getMemberDetailsPage()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(0, res['data']['isVIP'])

    def test_p1_vip_getMemberDetailsPage(self):
        """
        title:会员详情页--是会员
        url:/student/getMemberDetailsPage
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.student_getMemberDetailsPage()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertEqual(1, res['data']['isVIP'])

    def test_p1_getWeaknessMealDetail(self):
        """
        title:补弱加餐包详情页
        url:/meal/getWeaknessMealDetail
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.meal_getWeaknessMealDetail()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_xinli_getInterestMealDetail(self):
        """
        title:兴趣加餐包详情页--心灵成长
        url:/meal/getInterestMealDetail
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.meal_getInterestMealDetail(type=1)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_apply_getInterestMealDetail(self):
        """
        title:兴趣加餐包详情页--生涯规划
        url:/meal/getInterestMealDetail
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.meal_getInterestMealDetail(type=2)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_Quality_getInterestMealDetail(self):
        """
        title:兴趣加餐包详情页--综合素养
        url:/meal/getInterestMealDetail
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.meal_getInterestMealDetail(type=3)
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_rewardPopup(self):
        """
        title:答题积分赛-奖励弹窗（T+1）
        url:/reward/rewardPopup
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.reward_rewardPopup()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_seriesPartakeRewardPopup(self):
        """
        title:答题积分赛-连续参与答题奖励（实时）
        url:/reward/seriesPartakeRewardPopup
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.reward_seriesPartakeRewardPopup()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_seriesChallengeRewardPopup(self):
        """
        title:C端主页-连续完成作业奖励（实时）
        url:/reward/seriesChallengeRewardPopup
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.reward_seriesChallengeRewardPopup()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getBanner(self):
        """
        title:积分排行banner
        url:/read/getBanner
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getBanner()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getTodayAnswerRank(self):
        """
        title:获取今日排行榜以及我的排名和成绩
        url:/answer/getTodayAnswerRank
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.answer_getTodayAnswerRank()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getHistoryAnswerRank(self):
        """
        title:获取历史积分榜以及我的积分排名
        url:/answer/getHistoryAnswerRank
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.answer_getHistoryAnswerRank()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getAnswerCountsState(self):
        """
        title:可答题次数状态
        url:/answer/getAnswerCountsState
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.answer_getAnswerCountsState()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getStudentAppBanner(self):
        """
        title:C端标准化学习-获取banner列表 h5
        url:/read/getStudentAppBanner
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getStudentAppBanner()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getStudentPcBanner(self):
        """
        title:C端标准化学习-获取banner列表 pc
        url:/read/getStudentPcBanner
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getStudentPcBanner()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getAppTuoZhanTiSheng(self):
        """
        title:拓展提升_h5
        url:/read/getAppTuoZhanTiSheng
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getAppTuoZhanTiSheng()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getPcTuoZhanTiSheng(self):
        """
        title:拓展提升_pc
        url:/read/getPcTuoZhanTiSheng
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getPcTuoZhanTiSheng()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getMasterpiece(self):
        """
        title:名著精读
        url:/read/getMasterpiece
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getMasterpiece()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getRecommend(self):
        """
        title:推荐书单
        url:/read/getRecommend
        author:张水琴
        """
        student_web = teacher(
            web_client(username=old_course_student['username'], password=old_course_student['password']))
        res = student_web.read_getRecommend()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getSingleLive(self):
        """
        title:获取直播列表
        url:/live/getSingleLive
        author:张水琴
        """
        student_web = teacher(
            web_client(username=principal_user['username'], password=principal_user['password']))
        res = student_web.live_getSingleLive()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getHomeworkState(self):
        """
        title:C端获取是否布置了作业
        url:/newStudent/getHomeworkState
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newStudent_getHomeworkState()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_listJoinClass(self):
        """
        title:获取已加入班级列表
        url:/newStudent/listJoinClass
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newStudent_listJoinClass()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_getSchoolVideoInfo(self):
        """
        title:学生端获取学校的视频信息
        url:/newStudent/getSchoolVideoInfo
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newStudent_getSchoolVideoInfo()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getHomeworkProgress(self):
        """
        title:获取C端作业总进度
        url:/newStudent/getHomeworkProgress
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newStudent_getHomeworkProgress()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getHomeworkInfo(self):
        """
        title:C端作业及非作业详情/变更记录
        url:/newStudent/getHomeworkInfo
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newStudent_getHomeworkInfo()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data']['dateSourceList'])

    def test_p1_getState(self):
        """
        title:获取状态
        url:/newTeacher/getState
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newTeacher_getState()
        print(res)
        self.assertEqual('200', res['code'])

    def test_p1_getCategoryTree(self):
        """
        title:新高一四期 获取分类信息树
        url:/newTeacher/getCategoryTree
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = student_web.newTeacher_getCategoryTree()
        print(res)
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_listLessonSchedule(self):
        """
        title:获取课表方案
        url:/newTeacher/listLessonSchedule
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = student_web.newTeacher_listLessonSchedule()
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_listSubjectVersion(self):
        """
        title:获取新教材版本
        url:/newTeacher/listSubjectVersion
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res = student_web.newTeacher_listSubjectVersion()
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_getStandardResource(self):
        """
        title:获取标准化课表
        url:/newTeacher/getStandardResource
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res1 = student_web.newTeacher_getCategoryTree()
        print(res1)
        versionId = res1['data']['categoryTree'][0]['typeList'][0]['versionList'][0]['versionId']
        res = student_web.newTeacher_getStandardResource(versionId)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_getTeacherCustom(self):
        """
        title:获取自定义课表
        url:/newTeacher/getTeacherCustom
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_senior_user['username'], password=new_senior_user['password']))
        res1 = student_web.newTeacher_getCategoryTree()
        print(res1)
        textbookId = res1['data']['categoryTree'][0]['textbookId']
        typeId = res1['data']['categoryTree'][0]['typeList'][1]['typeId']
        res = student_web.newTeacher_getTeacherCustom(textbookId, typeId)
        print(res)
        self.assertEqual('200', res['code'])
        self.assertIsNotNone(res['data'])

    def test_p1_getAssignedHomeworkMaterial(self):
        """
        title:获取已布置作业的讲义
        url:/newTeacher/getAssignedHomeworkMaterial
        author:张水琴
        """
        student_web = teacher(
            web_client(username=new_course_student['username'], password=new_course_student['password']))
        res = student_web.newTeacher_getAssignedHomeworkMaterial()
        print(res)
        self.assertEqual('200', res['code'])
