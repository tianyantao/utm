from lib.api_lib.teacher.teacher_urls import TeacherUrls
import datetime
from common.helper import get_str_md5
from config.config_case import ConfigCase
import time
import requests

now = int(time.time())


class TeacherTyt:

    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()

    def get_homework_detail(self, homeworkId, schoolId):
        data = {"homeworkId": str(homeworkId), "schoolId": schoolId}
        return self.client.post(url=self.url_builder.homework_GetHomeworkDetailInfo, data=data)

    def get_userinfo(self):
        return self.client.post(self.url_builder.userinfo)

    def get_student_userinfo(self):
        return self.client.post(self.url_builder.userinfo_student)

    def get_userinfoforpsychology(self):
        return self.client.post(self.url_builder.userinfoforpsychology)

    def modifyteachername(self, teacherid, teachername):
        data = {'teacherid': int(teacherid), 'teachername': str(teachername)}
        return self.client.post(url=self.url_builder.modifyteachername, data=data)

    def get_permissionmenu(self):
        return self.client.post(self.url_builder.permissionmenu)

    def get_menu(self):
        return self.client.post(self.url_builder.menu)

    def get_naviandmenus(self):
        return self.client.get(self.url_builder.naviandmenus)

    def get_getkemu(self, homeworktype=1):
        post_data = {"homeworktype": homeworktype}
        return self.client.post(self.url_builder.getkemu, data=post_data)

    def get_getteachers(self, type=1, kemu=1):
        post_data = {"type": type, "kemu": kemu}
        return self.client.post(self.url_builder.getteachers, data=post_data)

    def get_getbasketitems(self, kemu=1, page=1, pagesize=10, homeworkxueketype=1):
        post_data = \
            {
                "subjectinput": {
                    "kemu": kemu,
                    "page": page,
                    "pagesize": pagesize
                },
                "homeworkxueketype": homeworkxueketype
            }
        return self.client.post(self.url_builder.getbasketitems, data=post_data)

    def get_app_myhomework(self, page=1, pagesize=40, sid=0, status=1, tid=0):
        params = {"page": page, "pagesize": pagesize, "sid": sid, "status": status, "tid": tid}
        return self.client.get(url=self.url_builder.myhomework_app, params=params, sign_mode=11)

    def get_app_homework_info(self, cid, hid):
        params = {"cid": cid, "hid": hid}
        return self.client.get(url=self.url_builder.homeworkinfo_app, params=params, sign_mode=11)

    def get_getknowledgelist(self, kemu=1):
        post_data = {"kemu": kemu}
        return self.client.post(url=self.url_builder.getknowledgelist, data=post_data)

    def get_getcourses(self, type=1, knowledgeid=0, kemu=1, page=1, teacherid=0, realname="全部", pagesize=10):
        post_data = \
            {
                "type": type,
                "knowledgeid": knowledgeid,
                "kemu": kemu,
                "page": page,
                "pagesize": pagesize,
                "teacherid": teacherid
            }
        return self.client.post(url=self.url_builder.getcourses, data=post_data)

    def addtobasket_xueke(self, qid=0, kemu=1, knowledgeid=0, knowledgetitle='auto', homeworkxueketype=1):
        post_data = \
            {
                "basketaddinputs": [
                    {
                        "qid": qid,
                        "kemu": kemu,
                        "knowledgeid": str(knowledgeid),
                        "knowledgetitle": knowledgetitle
                    }
                ],
                "homeworkxueketype": homeworkxueketype
            }
        return self.client.post(url=self.url_builder.addtobasket, data=post_data)

    def clearbasket(self, homeworkxueketype=1, kemu=1):
        post_data = \
            {
                "clearinput": {
                    "kemu": kemu
                },
                "homeworkxueketype": homeworkxueketype
            }
        return self.client.post(url=self.url_builder.clearbasket, data=post_data)

    def getbasketitems(self, kemu=1, page=1, pagesize=10, homeworkxueketype=1):
        post_data = \
            {
                "subjectinput": {
                    "kemu": kemu,
                    "page": page,
                    "pagesize": pagesize
                },
                "homeworkxueketype": homeworkxueketype
            }
        return self.client.post(url=self.url_builder.getbasketitems, data=post_data)

    def getclasseswithgradeinfo(self, kemu=1, onlyheaderteacher=False, **kwargs):
        post_data = {"kemu": kemu, "onlyheaderteacher": onlyheaderteacher}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.getclasseswithgradeinfo, data=post_data)

    def get_qSearchSubjects(self):
        return self.client.get(url=self.url_builder.qSearch_Subjects)

    def get_qSearchRegions(self):
        return self.client.get(url=self.url_builder.qSearch_Regions)

    def get_qSearchGetJYDegree(self):
        return self.client.get(url=self.url_builder.qSearch_GetJYDegree)

    def get_qSearchGetJYTilei(self):
        return self.client.get(url=self.url_builder.qSearch_GetJYTilei)

    def get_qSearchGetJYSources(self, kemuid=1):
        data = {"kemuid": kemuid}
        return self.client.get(url=self.url_builder.qSearch_GetJYSources, params=data)

    def get_qSearchGetJYCates(self, subject=1):
        data = {"subject": subject}
        return self.client.get(url=self.url_builder.qSearch_GetJYCates, params=data)

    def get_qSearchPoints(self, subject=1):
        data = {"subject": subject}
        return self.client.get(url=self.url_builder.qSearch_Points, params=data)

    def get_qSearchQuestionsByPoint(self, subject=1, Level1=1, Cate=0, Degree=0, GC=False, RC=False, YC=False, EC=False,
                                    Source=0, PO=0, PD=1, PageIndex=1, PageSize=10):
        data = \
            {"subject": subject,
             "Level1": Level1,
             "Cate": Cate,
             "Degree": Degree,
             "GC": GC,
             "RC": RC,
             "YC": YC,
             "EC": EC,
             "Source": Source,
             "PO": PO,
             "PD": PD,
             "PageIndex": PageIndex,
             "PageSize": PageSize
             }
        return self.client.get(url=self.url_builder.qSearch_QuestionsByPoint, params=data)

    # def setxuekehomeworkjson(self, grade=0, expireyear=0, classlist=[], expireyears=[], deadline="",
    #                          title="string_auto", iscgradehomework=False, kemu=0, classtype=0,
    #                          homeworkxueketype=1, classlistsStatus=0, gradeclasses=False, arrangetype=0):
    #     data_json = \
    #         {
    #             "gradeclasses": [
    #                 {
    #                     "grade": grade,
    #                     "expireyear": expireyear,
    #                     "classlist": classlist
    #                 }
    #             ],
    #             "expireyears": expireyears,
    #             "deadline": deadline,
    #             "tittle": title,
    #             "iscgradehomework": iscgradehomework,
    #             "kemu": kemu,
    #             "classtype": classtype,
    #             "classlistsStatus": classlistsStatus,
    #             "arrangetype": arrangetype
    #         }
    #     if gradeclasses == []:
    #         data_json['gradeclasses'] = []
    #     if classlistsStatus is 0:
    #         data_json.pop('classlistsStatus')
    #     data = \
    #         {
    #             "json": '{}'.format(json.dumps(data_json)),
    #             "homeworkxueketype": homeworkxueketype
    #         }
    #     return self.client.post(url=self.url_builder.setxuekehomeworkjson, data=data)

    def get_homeworkrecord(self, HomeworkStatus=0, BeginDate="", EndDate="", Page=1, PageSize=20, gradeexpireyear=0,
                           fixer=0, kemu=0, type=0, Title="", pageDirect=0, pageStart=0, homeworkId=0):
        data = \
            {
                "HomeworkStatus": HomeworkStatus,
                "Page": Page,
                "BeginDate": BeginDate,
                "EndDate": EndDate,
                "gradeexpireyear": gradeexpireyear,
                "fixer": fixer,
                "kemu": kemu,
                "type": type,
                "Title": Title,
                "PageSize": PageSize,
                "pageDirect": pageDirect,
                "pageStart": pageStart,
                "homeworkId": homeworkId
            }
        return self.client.post(url=self.url_builder.homeworkrecord, data=data)

    def deletehomework(self, homeworkids=[]):
        data = {"homeworkids": homeworkids}
        return self.client.post(url=self.url_builder.deletehomework, data=data)



    # def app_GetQuestionIdsByHomeworkId(self, homeworkid):
    #     if self.client.__class__.__name__ == 'EWTAppClient':
    #         token = self.client.get_user_token()
    #         data = \
    #             {
    #                 "sign": get_str_md5(APP_AES_KEY + str(now) + token + APP_AES_KEY),
    #                 "payload": {
    #                     "homeworkid": homeworkid
    #                 },
    #                 "now": str(now),
    #                 "token": token
    #             }
    #         return self.client.post(url=self.url_builder.GetQuestionIdsByHomeworkId, json=data)
    #     else:
    #         token = self.client.get_user_token()
    #         data = \
    #             {
    #                 "sign": get_str_md5(APP_AES_KEY + str(now) + token + APP_AES_KEY),
    #                 "payload": {
    #                     "homeworkid": homeworkid
    #                 },
    #                 "now": str(now),
    #                 "token": token
    #             }
    #         return self.client.post(url=self.url_builder.GetQuestionIdsByHomeworkId, jsons=data)
    #
    # def h5_GetQuestionInfoByQid(self, qid, token):
    #     data = \
    #         {
    #             "qId": qid,
    #             "token": token
    #         }
    #     return self.client.post(url=self.url_builder.GetQuestionInfoByQid, data=data)
    #
    # def submithomeworkpaper_mobi(self, userid, groupid, homeworkid, qid=0, usetime=10, homewordflag=1, platform=1,
    #                              QuestionAnswerImageIds=None, UserAnswerResult=0, answer="A", Answer=None):
    #     now = int(time.time())
    #     if Answer:
    #         data = \
    #             {
    #                 "sign": get_str_md5(APP_AES_KEY + str(now) + self.client.get_user_token() + APP_AES_KEY),
    #                 "payload": {
    #                     "UserID": userid,
    #                     "Answer": Answer,
    #                     "PaperID": homeworkid,
    #                     "GroupID": groupid,
    #                     "UseTime": usetime,
    #                     "Platform": platform,
    #                     "HomeworkFlag": homewordflag
    #                 },
    #                 "now": now,
    #                 "token": self.client.get_user_token()
    #             }
    #     else:
    #         data = \
    #             {
    #                 "sign": get_str_md5(APP_AES_KEY + str(now) + self.client.get_user_token() + APP_AES_KEY),
    #                 "payload": {
    #                     "UserID": userid,
    #                     "Answer": [
    #                         {
    #                             "QuestionAnswerImageIds": QuestionAnswerImageIds,
    #                             "Qid": qid,
    #                             "UserAnswerResult": UserAnswerResult,
    #                             "Answer": answer
    #                         }
    #                     ],
    #                     "PaperID": homeworkid,
    #                     "GroupID": groupid,
    #                     "UseTime": usetime,
    #                     "Platform": platform,
    #                     "HomeworkFlag": homewordflag
    #                 },
    #                 "now": now,
    #                 "token": self.client.get_user_token()
    #             }
    #     return self.client.post(url=self.url_builder.submithomeworkpaper_mobi, json=data)
    #
    # def submithomeworkpaper_student_pc(self, groupid, paperid, userid, platform=1, usetime=24, homeworkflag=1,
    #                                    answer=None):
    #     data = \
    #         {"AnswerQuestionModel":
    #              {"GroupID": groupid,
    #               "UserID": userid,
    #               "PaperID": paperid,
    #               "UseTime": usetime,
    #               "Platform": platform,
    #               "HomeworkFlag": homeworkflag,
    #               "Answer": answer
    #               }}
    #     return self.client.post(url=self.url_builder.submithomeworkpaper_student, data=data)
    #
    # def uploadSubjectiveAnswerPic(self, token):
    #     import os
    #     p = os.path.split(__file__)
    #     data = {"token": token}
    #     files = {"filename": open("{}/TestData/upload_pic.jpg".format(p[0]), "rb")}
    #     # files = {"filename": open("./TestData/upload_pic.jpg", "rb")}
    #     return self.client.post(url=self.url_builder.UploadSubjectiveAnswerPic, data=data, files=files)

    def get_homeworkinfo_teacher(self, homeworkid):
        data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.homeworkinfo_teacher, data=data)

    # def get_HomeworkRecordClasses(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.post(url=self.url_builder.HomeworkRecordClasses, data=data)
    #
    # def get_ClassHomeworkCompletion(self, homeworkid, classid, sort=1, page=1, pagesize=10, studentname=None):
    #     data = {"homeworkid": homeworkid, "sort": sort, "page": page, "pagesize": pagesize, "classid": classid,
    #             "studentname": studentname}
    #     return self.client.post(url=self.url_builder.ClassHomeworkCompletion, data=data)
    #
    # def get_homeworkcompletion_exercises(self, homeworkid, sort=3, page=1, pagesize=15):
    #     data = {"sort": sort, "homeworkid": homeworkid, "page": page, "pagesize": pagesize}
    #     return self.client.post(url=self.url_builder.homeworkcompletion_exercises, data=data)
    #
    # def get_uncompleted(self, homeworkid, classid=0, page=1, pagesize=15):
    #     data = {"homeworkid": homeworkid, "classid": classid, "page": page, "pagesize": pagesize}
    #     return self.client.post(url=self.url_builder.UnCompleted, data=data)
    #
    # def get_gethomeworkpaperreport_teacher(self, groupid, homeworkid, userid, platform=1):
    #     data = {"HomeworkID": homeworkid, "GroupID": groupid, "UserID": userid, "Platform": platform}
    #     return self.client.post(url=self.url_builder.gethomeworkpaperreport_teacher, data=data)
    #
    # def get_gethomeworkpaperreport_student(self, groupid, homeworkid, userid, platform=1):
    #     data = {"HomeworkID": homeworkid, "GroupID": groupid, "UserID": userid, "Platform": platform}
    #     return self.client.post(url=self.url_builder.gethomeworkpaperreport_student, data=data)
    #
    # def get_courserecommendations4fraud(self, post_data):
    #     return self.client.post(url=self.url_builder.courserecommendations4fraud, data=post_data)
    #
    # def searchschoolclasses(self, token, schoolid=0, gradeyear=0):
    #     data = {"schoolId": schoolid, "gradeYear": gradeyear}
    #     headers = {}
    #     if token:
    #         headers["ettoken"] = token
    #     return self.client.post(url=self.url_builder.searchschoolclasses, headers=headers, data=data)
    #
    # def getQuestionListByHomeworkId(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.post(url=self.url_builder.GetQuestionListByHomeworkId, data=data)
    #
    # def get_analysis(self, questionid):
    #     data = {"questionId": questionid}
    #     return self.client.get(url=self.url_builder.analysis_xueke_pc, params=data)
    #
    # def submitjoinclassdata(self, classId, masterName, studentName):
    #     data = {"classId": classId, "studentName": studentName, "masterName": masterName}
    #     return self.client.post(url=self.url_builder.submitjoinclassdata, data=data)
    #
    # def winter2019_getuserrole(self, teacherid=None):
    #     if teacherid:
    #         data = {"teacherid": teacherid}
    #     else:
    #         data = {}
    #     return self.client.post(url=self.url_builder.winter2019_getuserrole, data=data)
    #
    # def winter2019_getprerecordinfos(self, ettoken, schoolid=0, expireyear=0, teacherid=0, topichomeworktype=0):
    #     data = \
    #         {
    #             "schoolid": schoolid,
    #             "grade": expireyear,
    #             "teacherid": teacherid,
    #             "topichomeworktype": topichomeworktype
    #         }
    #     headers = {}
    #     if ettoken:
    #         headers["ettoken"] = ettoken
    #     return self.client.post(url=self.url_builder.winter2019_getprerecordinfos, headers=headers, data=data)
    #
    # def winter2019_setstandardhomework(self, ettoken, schoolid, grade, teacherid,
    #                                    deadline=int(time.time()) * 1000 + 90000000, classids=[], **kwargs):
    #     data = \
    #         {
    #             "schoolid": schoolid,
    #             "grade": grade,
    #             "classids": classids,
    #             "teacherid": teacherid,
    #             "deadline": deadline
    #         }
    #     data.update(kwargs)
    #     headers = {}
    #     if ettoken:
    #         headers["ettoken"] = ettoken
    #     return self.client.post(url=self.url_builder.winter2019_setstandardhomework, headers=headers, data=data)
    #
    # def winter2019_setgradepersonalizedhomework(self, ettoken, schoolid, grade, teacherid,
    #                                             deadline=int(time.time()) * 1000 + 90000000):
    #     data = \
    #         {
    #             "schoolid": schoolid,
    #             "grade": grade,
    #             "teacherid": teacherid,
    #             "deadline": deadline
    #         }
    #     headers = {}
    #     if ettoken:
    #         headers["ettoken"] = ettoken
    #     return self.client.post(url=self.url_builder.winter2019_setgradepersonalizedhomework, headers=headers,
    #                             data=data)
    #
    # def winter2019_getpersonalquestionsinfos(self, studentid, homeworkid):
    #     data = \
    #         {
    #             "studentid": studentid,
    #             "homeworkid": homeworkid
    #         }
    #     return self.client.post(url=self.url_builder.winter2019_getpersonalquestionsinfos, data=data)
    #
    # def winter2019_studentanswer(self, studentid, homeworkid):
    #     data = \
    #         {
    #             "studentid": studentid,
    #             "homeworkid": homeworkid
    #         }
    #     return self.client.post(url=self.url_builder.winter2019_studentanswer, data=data)
    #
    # def winter2019_getquestionrecommends(self, questionid, homeworkid):
    #     data = \
    #         {
    #             "questionid": questionid,
    #             "homeworkid": homeworkid
    #         }
    #     return self.client.post(url=self.url_builder.winter2019_getquestionrecommends, data=data)
    #
    # def winter2019_pointanswerrate(self, studentid, homeworkid, ettoken=None):
    #     data = \
    #         {
    #             "studentid": studentid,
    #             "homeworkid": homeworkid
    #         }
    #     headers = {}
    #     if ettoken:
    #         headers["ettoken"] = ettoken
    #     return self.client.post(url=self.url_builder.winter2019_pointanswerrate, headers=headers, data=data)
    #
    # def app_gethomeworksetlist(self, homeworkid, page=1, pagesize=20, version="6.4.1"):
    #     token = self.client.get_user_token()
    #     data = \
    #         {
    #             "sign": get_str_md5(APP_AES_KEY + str(now) + token + APP_AES_KEY),
    #             "payload": {
    #                 "page": page,
    #                 "pagesize": pagesize,
    #                 "homeworkid": str(homeworkid)
    #             },
    #             "now": str(now),
    #             "token": token
    #         }
    #     headers = {"version": version}
    #     return self.client.post(url=self.url_builder.gethomeworksetlist, json=data, headers=headers)

    def getsbrpaperquestioncard(self, homeworkid):
        token = self.client.user_token
        data = \
            {
                "sign": get_str_md5(ConfigCase.APP_AES_KEY + str(now) + token + ConfigCase.APP_AES_KEY),
                "payload": {
                    "homeworkid": str(homeworkid)
                },
                "now": str(now),
                "token": token
            }
        return self.client.post(url=self.url_builder.getsbrpaperquestioncard, data=data)

    def submitSbrPaperAnswer(self, homeworkid, paperid, timespend=775,
                             answers=[{"answerindexes": [0], "syllabusno": 1, "no": 1}]):
        token = self.client.user_token
        data = \
            {
                "sign": get_str_md5(ConfigCase.APP_AES_KEY + str(now * 1000) + token + ConfigCase.APP_AES_KEY),
                "payload": {
                    "homeworkid": homeworkid,
                    "paperid": paperid,
                    "timespend": timespend,
                    "answers": answers
                },
                "now": str(now * 1000),
                "token": token
            }
        return self.client.post(url=self.url_builder.SubmitSbrPaperAnswer, data=data)

    def get_homeworklist_student_pc(self, homeworkstatus=0, pagesize=20, page=1, homeworksubject=0, homeworktype=0):
        data = \
            {
                "homeworkstatus": homeworkstatus,
                "pagesize": pagesize,
                "page": page,
                "homeworksubject": homeworksubject,
                "homeworktype": homeworktype
            }
        return self.client.post(url=self.url_builder.homeworklist, data=data)

    # def get_homeworkvideolist_pc(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.post(url=self.url_builder.homeworkvideolist, data=data)
    #
    def getSbrPaperExam_pc(self, groupid, homeworkid, homeworkflag=1):
        data = "gid={0}&hid={1}&homeworkflag={2}".format(groupid, homeworkid, homeworkflag)
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        return self.client.post(url=self.url_builder.GetSbrPaperExam, data=data, headers=headers)

