from lib.api_lib.teacher.teacher_urls import TeacherUrls
import time
import random
from common.helper import get_str_md5
from config.config_case import ConfigCase


def timestampms():
    # 返回延迟一天的时间戳（ms）
    timestamp = time.time()
    timestamp1 = int(timestamp) + 86400
    return int(round(timestamp1 * 1000))


class TeacherWly:

    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()

    # B端地图模块
    def hp_ThemeMapData(self, **kwargs):
        return self.client.post(url=self.url_builder.hp_ThemeMapData, data=kwargs)

    def hp_themerecord(self, **kwargs):
        return self.client.post(url=self.url_builder.hp_themerecord, data=kwargs)

    def hp_themehomeworkdetail(self, **kwargs):
        return self.client.post(url=self.url_builder.hp_themehomeworkdetail, data=kwargs)

    def hp_setxuekevideohomework(self, isgradehomework, gradeyear, classlist,
                                 videohomeworktitle, videoid, kemuid, themeid, moduleid, deadline=timestampms()):
        post_data = \
            {
                "themeid": themeid,
                "moduleid": moduleid,
                "deadline": deadline,
                "isgradehomework": isgradehomework,
                "gradeyear": gradeyear,
                "classlist": classlist,
                "videohomework": {
                    "title": videohomeworktitle,
                    "videos": [{"id": videoid, "kemuid": kemuid}],
                },
                "paperhomework": {"title": None},
                "fmhomework": {"title": None},
                "evaluationhomework": {"title": None}
            }
        return self.client.post(url=self.url_builder.hp_setxuekehomework, data=post_data)

    def hp_setshengyavideohomework(self, isgradehomework, gradeyear, classlist,
                                   videohomeworktitle, videoid, kemuid, themeid, moduleid, deadline=timestampms()):
        post_data = \
            {
                "themeid": themeid,
                "moduleid": moduleid,
                "deadline": deadline,
                "isgradehomework": isgradehomework,
                "gradeyear": gradeyear,
                "classlist": classlist,
                "videohomework": {
                    "title": videohomeworktitle,
                    "videos": [{"id": videoid, "kemuid": kemuid}],
                },
                "paperhomework": {"title": None},
                "fmhomework": {"title": None},
                "evaluationhomework": {"title": None}
            }
        return self.client.post(url=self.url_builder.hp_setshengyahomework, data=post_data)

    # 校本模块
    def get_sbravailablegrades(self):
        post_data = {}
        return self.client.post(url=self.url_builder.sbr_getavailablegrades, data=post_data)

    def get_SbrPaperFilter(self):
        return self.client.get(url=self.url_builder.GetSbrPaperFilter)

    def get_SbrPaper(self, kemu=1, grades=0, page=1, pagesize=15):
        post_data = \
            {
                "kemu": kemu,
                "grades": grades,
                "page": page,
                "pagesize": pagesize
            }
        return self.client.post(url=self.url_builder.getSbrPaperPagingList, data=post_data)

    def classtypeoptions(self, classTypes='classTypes', includeAll=False):
        params = {"enumType": classTypes, "includeAll": includeAll}
        return self.client.get(url=self.url_builder.selectclasstypeoptions, params=params)

    def setsbrpaperhomework(self, expireyears=[], grade=0, expireyear=0, classlist=[], classtype=0, deadline="",
                            iscgradehomework=False, kemu=0, paperids=[], title='autoSbr试卷'):
        # 如果是年级作业，需要传ExpireYears(过期年份)，iscgradehomework：true,ClassList: []，classtype(1是行政班，2是教学班)
        post_data = \
            {
                "ExpireYears": expireyears,
                "GradeClasses": [
                    {
                        "Grade": grade,
                        "ExpireYear": expireyear,
                        "ClassList": classlist
                    }
                ],
                "classtype": classtype,
                "deadline": deadline,
                "iscgradehomework": iscgradehomework,
                "kemu": kemu,
                "paperids": paperids,
                "title": title
            }
        return self.client.post(url=self.url_builder.SetSbrPaperHomework, data=post_data)

    # 接口弃用
    # def get_classlist(self, classname="", classtype="0", expireyear="0", page=1, pagesize=300):
    #     post_data = \
    #         {
    #             "classname": classname,
    #             "classtype": classtype,
    #             "expireyear": expireyear,
    #             "page": page,
    #             "pagesize": pagesize
    #         }
    #     return self.client.post(url=self.url_builder.getclasslist, data=post_data)

    def get_classstudents(self, classid, sort=1, page=1, pagesize=100):
        post_data = \
            {
                'classid': classid,
                'sort': sort,
                'page': page,
                'pagesize': pagesize,
                'studentname': None
            }
        return self.client.post(url=self.url_builder.classstudents, data=post_data)

    def create_administrationclass(self, classname=None, classnametype=2, expireyear=2021):
        if classname is None:
            classname = random.randint(1000, 9999)
        post_data = \
            {
                'classname': classname,
                'classnametype': classnametype,
                'expireyear': expireyear
            }
        return self.client.post(url=self.url_builder.createadministrationclass, data=post_data)

    def create_teachingclass(self, classnametype=1, expireyear=2021, subjectid=1):
        classname = "{}".format(random.randint(1, 99999))
        post_data = \
            {
                "classname": classname,
                "classnametype": classnametype,
                "expireyear": expireyear,
                "subjectid": subjectid
            }
        return self.client.post(url=self.url_builder.createteachingclass, data=post_data)

    def disband_teachingclass(self, classid):
        post_data = \
            {
                "classid": classid
            }
        return self.client.post(url=self.url_builder.disbandclass, data=post_data)

    def SubmitJoinClassInfo(self, classid, rolevalues="32,64"):
        post_data = \
            {
                "classid": classid,
                "rolevalues": rolevalues
            }
        return self.client.post(url=self.url_builder.SubmitJoinClassInfo, data=post_data)

    def TeacherRoleGroupList(self, expireyear=2020):
        post_data = \
            {
                "expireyear": expireyear
            }
        return self.client.post(url=self.url_builder.TeacherRoleGroupList, data=post_data)

    def addedstudentlist(self, classid):
        post_data = \
            {
                "classid": classid
            }
        return self.client.post(url=self.url_builder.addedstudentlist, data=post_data)

    def submitaddedstudentlist(self, classid, studentids):
        post_data = \
            {
                "classid": classid,
                "studentids": [studentids]
            }
        return self.client.post(url=self.url_builder.submitaddedstudentlist, data=post_data)

    def removestudent(self, classid, studentids):
        post_data = \
            {
                "classid": classid,
                "userid": studentids
            }
        return self.client.post(url=self.url_builder.removestudent, data=post_data)

    def studentclasslist(self):
        post_data = {}
        return self.client.post(url=self.url_builder.studentmyclasslist, data=post_data)

    def studentclasslist_app(self, version="9.0.8"):
        token = self.client.user_token
        params = {"token": token, "sign": get_str_md5(ConfigCase.APP_AES_KEY + token + ConfigCase.APP_AES_KEY)}
        return self.client.get(url=self.url_builder.studentmyclasslist_app, params=params, sign_mode=11,
                               headers={"version": version})

    def getclasslistofschool(self):
        post_data = {}
        return self.client.post(url=self.url_builder.schoolandclassinfo, data=post_data)

    def getclasslistofschool_app(self):
        now = int(time.time())
        token = self.client.user_token
        post_data = {"now": now, "sign": get_str_md5(ConfigCase.APP_AES_KEY + str(now) + token + ConfigCase.APP_AES_KEY), "token": token}
        return self.client.post(url=self.url_builder.schoolandclassinfo_app, data=post_data)

    def searchschools_app(self, keyword):
        now = int(time.time())
        token = self.client.user_token
        post_data = \
            {
                "now": now,
                "sign": get_str_md5(ConfigCase.APP_AES_KEY + str(now) + token + ConfigCase.APP_AES_KEY),
                "token": token,
                "payload":
                    {
                        "schoolname": keyword
                    }
            }
        return self.client.post(url=self.url_builder.searchschools_app, data=post_data)

    def searchclasses_app(self, schoolid):
        now = int(time.time())
        token = self.client.user_token
        post_data = \
            {
                "now": now,
                "sign": get_str_md5(ConfigCase.APP_AES_KEY + str(now) + token + ConfigCase.APP_AES_KEY),
                "token": token,
                "payload":
                    {
                        "schoolid": schoolid
                    }
            }
        return self.client.post(url=self.url_builder.searchclasses_app, data=post_data)

    # 学情报告_学生学情报告
    def breportgetuserrole(self, userId):
        post_data = {"userId": userId}
        return self.client.post(url=self.url_builder.breportgetuserrole, data=post_data)

    def statisticsstudentnum(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticsstudentnum, data=post_data)

    def statisticsgeneraldata(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticsgeneraldata, data=post_data)

    def statisticsvideo(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticsvideo, data=post_data)

    def statisticsexercise(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticsexercise, data=post_data)

    def statisticspsychocate(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticspsychocate, data=post_data)

    def statisticscareer(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.statisticscareer, data=post_data)

    # 学情报告_学生使用详情
    def usagegeneral(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.usagegeneral, data=post_data)

    def usagedetails(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime,
                "pagenum": 1,
                "pagesize": 8,
                "sort": "view_duration",
                "desc": True,
                "studentname": "0",
            }
        return self.client.post(url=self.url_builder.usagedetails, data=post_data)

    def usagevideodetails(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime,
                "pagenum": 1,
                "pagesize": 8,
                "sort": "view_duration",
                "desc": True,
                "studentname": "0",
                "subjectName": "0"
            }
        return self.client.post(url=self.url_builder.usagevideodetails, data=post_data)

    def usageexerciseanswer(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime,
                "pagenum": 1,
                "pagesize": 8,
                "sort": "view_duration",
                "desc": True,
                "studentname": "0",
                "subjectName": "0"
            }
        return self.client.post(url=self.url_builder.usageexerciseanswer, data=post_data)

    def usagehomeworklist(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime,
                "pagenum": 1,
                "pagesize": 8,
                "sort": "finish_date",
                "desc": True,
                "studentname": "0"
            }
        return self.client.post(url=self.url_builder.usagehomeworklist, data=post_data)

    # 教师使用报告
    def staffusagesum(self, grade, classid):
        post_data = \
            {
                "grade": grade,
                "classid": classid,
                "pagenum": 1,
                "pagesize": 8
            }
        return self.client.post(url=self.url_builder.staffusagesum, data=post_data)

    def staffusagebehavior(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.staffusagebehavior, data=post_data)

    def staffusagedetails(self, grade, gradeName, classid, className, starttime, endtime):
        post_data = \
            {
                "grade": grade,
                "gradeName": gradeName,
                "classid": classid,
                "className": className,
                "starttime": starttime,
                "endtime": endtime
            }
        return self.client.post(url=self.url_builder.staffusagedetails, data=post_data)

    # 微信端
    def menuall(self, token):
        header = {"token": token}
        return self.client.get(url=self.url_builder.menuall, headers=header)

    def menuselect(self, menuId, subjectId):
        params = {"menuId": menuId, "subjectId": subjectId}
        return self.client.get(url=self.url_builder.menuselect, params=params)

    def solutionlist(self, menuId, pageIndex=1, pageSize=300):
        post_data = {"menuId": menuId, "pageIndex": pageIndex, "pageSize": pageSize}
        return self.client.post(url=self.url_builder.solutionlist, data=post_data)

    def topicdetail(self, topicId):
        params = {"topicId": topicId}
        return self.client.get(url=self.url_builder.topicdetail, params=params)

    def solutioncontent(self, solutionId):
        params = {"solutionId": solutionId}
        return self.client.get(url=self.url_builder.solutioncontent, params=params)

    def solutionintroduce(self, solutionId):
        params = {"solutionId": solutionId}
        return self.client.get(url=self.url_builder.solutionintroduce, params=params)

    def papergetquestions(self, token, paperId):
        header = {"token": token}
        params = {"paperId": paperId}
        return self.client.get(url=self.url_builder.papergetquestions, headers=header, params=params)

    def createpaper(self, token, questionids, paperid):
        header = \
            {"token": token,
             "Content-Type": "application/json",
             "X-Requested-With": "XMLHttpRequest",
             "Ewt-ContentStyle": "Camelcase"
             }
        post_data = {"questionids": questionids, "paperid": paperid}
        return self.client.post(self.url_builder.createpaper, headers=header, data=post_data)

    def wxgetclasseswithgradeinfo(self, subjectId, withSpecialTopic):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"subjectId": subjectId, "withSpecialTopic": withSpecialTopic}
        return self.client.get(url=self.url_builder.wxgetclasseswithgradeinfo, headers=header, params=params)

    def homeworkassign(self, arrangeType, classType, components, isGradeHomework, gradeClasses, currentClass,
                       expireYears, selectedClass, subject, solutionId, usetimes, startTime, deadline):
        # （arrangeType立即布置：0；定时布置：1；）
        # （classType行政班：1；教学班：2）
        # (type:视频1、试卷2、专题3;)
        # isGradeHomework false/true
        post_data = \
            {"arrangeType": arrangeType,
             "classType": classType,
             "components": components,  # [{title: "10.10-111汤接口测试专用课程讲-第一讲等", type: 1, refIds: [2419, 1]}]
             "isGradeHomework": isGradeHomework,
             "gradeClasses": gradeClasses,  # [{expireYear: 2022, classList: [991464]}]
             "currentClass": currentClass,
             # [{classid: 991464, classname: "wly0314", classtype: 1, subject: 0, gradeyear: 2022, studentnumber: 2,…}]
             "expireYears": expireYears,
             "selectedClass": selectedClass,  # ?不懂
             "subject": subject,
             "solutionId": solutionId,
             "usetimes": usetimes,
             "startTime": startTime,
             "deadline": deadline
             }
        # header = {"Content-Type": application/json}headers=header,
        return self.client.post(url=self.url_builder.homeworkassign, data=post_data)

    def fetchuserinfo(self, token):
        header = {"token": token}
        return self.client.get(url=self.url_builder.fetchuserinfo, headers=header)

    def getuserrole(self, ettoken):
        header = {"Content-Type": "application/json"}
        if ettoken:
            header["ettoken"] = ettoken
        data = {}
        return self.client.post(url=self.url_builder.getuserrole, headers=header, data=data)

    def myclasslist(self):
        return self.client.get(url=self.url_builder.myclasslist)

    # 接口弃用
    # def classmanagegrades(self):
    #     post_data = {}
    #     return self.client.post(url=self.url_builder.classmanagegrades, data=post_data)

    def classinfo(self, classid):
        post_data = {"classid": classid}
        return self.client.post(url=self.url_builder.classinfo, data=post_data)

    # 督学
    def getteachergradeclassList(self):
        return self.client.get(url=self.url_builder.getteachergradeclassList)

    def getgradeweeklydetails(self, bizdate, schoolId, gradeYear):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        # post_data = "bizdate={0}&schoolId={1}&gradeYear={2}".format(bizdate, schoolId, gradeYear)
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear
            }
        return self.client.post(url=self.url_builder.gradeweeklydetails, data=post_data)

    def pagestudenthomeworklist(self, bizdate, schoolId, gradeYear, pageIndex=1, pageSize=20):
        post_data = \
            {"pageIndex": pageIndex,
             "pageSize": pageSize,
             "bizdate": bizdate,
             "schoolId": schoolId,
             "gradeYear": gradeYear
             }
        return self.client.post(url=self.url_builder.pagestudenthomeworklist, data=post_data)

    def teacherusedetaillist(self, bizdate, schoolId, gradeYear):
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear
            }
        return self.client.post(url=self.url_builder.teacherusedetaillist, data=post_data)

    def getschoolgradeclasslist(self, schoolId, gradeYear):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        params = "schoolId={0}&gradeYear={1}".format(schoolId, gradeYear)
        return self.client.get(url=self.url_builder.schoolgradeclasslist, params=params)

    def getclassweeklydetails(self, bizdate, schoolId, gradeYear, classId, classType=1):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        # post_data = "bizdate={0}&schoolId={1}&gradeYear={2}".format(bizdate, schoolId, gradeYear)
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear,
                "classType": classType,
                "classId": classId
            }
        return self.client.post(url=self.url_builder.classweeklydetails, data=post_data)

    def reportpraise(self, bizdate, schoolId, gradeYear, classId, deviceType=2, reportType=2):
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear,
                "reportType": reportType,
                "classId": classId,
                "deviceType": deviceType
            }
        return self.client.post(url=self.url_builder.reportpraise, data=post_data)

    def homeworkurge(self, homeworkId, deviceType=3):
        params = {"homeworkId": homeworkId, "deviceType": deviceType}
        return self.client.get(url=self.url_builder.homeworkurge, params=params)

    def homeworkurgestate(self, homeworkId):
        params = {"homeworkId": homeworkId}
        return self.client.get(url=self.url_builder.homeworkurgestate, params=params)

    # 督学
    def getteachergradeclassList(self):
        return self.client.get(url=self.url_builder.getteachergradeclassList)

    def getgradeweeklydetails(self, bizdate, schoolId, gradeYear):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        # post_data = "bizdate={0}&schoolId={1}&gradeYear={2}".format(bizdate, schoolId, gradeYear)
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear
            }
        return self.client.post(url=self.url_builder.gradeweeklydetails, data=post_data)

    def pagestudenthomeworklist(self, bizdate, schoolId, gradeYear, pageIndex=1, pageSize=20):
        post_data = \
            {"pageIndex": pageIndex,
             "pageSize": pageSize,
             "bizdate": bizdate,
             "schoolId": schoolId,
             "gradeYear": gradeYear
             }
        return self.client.post(url=self.url_builder.pagestudenthomeworklist, data=post_data)

    def teacherusedetaillist(self, bizdate, schoolId, gradeYear):
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear
            }
        return self.client.post(url=self.url_builder.teacherusedetaillist, data=post_data)

    def getschoolgradeclasslist(self, schoolId, gradeYear):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        params = "schoolId={0}&gradeYear={1}".format(schoolId, gradeYear)
        return self.client.get(url=self.url_builder.schoolgradeclasslist, params=params)

    def getclassweeklydetails(self, bizdate, schoolId, gradeYear, classId, classType=1):
        # header = \
        #     {"Content-Type": "application/x-www-form-urlencoded"}
        # post_data = "bizdate={0}&schoolId={1}&gradeYear={2}".format(bizdate, schoolId, gradeYear)
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear,
                "classType": classType,
                "classId": classId
            }
        return self.client.post(url=self.url_builder.classweeklydetails, data=post_data)

    def reportpraise(self, bizdate, schoolId, gradeYear, classId, deviceType=2, reportType=2):
        post_data = \
            {
                "bizdate": bizdate,
                "schoolId": schoolId,
                "gradeYear": gradeYear,
                "reportType": reportType,
                "classId": classId,
                "deviceType": deviceType
            }
        return self.client.post(url=self.url_builder.reportpraise, data=post_data)

    def homeworkurge(self, homeworkId, deviceType=3):
        params = {"homeworkId": homeworkId, "deviceType": deviceType}
        return self.client.get(url=self.url_builder.homeworkurge, params=params)

    def homeworkurgestate(self, homeworkId):
        params = {"homeworkId": homeworkId}
        return self.client.get(url=self.url_builder.homeworkurgestate, params=params)

    # 假期调用的接口
    def getteacherinfo(self):
        return self.client.get(url=self.url_builder.teacherinfo)

    def getschoolhomeworkassigncount(self, actId):
        params = {"actId": actId}
        return self.client.get(url=self.url_builder.schoolhomeworkassigncount, params=params)

    def getgradetagAndassignInfo(self, token, actId):
        header = {"token": token}
        params = {"actId": actId}
        return self.client.get(url=self.url_builder.gradetagAndassignInfo, params=params, headers=header)

    def getgradetopcategoryid(self, token, actId, grade=1):
        header = {"token": token}
        params = {"actId": actId, "grade": grade}
        return self.client.get(url=self.url_builder.gradetopcategoryid, params=params, headers=header)

    # 错題本
    def geterrorquestioncatrgories(self, subject, bookEditionId, bookId, schoolId):
        params = {"subject": subject,
                  "bookEditionId": bookEditionId,
                  "bookId": bookId,
                  "schoolId": schoolId}
        return self.client.get(url=self.url_builder.errorquestioncatrgories, params=params)

    def geterrorquestionpoints(self, subject, schoolId):
        params = {"subject": subject,
                  "schoolId": schoolId}
        return self.client.get(url=self.url_builder.errorquestionpoints, params=params)

    def geterrorquestions(self, schoolId, startTime, endTime, expireYear, errorQuestionScopeType=0,
                          errorQuestionType=1, answerTimes=0, correctRate=100, sortModel=0, points=[],
                          kemuId=1, page=1, pagesize=10):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "schoolId": schoolId,
                "startTime": startTime,
                "endTime": endTime,
                "expireYear": expireYear,
                "errorQuestionScopeType": errorQuestionScopeType,
                "errorQuestionType": errorQuestionType,
                "answerTimes": answerTimes,
                "correctRate": correctRate,
                "sortModel": sortModel,
                "points": points,
                "kemuId": kemuId,
                "page": page,
                "pageSize": pagesize
            }
        return self.client.post(url=self.url_builder.errorquestions, headers=header, data=post_data)

    def defaultsearchoption(self):
        return self.client.get(url=self.url_builder.defaultsearchoption)

    # 作业
    '''计划性大作业'''

    def getuserhomeworkscenes(self, userId, schoolId):
        header = \
            {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"userId": userId,
                  "schoolId": schoolId}
        return self.client.get(url=self.url_builder.planhomework_getUserHomeworkScenes, headers=header, params=params)

    def gethomeworksceneinfo(self, sceneId):
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_getHomeworkSceneInfo, params=params)

    def getDefaultSubject(self):
        return self.client.get(url=self.url_builder.planhomework_getDefaultSubject)

    def listBigHomeworkSummary(self, sceneId):
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_listBigHomeworkSummary, params=params)

    def listBigHomeworkItems(self, sceneId, needGetExaminationRelatedPosition=1):
        params = {"sceneId": sceneId, "needGetExaminationRelatedPosition": needGetExaminationRelatedPosition}
        return self.client.get(url=self.url_builder.planhomework_listBigHomeworkItems, params=params)

    def removeBasketContent(self, **kwargs):
        header = \
            {"Content-Type": "application/json"}
        return self.client.post(url=self.url_builder.planhomework_removeBasketContent, headers=header, data=kwargs)

    def addBasketContent(self, resourceType, resourceId, sceneId, category):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "resourceType": resourceType,
                "resourceId": resourceId,
                "sceneId": sceneId,
                "category": category
            }
        return self.client.post(url=self.url_builder.planhomework_addBasketContent, headers=header, data=post_data)

    def saveAssignContents(self, sceneId, contents):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "sceneId": sceneId,
                "contents": [contents]
            }
        return self.client.post(url=self.url_builder.planhomework_saveAssignContents, headers=header, data=post_data)

    def getAssignData(self, sceneId, schoolId):
        header = \
            {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"sceneId": sceneId,
                  "schoolId": schoolId}
        return self.client.get(url=self.url_builder.planhomework_getAssignData, headers=header, params=params)

    def makeStudyPlan(self, sceneId, schoolId, startTime, endTime, restDates, resources, sortType=1):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {"sceneId": sceneId,
             "schoolId": schoolId,
             "sortType": sortType,
             "startTime": startTime,
             "endTime": endTime,
             "restDates": restDates,
             "resources": resources
             }
        return self.client.post(url=self.url_builder.planhomework_makeStudyPlan, headers=header, data=post_data)

    def assignHomework(self, sceneId, schoolId, teacherId, teacherName, title, resources, classType, classes):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {"sceneId": sceneId,
             "schoolId": schoolId,
             "teacherId": teacherId,
             "teacherName": teacherName,
             "title": title,
             "resources": resources,
             "classType": classType,
             "classes": classes
             }
        return self.client.post(url=self.url_builder.planhomework_assignHomework, headers=header, data=post_data)

    def revokeHomework(self, homeworkId):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "homeworkId": homeworkId
            }
        return self.client.post(url=self.url_builder.planhomework_revokeHomework, headers=header, data=post_data)

    def getSceneHomeworks(self):
        header = \
            {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.get(url=self.url_builder.planhomework_getSceneHomeworks, headers=header)

    def getSceneStatInfo(self, sceneId):
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_getSceneStatInfo, params=params)

    def getSceneStatInfo_wx(self, sceneId):
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_getSceneStatInfo_wx, params=params)

    def addBasketItems(self, contents, sceneId):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "sceneId": sceneId,
                "contents": contents
            }
        return self.client.post(url=self.url_builder.planhomework_addBasketItems, headers=header, data=post_data)

    def removeBasketItems(self, contents, sceneId):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "sceneId": sceneId,
                "contents": contents
            }
        return self.client.post(url=self.url_builder.planhomework_removeBasketItems, headers=header, data=post_data)

    def getBasketInfo(self, sceneId):
        header = \
            {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_getBasketInfo, headers=header, params=params)

    def saveHomeworkData(self, sceneId, activityId, contents, daySort=1):
        header = \
            {"Content-Type": "application/json"}
        post_data = \
            {
                "sceneId": sceneId,
                "activityId": activityId,
                "resources": [{"contents": [contents],
                               "daySort": daySort}]
            }
        return self.client.post(url=self.url_builder.planhomework_saveHomeworkData, headers=header, data=post_data)

    def getHomeworkData(self, sceneId):
        header = \
            {"Content-Type": "application/x-www-form-urlencoded"}
        params = {"sceneId": sceneId}
        return self.client.get(url=self.url_builder.planhomework_getHomeworkData, headers=header, params=params)

    # openapi
    def queryTeacherClasses(self, userId):
        header = \
            {"Content-Type": "application/json"}
        post_data = {"userId": userId}
        return self.client.get(url=self.url_builder.queryTeacherClasses, headers=header, params=post_data)
