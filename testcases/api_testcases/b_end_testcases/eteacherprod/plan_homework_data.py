import datetime
import calendar

today_date = datetime.datetime.today()
this_year = today_date.date().year
if today_date.month == 1:
    last_month = 12
    last_year = this_year - 1
else:
    last_month = today_date.month - 1
    last_year = this_year
month_info = calendar.monthrange(last_year, last_month)
month_last_day = datetime.datetime.strptime('%s-%s-%s' % (last_year, last_month, month_info[1]),
                                            '%Y-%m-%d').date()
month_last_day_week = int(month_last_day.strftime('%w'))
# month_last_sunday = month_last_day

day_week = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '0': 6}
# month_last_sunday = month_last_day - datetime.timedelta(days=day_week[str(month_last_day_week)])

from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *
from testcases.api_testcases.b_end_testcases.homework_data import *


def setvideohomework_by_principal_classType_2():
    """
    校长布置学科视频作业_教学班班级作业_立即布置
    """
    teacher_principal = teacher(
        web_client(username=principal_user['username'], password=principal_user['password']))
    components = [{"type": "1", "title": "testauto_video", "resourceIds": lesson_ids}]
    gradeClasses = [{"grade": grade, "expireYear": expireyear, "classList": [groupid_jiaoxue]}]
    res = teacher_principal.sethomework(components=components, gradeClasses=gradeClasses,
                                        deadline=deadline_timestamp,
                                        arrangeType=0, classType=2, expireYears=[], isGradeHomework=False,
                                        subject='1')
    # print(res)
    time.sleep(15)  # 等待作业分发
    homeworkid = res['data'][0]
    return homeworkid


if get_env() == 'prod':
    actId = 598
    # 錯題本
    subject = 1
    bookEditionId = 14
    bookId = '1dc14bc4-ddf8-4ea9-9c7a-b767c29c3043'
    expireYear = "2021"
    startTime = "2020-01-02"
    # bizdate = month_last_sunday
    endTime = time.strftime("%Y-%m-%d", time.localtime())
    # 计划性作业
    resourceId_VIDEO = {"resourceType": 1, "id": ['21376'], "category": 3}
    resourceId_EXAM_PAPER = {"resourceType": 2, "id": ['43238'], "category": 1}
    resourceId_XB_VIDEO = {"resourceType": 11, "id": ['2084'], "category": 7}
    resourceId_XB_PAPER = {"resourceType": 12, "id": ['24160'], "category": 7}
    resourceId_FM = {"resourceType": 3, "id": ['30607'], "category": 10}
    resourceId_CAREER_NEWS = {"resourceType": 4, "id": ['2358'], "category": 11}
    resourceId_SYCHOLOGY_REPORT = {"resourceType": 5, "id": ['31577'], "category": 12}
    resourceId_FUN_TEST = {"resourceType": 6, "id": ['70'], "category": 11}
    activityId = 20936
else:
    actId = 40
    # 錯題本
    subject = 1
    bookEditionId = 14
    bookId = '1dc14bc4-ddf8-4ea9-9c7a-b767c29c3043'
    # expireYear = "2021"
    # startTime = "2020-01-02"
    # bizdate = month_last_sunday
    # endTime = time.strftime("%Y-%m-%d", time.localtime())
    resourceId_VIDEO = {"resourceType": 1, "id": ['2415'], "category": 3}
    resourceId_EXAM_PAPER = {"resourceType": 2, "id": ['74883'], "category": 1}
    resourceId_XB_PAPER = {"resourceType": 12, "id": ['80'], "category": 9}
    activityId = 21561