# todo: bug：
    def submitSbrPaperExam_pc(self, homeworkid, studentid, groupid, answer, AnswerDurationStr='00:00:05',
                              HomeworkFlag=1):
        data = "HomeworkID={0}&StudentId={1}&GroupID={2}&AnswerDurationStr={3}&HomeworkFlag={4}&AnswerRecordList={5}".format(homeworkid,
                                                                                                           studentid,
                                                                                                           groupid,
                                                                                                           AnswerDurationStr,
                                                                                                           HomeworkFlag,
                                                                                                           answer)
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        return self.client.post(url=self.url_builder.SubmitSbrPaperExam_pc, data=data, headers=headers)

    def evaluation_sethomework(self, evaluationid, scopetype, gradescope, classscope=[], deadlinetime=str(
        datetime.datetime.now().date() + datetime.timedelta(days=2)) + ' 00:00:00', title='test'):
        data = \
            {
                "evaluationid": evaluationid,
                "scopetype": scopetype,
                "gradescope": gradescope,
                "classscope": classscope,
                "deadlinetime": deadlinetime,
                "title": title
            }
        return self.client.post(url=self.url_builder.evaluation_sethomework, data=data)

    def evaluation_GetHomeworkLogList(self, scopetype=0, expireyear=0, homeworkstatus=0, pagesize=60, page=1,
                                      searchendtime='', searchbegintime=''):
        data = \
            {
                "scopetype": scopetype,
                "expireyear": expireyear,
                "homeworkstatus": homeworkstatus,
                "Pagesize": pagesize,
                "Page": page,
                "searchbegintime": searchbegintime,
                "searchendtime": searchendtime
            }
        return self.client.post(url=self.url_builder.evaluation_GetHomeworkLogList, data=data)

    def evaluation_deletehomework(self, homeworkid):
        url = self.url_builder.evaluation_deletehomework + '?homeworkid=' + str(homeworkid)
        return self.client.post(url=url)

    def get_psychology_html(self):
        return self.client.get(url=self.url_builder.psychology_html)

    def evaluation_GetEvaluationList(self):
        return self.client.post(url=self.url_builder.evaluation_GetEvaluationList)

    def evaluation_GetEvaluationDetail(self, evaluationId):
        data = {"evaluationId": evaluationId}
        return self.client.post(url=self.url_builder.evaluation_GetEvaluationDetail, data=data)

    def evaluation_GradeClassStateInfo(self, evaluationId):
        data = {"evaluationId": evaluationId}
        return self.client.post(url=self.url_builder.evaluation_GradeClassStateInfo, data=data)

    def evaluation_GetClassCompletion(self, homeworkid, page=1, pagesize=20):
        data = \
            {
                "homeworkid": homeworkid,
                "page": page,
                "pagesize": pagesize
            }
        return self.client.post(url=self.url_builder.evaluation_GetClassCompletion, data=data)

    # def career_postheadertypelist(self, newclsid=10):
    #     data = \
    #         {"newclsid": newclsid}
    #     return self.client.post(url=self.url_builder.career_postheadertypelist, data=data)
    #
    # def career_gethomworklist(self, typeid=10, parentid=17, childid=17, pageindex=1, pagesize=10):
    #     data = \
    #         {"typeid": typeid,
    #          "parentid": parentid,
    #          "pageindex": pageindex,
    #          "childid": childid,
    #          "pagesize": pagesize
    #          }
    #     return self.client.post(url=self.url_builder.career_gethomworklist, data=data)
    #
    # def career_addbasket(self, qids=[], kemu=10, typeid=1):
    #     data = \
    #         {
    #             "basketforteaaddinput": []
    #         }
    #     for qid in qids:
    #         data['basketforteaaddinput'].append({
    #             "qid": qid,
    #             "kemu": kemu,
    #             "typeid": typeid
    #         })
    #     return self.client.post(url=self.url_builder.career_addbasket, data=data)
    #
    # def career_clearbasket(self, typeid=1, kemu=10):
    #     data = \
    #         {
    #             "typeid": typeid,
    #             "kemu": kemu
    #         }
    #     return self.client.post(url=self.url_builder.career_clearbasket, data=data)
    #
    # def career_getbaseketvideolist(self, typeid=1, kemu=10):
    #     data = \
    #         {
    #             "typeid": typeid,
    #             "kemu": kemu
    #         }
    #     return self.client.post(url=self.url_builder.career_getbaseketvideolist, data=data)

    def career_getgradeandclassinfo(self):
        return self.client.post(url=self.url_builder.career_getgradeandclassinfo, data={})

    # def career_submithomework(self, homeworkxueketype=1, submiting=False, title='', iscgradehomework=True, kemu=10,
    #                           classtype=1, expireyears=[], gradeclasses=[], deadline=''):
    #     data = \
    #         {
    #             "homeworkxueketype": homeworkxueketype,
    #             "submiting": submiting,
    #             "json": '{}'.format(json.dumps({
    #                 "tittle": title,
    #                 "iscgradehomework": iscgradehomework,
    #                 "deadline": deadline,
    #                 "kemu": kemu,
    #                 "classtype": classtype,
    #                 "expireyears": expireyears,
    #                 "gradeclasses": gradeclasses
    #             }))
    #         }
    #     return self.client.post(url=self.url_builder.career_submithomework, data=data)
    #
    def homeworkservice_getuserrole(self, teacherid=None, token=None):
        if teacherid:
            data = {"teacherid": teacherid}
        else:
            data = {}
        headers = {}
        if token:
            headers["ettoken"] = token
        return self.client.post(url=self.url_builder.homeworkservice_getuserrole, data=data, headers=headers)

    def modifystudentinfo(self, studentname='test'):
        data = {"StudentName": studentname}
        return self.client.post(url=self.url_builder.modifystudentinfo, data=data)

    def get_studentname(self):
        return self.client.post(url=self.url_builder.getstudentname)
    #
    # def homeworkservice_homeworkrecordclasses(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.post(url=self.url_builder.homeworkservice_homeworkrecordclasses, data=data)
    #
    # def homeworkservice_getpapaerinfo(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.post(url=self.url_builder.homeworkservice_getpapaerinfo, data=data)
    #
    # def homeworkservice_getexercisehomeworclasscompletion(self, homeworkid, page=1, pagesize=15, sort=3):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "page": page,
    #             "pagesize": pagesize,
    #             "sort": sort
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_getexercisehomeworclasscompletion, data=data)
    #
    # def homeworkservice_xueKeClassHomeworkStudentCompletion(self, homeworkid, classid, page=1, pagesize=10, sort=1,
    #                                                         studentname=None):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "classid": classid,
    #             "page": page,
    #             "pagesize": pagesize,
    #             "sort": sort,
    #             "studentname": studentname
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_xueKeClassHomeworkStudentCompletion, data=data)
    #
    # def homeworkservice_teacherKnowledgeErrorRate(self, homeworkid, classid=0):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "classid": classid
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_teacherKnowledgeErrorRate, data=data)
    #
    # def homeworkservice_GetPersonalQuestionsInfos(self, homeworkid, sort=1):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "sort": sort
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_GetPersonalQuestionsInfos, data=data)
    #
    # def homeworkservice_GetPaperErrorStudentsWithErrorRate(self, homeworkid, classid=0):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "classid": classid
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_GetPaperErrorStudentsWithErrorRate, data=data)
    #
    # def homeworkservice_GetPaperQuestionErrorStudents(self, homeworkid, questionid, classid=0, page=1, pagesize=10):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "classid": classid,
    #             "page": page,
    #             "pagesize": pagesize,
    #             "questionid": questionid
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_GetPaperQuestionErrorStudents, data=data)
    #
    # def homeworkservice_uncompleted(self, homeworkid, classid=0, page=1, pagesize=15):
    #     data = \
    #         {
    #             "homeworkid": homeworkid,
    #             "classid": classid,
    #             "page": page,
    #             "pagesize": pagesize
    #         }
    #     return self.client.post(url=self.url_builder.homeworkservice_uncompleted, data=data)
    #
    # # 卷库v2.0：
    # def paper_papertype(self):
    #     return self.client.post(url=self.url_builder.paper_papertype)
    #
    # def paper_kemu(self, papertype=''):
    #     data = {"papertype": papertype}
    #     return self.client.post(url=self.url_builder.paper_kemu, data=data)

    def paper_GetUserSubjects(self):
        return self.client.post(url=self.url_builder.paper_GetUserSubjects, data={})

    # def paper_GetPaperDetailInfo(self, paperid):
    #     data = {"paperid": paperid}
    #     return self.client.get(url=self.url_builder.paper_GetPaperDetailInfo, params=data)
    #
    # def paper_Sorts(self):
    #     return self.client.post(url=self.url_builder.paper_Sorts)
    #
    # def paper_TextBook(self, subjectid):
    #     data = {"subjectid": subjectid}
    #     return self.client.post(url=self.url_builder.paper_TextBook, data=data)
    #
    # def paper_Degree(self, type=''):
    #     data = {"type": type}
    #     return self.client.post(url=self.url_builder.paper_Degree, data=data)
    #
    # def paper_year(self, type=''):
    #     data = {"type": type}
    #     return self.client.post(url=self.url_builder.paper_year, data=data)
    #
    # def paper_area(self, type=''):
    #     data = {"type": type}
    #     return self.client.post(url=self.url_builder.paper_area, data=data)
    #
    # def paper_Semester(self, type=''):
    #     data = {"type": type}
    #     return self.client.post(url=self.url_builder.paper_Semester, data=data)
    #
    def paper_SetPaperHomeWork(self, expireyears=[], grade=0, expireyear=0, classlist=[], classtype=1, deadline=0,
                               iscgradehomework=False, kemu=1, paperids=[], title='testauto卷库', arrangetype=0, **kwargs):
        # 如果是年级作业，需要传ExpireYears(过期年份)，iscgradehomework：true,ClassList: []，classtype(1是行政班，2是教学班)
        if not iscgradehomework:
            post_data = \
                {
                    "expireyears": expireyears,
                    "gradeclasses": [
                        {
                            "grade": grade,
                            "expireyear": expireyear,
                            "classlist": classlist
                        }
                    ],
                    "classtype": classtype,
                    "deadline": deadline,
                    "iscgradehomework": iscgradehomework,
                    "paperids": paperids,
                    "tittle": title,
                    "kemu": kemu,
                    "arrangetype": arrangetype
                }
        else:
            post_data = \
                {
                    "expireyears": expireyears,
                    "gradeclasses": [],
                    "classtype": classtype,
                    "deadline": deadline,
                    "iscgradehomework": iscgradehomework,
                    "paperids": paperids,
                    "tittle": title,
                    "kemu": kemu,
                    "arrangetype": arrangetype
                }
        for k in kwargs:
            post_data[k] = kwargs[k]
        return self.client.post(url=self.url_builder.paper_SetPaperHomeWork, data=post_data)
    #
    # def paper_GetPaperHomeworkDetailInfo(self, homeworkid):
    #     data = {"homeworkid": homeworkid}
    #     return self.client.get(url=self.url_builder.paper_GetPaperHomeworkDetailInfo, params=data)
    #
    # def paper_papers(self, type='1,4', subjectid=1, sortid=1, page=1, pagesize=20, textbook='', degreeid=0, yearid=0,
    #                  areaid=0, semesterid=0, wenli='0'):
    #     data = \
    #         {
    #             "type": type,
    #             "subjectid": subjectid,
    #             "sortid": sortid,
    #             "page": page,
    #             "pagesize": pagesize,
    #             "textbook": textbook,
    #             "degreeid": degreeid,
    #             "yearid": yearid,
    #             "areaid": areaid,
    #             "semesterid": semesterid,
    #             "wenli": wenli
    #         }
    #     return self.client.post(url=self.url_builder.paper_papers, data=data)

    # B端地图

    def hp_getclasseswithgradeinfo(self, actiontype=2, promotionmoduletype=1):
        data = {"actiontype": actiontype, "promotionmoduletype": promotionmoduletype}
        return self.client.post(url=self.url_builder.hp_getclasseswithgradeinfo, data=data)

    def hp_grades(self):
        return self.client.post(url=self.url_builder.hp_grades, data={})

    def hp_GetTimeAxis(self, grade=1):
        data = {"grade": grade}
        return self.client.post(url=self.url_builder.hp_GetTimeAxis, data=data)

    # 章节选题
    def qSearch_TextbookEditions(self, subject=1):
        data = {"subject": subject}
        return self.client.get(url=self.url_builder.qSearch_TextbookEditions, params=data)

    def qSearch_Years(self, kemuid=1):
        data = {"kemuid": kemuid}
        return self.client.get(url=self.url_builder.qSearch_Years, params=data)

    def qSearch_ConciseTextbooks(self, subject=1, bookEditionId=1):
        data = {"subject": subject, "bookEditionId": bookEditionId}
        return self.client.get(url=self.url_builder.qSearch_ConciseTextbooks, params=data)

    def qSearch_Textbooks(self, subject=1, bookEditionId=1):
        data = {"subject": subject, "bookEditionId": bookEditionId}
        return self.client.get(url=self.url_builder.qSearch_Textbooks, params=data)

    def qSearch_Categorys(self, subject=1, bookEditionId=1, bookId=1):
        data = {"subject": subject, "bookEditionId": bookEditionId, "bookId": bookId}
        return self.client.get(url=self.url_builder.qSearch_Categorys, params=data)

    def qSearch_QuestionsByChapter(self, subject, bookid, ChapterID, PageIndex=1, PageSize=10, YR=2019, **kwargs):
        data = \
            {"subject": subject,
             "BookID": bookid,
             "ChapterID": ChapterID,
             "PageIndex": PageIndex,
             "PageSize": PageSize,
             "YR": YR
             }
        for k in kwargs:
            data[k] = kwargs[k]
        return self.client.get(url=self.url_builder.qSearch_QuestionsByChapter, params=data)

    def student_unclosed_homeworks(self, page=1, pagesize=10):
        headers = {}
        headers['userid'] = str(self.client.user_id)
        headers['token'] = self.client.user_token
        headers['now'] = str(now)
        body = {}
        body['page'] = page
        body['pagesize'] = pagesize
        return self.client.post(url=self.url_builder.homeworkservice_StudentUnClosedHomeworks, headers=headers, data=body)


    # def receive_paper_report(self, extid, paperid, reportid, answerstatus, userid):
    #     headers = \
    #         {"now": str(now),
    #          "sign": get_str_md5(WEB_TEACHER_KEY+str(now)+WEB_TEACHER_KEY)
    #          }
    #     body = \
    #         {
    #             "extid": extid,
    #             "paperid": paperid,
    #             "userreports": []
    #         }
    #     body['userreports'].append({
    #                 "reportid": reportid,
    #                 "userid": userid,
    #                 "answerstatus": answerstatus
    #             })
    #     return self.client.post(url=self.url_builder.receive_paper_report, data=body, headers=headers)

    def receive_paper_report(self, **kwargs):
        headers = \
            {"now": str(now),
             "sign": get_str_md5(ConfigCase.WEB_TEACHER_KEY+str(now)+ConfigCase.WEB_TEACHER_KEY)
             }
        return self.client.post(url=self.url_builder.receive_paper_report, data=kwargs, headers=headers)


    def holidayprod_getAssignState(self):
        return self.client.get(url=self.url_builder.holidayprod_getAssignState)

    def holidayprod_getCategoryTree(self):
        return self.client.get(url=self.url_builder.holidayprod_getCategoryTree)

    def holidayprod_getAssignDetail(self):
        return self.client.get(url=self.url_builder.holidayprod_getAssignDetail)

    def holidayprod_assign(self):
        pass

    def basket_remove(self, ids, category="1", homeworkType="1"):
        data = \
            {
                "category": category,
                "homeworkType": homeworkType,
                "ids": ids
            }
        return self.client.post(url=self.url_builder.basket_remove, data=data)

    def basket_add(self, ids, category="1", homeworkType="1"):
        data = \
            {
                "category": category,
                "homeworkType": homeworkType,
                "ids": ids
            }
        return self.client.post(url=self.url_builder.basket_add, data=data)

    def basket_listallexercise(self, category="1", homeworkType="1"):
        data = \
            {
                "category": category,
                "homeworkType": homeworkType
            }
        return self.client.post(url=self.url_builder.basket_listallexercise, data=data)

    def basket_listall(self, category="1", homeworkType="1"):
        data = \
            {
                "category": category,
                "homeworkType": homeworkType
            }
        return self.client.post(url=self.url_builder.basket_listall, data=data)

    def sethomework(self, components, gradeClasses, deadline, arrangeType=0, classType=1, expireYears=[], isGradeHomework=False, subject='1', **kwargs):
        data = \
            {"arrangeType": arrangeType,
             "classType": classType,
             "components": components,
             "isGradeHomework": isGradeHomework,
             "deadline": deadline,
             "subject": subject,
             "expireYears": expireYears,
             "gradeClasses": gradeClasses
             }
        for k in kwargs:
            data[k] = kwargs[k]
        return self.client.post(url=self.url_builder.sethomework, data=data)

    def oa_oauth(self, uid, schoolid, timespan, sign):
        params = {
            "uid": uid,
            "schoolid": schoolid,
            "timespan": timespan,
            "sign": sign
        }
        return self.client.get(url=self.url_builder.oaview_oauth, params=params, verify=False)

    def oa_disband(self, schoolid, groupid):
        params = {
            "schoolid": schoolid,
            "groupid": groupid
        }
        return self.client.post(url=self.url_builder.oaview_disband, data=params, verify=False)

    def oa_classlist(self, schoolid, page=1, pagesize=100):
        params = {
            "schoolID": schoolid,
            "page": page,
            "pagesize": pagesize
        }
        return self.client.get(url=self.url_builder.oaview_classlist, params=params, verify=False)

    def oa_schoollist(self):
        return self.client.get(url=self.url_builder.oaview_schoollist, verify=False)

    def oa_addSchoolLeader(self, mobile, schoolID, expireYear, name='auto_principal', account='', duty='auto_duty'):
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        data = 'mobile={0}&account={1}&name={2}&duty={3}&schoolID={4}&expireYear={5}'.format(mobile, account, name,
                                                                                             duty, schoolID, expireYear)
        return self.client.post(url=self.url_builder.oaview_AddSchoolLeader, data=data, headers=headers, verify=False)

    def oa_addGradeLeader(self, mobile, schoolID, expireYear, name='auto_principal', account='', duty='auto_duty'):
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        data = 'mobile={0}&account={1}&name={2}&duty={3}&schoolID={4}&expireYear={5}'.format(mobile, account, name,
                                                                                             duty, schoolID, expireYear)
        return self.client.post(url=self.url_builder.oaview_AddGradeLeader, data=data, headers=headers, verify=False)

    def oa_ModifyClass(self, name, type, expireYear, schoolid, sequence=0, teacheraccount='', teachermobile='',
                       teachername='', JoinClassControl='0', UpdateStudentNameControl=False):
        data = {"sequence": sequence, "name": name, "expireYear": expireYear, "schoolid": schoolid,
                "teacheraccount": teacheraccount,
                "teachermobile": teachermobile, "teachername": teachername, "type": type,
                "JoinClassControl": JoinClassControl,
                "UpdateStudentNameControl": UpdateStudentNameControl}
        return self.client.post(url=self.url_builder.oaview_ModifyClass, data=data, verify=False)

    def getteacheruserrole(self, userid):
        header = {"Content-Type": "application/json"}
        header["now"] = str(now)
        header["sign"] = get_str_md5(ConfigCase.WEB_TEACHER_KEY+str(now)+ConfigCase.WEB_TEACHER_KEY)
        data = {"userid": userid}
        return self.client.post(url=self.url_builder.getTeacherUserRole, headers=header, data=data)

    def get_user_manager_role(self, userid):
        header = {}
        header["now"] = str(now)
        header["sign"] = get_str_md5(ConfigCase.WEB_TEACHER_KEY + str(now) + ConfigCase.WEB_TEACHER_KEY)
        data = {"userid": userid}
        return self.client.post(url=self.url_builder.GetUserManagerRole, headers=header, data=data)
        # header = {"Content-Type": "application/json"}
        # if ettoken:
        #     header["ettoken"] = ettoken
        # data = data  # {"userid": xxxxxxx}
        # return self.client.post(url=self.url_builder.GetUserManagerRole, headers=header, data=data)

    def get_user_manager_and_class_role(self, userid):
        header = {}
        header["now"] = str(now)
        header["sign"] = get_str_md5(ConfigCase.WEB_TEACHER_KEY + str(now) + ConfigCase.WEB_TEACHER_KEY)
        data = {"userid": userid}
        return self.client.post(url=self.url_builder.GetUserManagerAndClassRole, headers=header, data=data)

    def oa_LoadLeaderList(self,SchoolId):
        data = {"SchoolId":SchoolId}
        return self.client.post(url=self.url_builder.oaview_LoadLeaderList, data=data, verify=False)

    # strategy系统：
    def strategy_rank_all(self, solutionId, activityId, pageNum=1, pageSize=20):
        params = {
            "solutionId": solutionId,
            "activityId": activityId,
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        return self.client.get(url=self.url_builder.rank_all, params=params)

    def strategy_rank_person(self, solutionId, activityId, userId):
        params = {
            "solutionId": solutionId,
            "activityId": activityId,
            "userId": userId,
        }
        return self.client.get(url=self.url_builder.rank_person, params=params)

    def strategy_activity_user_list(self, userId, activityIds):
        data = {
            "userId": userId,
            "activityIds": activityIds
        }
        return self.client.post(url=self.url_builder.activity_user_list, data=data)

    # 校本试卷升级
    def sbr_getSbrHomeworkInfo4Answer(self, homeworkid):
        return self.client.get(url=self.url_builder.getSbrHomeworkInfo4Answer, params={"homeworkId": homeworkid})

    def sbr_submitQuestionAnswers(self, data):
        return self.client.post(url=self.url_builder.submitQuestionAnswers, data=data)

    def sbr_SubmitQuestionAnswerRating(self, data):
        return self.client.post(url=self.url_builder.SubmitQuestionAnswerRating, data=data)

    def sbr_GetSbrHomeworkInfo4SelfRating(self, homeworkid):
        return self.client.get(url=self.url_builder.GetSbrHomeworkInfo4SelfRating, params={"homeworkId": homeworkid})

    def sbr_GetStudentSbrHomeworkReport(self, homeworkid):
        return self.client.get(url=self.url_builder.GetStudentSbrHomeworkReport, params={"homeworkId": homeworkid})

    def sbr_GetExamPaperStaticByPaperId(self, homeworkid, classid=0):
        data = {
            "homeworkid": homeworkid,
            "classid": classid
        }
        return self.client.post(url=self.url_builder.GetExamPaperStaticByPaperId, data=data)

    def sbr_SubmitSubjectiveFileUrls(self, answerCardId, paperId, **kwargs):
        post_data = {"answerCardId": answerCardId, "paperId": paperId}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.SubmitSubjectiveFileUrls, data=post_data)

    # 用户权限重构
    def queryMenuInfo(self, schoolid):
        return self.client.get(url=self.url_builder.queryMenuInfo, params={"schoolId": schoolid})

    def queryTeacherRoleAndSchoolInfo(self, schoolid):
        return self.client.get(url=self.url_builder.queryTeacherRoleAndSchoolInfo, params={"schoolId": schoolid})

    def getSchoolUserInfo(self):
        return self.client.get(url=self.url_builder.getSchoolUserInfo)

    def queryCurrentSchoolConf(self):
        return self.client.get(url=self.url_builder.queryCurrentSchoolConf)

    def querySchoolInfo(self):
        return self.client.get(url=self.url_builder.querySchoolInfo)

    # 题卷库升级
    def homeworkprod_getQuestionSubject(self, schoolid):
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionSubject, params={"schoolId": schoolid})

    def homeworkprod_getQuestionProvince(self, schoolid):
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionProvince, params={"schoolId": schoolid})

    def homeworkprod_listQuestionBasketItems(self, schoolId, basketType=2, category=1, subjectId=1):
        params = {
            "basketType": basketType,
            "category": category,
            "subjectId": subjectId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_listQuestionBasketItems, params=params)

    def homeworkprod_getQuestionBookBySubject(self, schoolId, subjectEn="chinese2"):
        params = {
            "subjectEn": subjectEn,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionBookBySubject, params=params)

    def homeworkprod_getQuestionChapterByBook(self, schoolId, bookId, subjectEn="chinese2"):
        params = {
            "subjectEn": subjectEn,
            "bookId": bookId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionChapterByBook, params=params)

    def homeworkprod_getQuestionFilterList(self, schoolId, subjectEn="chinese2"):
        params = {
            "subjectEn": subjectEn,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionFilterList, params=params)

    def homeworkprod_getQuestionPointBySubject(self, schoolId, subjectEn="chinese2"):
        params = {
            "subjectEn": subjectEn,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionPointBySubject, params=params)

    def homeworkprod_pageQueryQuesAtChapterOrPoint(self, post_data):
        return self.client.post(url=self.url_builder.homeworkprod_pageQueryQuesAtChapterOrPoint, data=post_data)

    def homeworkprod_querySameQues(self, subjectEn, id, schoolid, ps=10):
        params = {
            "subjectEn": subjectEn,
            "schoolId": schoolid,
            "id": id,
            "ps": ps
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionPointBySubject, params=params)

    def homeworkprod_queryQuestionDetail(self, subjectEn, queryType, schoolid, questionId):
        params = {
            "subjectEn": subjectEn,
            "schoolId": schoolid,
            "queryType": queryType,
            "questionId": questionId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionPointBySubject, params=params)

    def homeworkprod_getPaperTreeCategory(self, subjectId, schoolId):
        params = {
            "subjectId": subjectId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getPaperTreeCategory, params=params)

    def homeworkprod_getPaperTreeByChapterId(self, chapterId, schoolId):
        params = {
            "chapterId": chapterId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getPaperTreeByChapterId, params=params)

    def homeworkprod_getChapterFilterPaperType(self, chapterId, schoolId):
        params = {
            "chapterId": chapterId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getChapterFilterPaperType, params=params)

    def homeworkprod_pagePaper(self, post_data):
        return self.client.post(url=self.url_builder.homeworkprod_pagePaper, data=post_data)

    def homeworkprod_getPaperInfo(self, paperId, schoolId):
        params = {
            "paperId": paperId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getPaperInfo, params=params)

    # def homeworkprod_getQuestionBookBySubject(self, subjectId, subjectEn, schoolId):
    #     params = {
    #         "subjectId": subjectId,
    #         "subjectEn": subjectEn,
    #         "schoolId": schoolId
    #     }
    #     return self.client.get(url=self.url_builder.homeworkprod_getQuestionBookBySubject, params=params)

    def homeworkprod_getWrongQuestionChapter(self, subjectId, subjectEn, bookId, schoolId):
        params = {
            "subjectId": subjectId,
            "subjectEn": subjectEn,
            "bookId": bookId,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getWrongQuestionChapter, params=params)

    def homeworkprod_getWrongQuestionPoints(self, subjectId, subjectEn, schoolId):
        params = {
            "subjectId": subjectId,
            "subjectEn": subjectEn,
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getWrongQuestionPoints, params=params)

    def homeworkprod_getWrongQuestionSearchOption(self, schoolId):
        params = {
            "schoolId": schoolId
        }
        return self.client.get(url=self.url_builder.homeworkprod_getWrongQuestionSearchOption, params=params)

    def homeworkprod_pageWrongQuestions(self, post_data):
        return self.client.post(url=self.url_builder.homeworkprod_pageWrongQuestions, data=post_data)

    def homeworkprod_generatePaperByQuestionList(self, post_data):
        return self.client.post(url=self.url_builder.homeworkprod_generatePaperByQuestionList, data=post_data)

    def getpsychologyhomework(self, schoolId, page=1, pagesize=10):
        params = {
            "schoolId": schoolId,
            "page": page,
            "pagesize": pagesize
        }
        return self.client.get(url=self.url_builder.getpsychologyhomework, params=params)
