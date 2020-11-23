from testcases.api_testcases.b_end_testcases.schooluser_data import *
from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import TeacherOaClient
import datetime
import time


class CaseServices:

    @staticmethod
    def delete_all_homework():
        for i in teacher_user_list:
            teacher_web = teacher(
                web_client(username=teacher_user_list[i]['username'], password=teacher_user_list[i]['password']))
            res = teacher_web.get_homeworkrecord(HomeworkStatus=1, type=0, PageSize=40)
            homework_list = [h['homeworkid'] for h in res['data']['homeworklist'] if h['candelete']]
            if len(homework_list) > 0:
                teacher_web.deletehomework(homeworkids=homework_list)

    @staticmethod
    def delete_all_evaluationhomework():
        for i in teacher_user_list:
            teacher_web = teacher(
                web_client(username=teacher_user_list[i]['username'], password=teacher_user_list[i]['password']))
            homeworklist = teacher_web.evaluation_GetHomeworkLogList(homeworkstatus=1)
            homework_delete_list = [i['homeworkid'] for i in homeworklist['data']['records'] if
                                    i['iscandeletehomework']]
            for homeworkid in homework_delete_list:
                teacher_web.evaluation_deletehomework(homeworkid=homeworkid)

    @staticmethod
    def delete_test_classes():
        teacher_web = teacher(web_client(principal_user['username'], principal_user['password']))
        teacher_oa = teacher(TeacherOaClient())
        res = teacher_web.get_classlist()
        for i in res['data']['classlist']:
            if 'auto' in i['classname']:
                print('delete {}'.format(i['classname']))
                teacher_oa.oa_disband(schoolid=schoolid, groupid=i['classid'])

    @staticmethod
    def get_expireyear():
        expireyear = []
        if datetime.datetime.now().year >= current_school_year:
            expireyear.append(datetime.datetime.now().year + 3)
            expireyear.append(datetime.datetime.now().year + 2)
            expireyear.append(datetime.datetime.now().year + 1)
        else:
            expireyear.append(datetime.datetime.now().year + 2)
            expireyear.append(datetime.datetime.now().year + 1)
            expireyear.append(datetime.datetime.now().year)
        return expireyear


    @staticmethod
    def randomstring():
        import random
        auth = "auto"  # 定义全局验证码变量
        for i in range(0, 4):  # 定义循环4次，形成4位验证码。
            current = random.randint(0, 2)  # 定义一个随机0-4的一个范围，去猜i 的值。
            if current == i:  # 如果current 和i 的值一样
                current_code = random.randint(0, 9)  # 生成一个随机的数字
            else:  # 如果current和i 的值不一样
                current_code = chr(random.randint(65, 90))  # 生成一个随机的字母，这里一定要主义chr（）转换一下。
            auth += str(current_code)  # 将每次随机生成的值赋值给auth
        return auth

    @staticmethod
    def get_deadlinetime():
        deadline = (int(time.time()) + 86400) * 1000
        return deadline

    @staticmethod
    def get_subjectId_and_subjectEn(teacher_web):
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        return res['data'][0]['subjectId'], res['data'][0]['english']

    @staticmethod
    def get_bookId_by_subjectEn(teacher_web, subjectEn):
        res = teacher_web.homeworkprod_getQuestionBookBySubject(schoolId=schoolid, subjectEn=subjectEn)
        return res['data'][0]['children'][0]['relationId']

    @staticmethod
    def get_chapter_by_book(teacher_web, subjectEn, bookId):
        res = teacher_web.homeworkprod_getQuestionChapterByBook(schoolId=schoolid, subjectEn=subjectEn, bookId=bookId)
        return res['data'][0]['id']

    @staticmethod
    def get_point_id_by_subjectEn(teacher_web, subjectEn):
        res = teacher_web.homeworkprod_getQuestionPointBySubject(schoolId=schoolid, subjectEn=subjectEn)
        return res['data'][0]['no']

    @staticmethod
    def get_questionid_and_relationId(teacher_web):
        subjectEn = CaseServices.get_subjectId_and_subjectEn(teacher_web)[1]
        bookid = CaseServices.get_bookId_by_subjectEn(teacher_web, subjectEn)
        chapterid = CaseServices.get_chapter_by_book(teacher_web, subjectEn, bookid)
        data = {"select": 1, "subject": subjectEn, "quesChapter": chapterid,
                "quesBook": bookid, "quesKnowledge": "", "quesType": "",
                "quesCategory": "", "degreeId": "", "quesSource": "", "quesYear": "", "regionId": "", "pageIndex": 1,
                "pageSize": 10, "schoolId": schoolid}
        res = teacher_web.homeworkprod_pageQueryQuesAtChapterOrPoint(post_data=data)
        return res['data'][0]['questionId'], res['data'][0]['relationId']

    @staticmethod
    def get_paper_id(teacher_web):
        chapterid = teacher_web.homeworkprod_getPaperTreeCategory(subjectId=1, schoolId=schoolid)['data'][0]['id']
        chapterid = teacher_web.homeworkprod_getPaperTreeByChapterId(chapterId=chapterid, schoolId=schoolid)['data'][
            'childrenList'][-1]['childrenList'][0]['id']
        post_data = {"typeId": None, "subjectId": 1, "chapterId": chapterid, "tagValueList": [], "pageIndex": 1,
                     "pageSize": 20, "schoolId": schoolid}
        res = teacher_web.homeworkprod_pagePaper(post_data=post_data)
        return res['data'][0]['id']

# print(CaseServices.delete_test_classes())

