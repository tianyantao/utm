from common.unittest_v2 import TestCaseV2
from testcases.api_testcases.b_end_testcases.case_services import CaseServices
from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
import datetime


class HomeworkprodResourceQuestionTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_question_subjects_by_principal(self):
        """
        title: 题库挑题-获取学科列表-校长：获取全部学科
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(principal_user['username'], principal_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(9, len(res['data']))

    def test_get_question_subjects_by_teacher(self):
        """
        title: 题库挑题-获取学科列表-学科老师：获取自己教的学科
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(1, len(res['data']))

    def test_get_question_subjects_by_classheadteacher(self):
        """
        title: 题库挑题-获取学科列表-教学班班主任：没有限制
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(classheadteacher_user['username'], classheadteacher_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(9, len(res['data']))

    def test_get_question_subjects_by_headteacher(self):
        """
        title: 题库挑题-获取学科列表-行政班班主任：获取全部学科
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(headteacher_user['username'], headteacher_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(9, len(res['data']))

    def test_get_question_subjects_by_grademaster(self):
        """
        title: 题库挑题-获取学科列表-年级主任：获取全部学科
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(grademaster_user['username'], grademaster_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(9, len(res['data']))

    def test_get_question_province(self):
        """
        title: 题库挑题-获取地区列表
        url: /api/homeworkprod/resource/question/getQuestionProvince
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        res = teacher_web.homeworkprod_getQuestionProvince(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)
        self.assertIn("全国", str(res))

    def test_get_question_book_by_subject(self):
        """
        title: 题库挑题-获取教材版本
        url: /api/homeworkprod/resource/question/getQuestionBookBySubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        res = teacher_web.homeworkprod_getQuestionBookBySubject(schoolId=schoolid, subjectEn=subjectEn)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_question_filter_list(self):
        """
        title: 题库挑题-获取题型
        url: /api/homeworkprod/resource/question/getQuestionFilterList
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        res = teacher_web.homeworkprod_getQuestionFilterList(schoolId=schoolid, subjectEn=subjectEn)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_question_chapter_by_book(self):
        """
        title: 题库挑题-获取章节目录
        url: /api/homeworkprod/resource/question/getQuestionChapterByBook
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        bookid = CaseServices.get_bookId_by_subjectEn(teacher_web, subjectEn)
        res = teacher_web.homeworkprod_getQuestionChapterByBook(schoolId=schoolid, bookId=bookid, subjectEn=subjectEn)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_page_query_question_by_chapter(self):
        """
        title: 题库挑题-章节挑题
        url: /api/homeworkprod/resource/question/pageQueryQuesAtChapterOrPoint
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        bookid = CaseServices.get_bookId_by_subjectEn(teacher_web, subjectEn)
        chapterid = CaseServices.get_chapter_by_book(teacher_web, subjectEn, bookid)
        data = {"select": 1, "subject": subjectEn, "quesChapter": chapterid,
                  "quesBook": bookid, "quesKnowledge": "", "quesType": "",
                  "quesCategory": "", "degreeId": "", "quesSource": "", "quesYear": "", "regionId": "", "pageIndex": 1,
                  "pageSize": 10, "schoolId": schoolid}
        res = teacher_web.homeworkprod_pageQueryQuesAtChapterOrPoint(post_data=data)
        print(res)
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_question_point_by_subject(self):
        """
        title: 题库挑题-获取知识点目录树
        url: /api/homeworkprod/resource/question/getQuestionPointBySubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        res = teacher_web.homeworkprod_getQuestionPointBySubject(schoolId=schoolid, subjectEn=subjectEn)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_page_query_question_by_pointid(self):
        """
        title: 题库挑题-知识点挑题
        url: /api/homeworkprod/resource/question/pageQueryQuesAtChapterOrPoint
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        pointid = CaseServices.get_point_id_by_subjectEn(teacher_web, subjectEn)
        data = {"select": 2, "subject": subjectEn, "quesChapter": "",
                  "quesBook": "", "quesKnowledge": pointid, "quesType": "",
                  "quesCategory": "", "degreeId": "", "quesSource": "", "quesYear": "", "regionId": "", "pageIndex": 1,
                  "pageSize": 10, "schoolId": schoolid}
        res = teacher_web.homeworkprod_pageQueryQuesAtChapterOrPoint(post_data=data)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_query_question_detail(self):
        """
        title: 题库挑题-获取题目解析
        url: /api/homeworkprod/resource/question/queryQuestionDetail
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        question_id = CaseServices.get_questionid_and_relationId(teacher_web)[1]
        res = teacher_web.homeworkprod_queryQuestionDetail(subjectEn=subjectEn, questionId=question_id, queryType=1, schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)


class HomeworkprodResourcePaperTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_paper_tree_category_by_subjectid(self):
        """
        title: 试卷挑题-获取教材版本
        url: /api/homeworkprod/resource/paper/getPaperTreeCategory
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        res = teacher_web.homeworkprod_getPaperTreeCategory(subjectId=1, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_paper_tree_by_chapterid(self):
        """
        title: 试卷挑题-根据章节id获取知识点树
        url: /api/homeworkprod/resource/paper/getPaperTreeByChapterId
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        chapterid = teacher_web.homeworkprod_getPaperTreeCategory(subjectId=1, schoolId=schoolid)['data'][0]['id']
        res = teacher_web.homeworkprod_getPaperTreeByChapterId(chapterId=chapterid, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_chapter_filter_paper_type(self):
        """
        title: 试卷挑题-根据章节id获取试卷类型
        url: /api/homeworkprod/resource/paper/getChapterFilterPaperType
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        chapterid = teacher_web.homeworkprod_getPaperTreeCategory(subjectId=1, schoolId=schoolid)['data'][0]['id']
        res = teacher_web.homeworkprod_getChapterFilterPaperType(chapterId=chapterid, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_page_paper(self):
        """
        title: 试卷挑题-获取试卷列表
        url: /api/homeworkprod/resource/paper/pagePaper
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        chapterid = teacher_web.homeworkprod_getPaperTreeCategory(subjectId=1, schoolId=schoolid)['data'][0]['id']
        chapterid = teacher_web.homeworkprod_getPaperTreeByChapterId(chapterId=chapterid, schoolId=schoolid)['data']['childrenList'][-1]['childrenList'][0]['id']
        post_data = {"typeId": None, "subjectId": 1, "chapterId": chapterid, "tagValueList": [], "pageIndex": 1,
                     "pageSize": 20, "schoolId": schoolid}
        res = teacher_web.homeworkprod_pagePaper(post_data=post_data)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)

    def test_get_paper_info(self):
        """
        title: 试卷挑题-根据试卷id获取试卷详情
        url: /api/homeworkprod/resource/paper/getPaperInfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        paperid = CaseServices.get_paper_id(teacher_web)
        res = teacher_web.homeworkprod_getPaperInfo(paperId=paperid, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']) > 0)
        self.assertTrue(len(res['data']['questionList']) > 0)


class HomeworkprodResourceWrongQuestionTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_wrong_question_chapter(self):
        """
        title: 题库挑题-学生错题-获取章节目录
        url: /api/homeworkprod/resource/wrongQuestion/getWrongQuestionChapter
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectid, subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)
        bookid = CaseServices.get_bookId_by_subjectEn(teacher_web, subjectEn)
        res = teacher_web.homeworkprod_getWrongQuestionChapter(subjectId=subjectid, subjectEn=subjectEn, bookId=bookid, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])

    def test_get_wrong_question_points(self):
        """
        title: 题库挑题-学生错题-获取知识点目录
        url: /api/homeworkprod/resource/wrongQuestion/getWrongQuestionPoints
        author: 田彦涛
        """
        teacher_web = teacher(web_client(teacher_user['username'], teacher_user['password']))
        subjectid, subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)
        res = teacher_web.homeworkprod_getWrongQuestionPoints(subjectId=subjectid, subjectEn=subjectEn, schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])

    def test_get_wrong_question_search_option_by_principal(self):
        """
        title: 题库挑题-学生错题-获取班级年级筛选条件-校长
        url: /api/homeworkprod/resource/wrongQuestion/getWrongQuestionPoints
        author: 田彦涛
        """
        teacher_web = teacher(web_client(principal_user['username'], principal_user['password']))
        res = teacher_web.homeworkprod_getWrongQuestionSearchOption(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']['gradeOptions']) >= 3)

    def test_get_wrong_question_search_option_by_headteacher(self):
        """
        title: 题库挑题-学生错题-获取班级年级筛选条件-班主任
        url: /api/homeworkprod/resource/wrongQuestion/getWrongQuestionPoints
        author: 田彦涛
        """
        teacher_web = teacher(web_client(headteacher_user['username'], headteacher_user['password']))
        res = teacher_web.homeworkprod_getWrongQuestionSearchOption(schoolId=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertTrue(len(res['data']['gradeOptions']) >= 3)
        self.assertTrue(len(res['data']['classOptions']) > 0)
        self.assertEqual(1, res['data']['filterScope'])

    def test_page_wrong_questions_by_grade(self):
        """
        title: 题库挑题-学生错题-获取最近三个月的错题-按年级筛选
        url: /api/homeworkprod/resource/wrongQuestion/pageWrongQuestions
        author: 田彦涛
        """
        teacher_web = teacher(web_client(headteacher_user['username'], headteacher_user['password']))
        end_time = datetime.datetime.now().strftime("%Y-%m-%d")
        start_time = (datetime.datetime.now() + datetime.timedelta(days=-90)).strftime("%Y-%m-%d")
        post_data = {"errorQuestionScopeType": 0, "classId": "", "expireYear": expireyear, "errorQuestionType": 1,
                     "answerTimes": 0, "correctRate": 100, "startTime": start_time, "endTime": end_time,
                     "sortModel": 0, "points": [], "kemuId": 1, "schoolId": 28344, "page": 1, "pageSize": 10}
        res = teacher_web.homeworkprod_pageWrongQuestions(post_data)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        # self.assertTrue(len(res['data']) > 0)
