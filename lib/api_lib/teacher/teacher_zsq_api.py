from lib.api_lib.teacher.teacher_urls import TeacherUrls
import time

now = int(time.time())


def timestampms():
    # 返回延迟一天的时间戳（ms）
    timestamp = time.time()
    timestamp1 = int(timestamp) + 86400
    return int(round(timestamp1 * 1000))


class TeacherZsq:
    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()

    # 新高一
    def student_getTextbookVersion(self):
        return self.client.get(url=self.url_builder.student_getTextbookVersion)

    def student_getNotice(self):
        return self.client.get(url=self.url_builder.student_getNotice)

    def student_getMemberDetailsPage(self):
        return self.client.get(url=self.url_builder.student_getMemberDetailsPage)

    def meal_getMealDetail(self):
        return self.client.get(url=self.url_builder.meal_getMealDetail)

    def meal_getWeaknessMealDetail(self):
        return self.client.get(url=self.url_builder.meal_getWeaknessMealDetail)

    def meal_getInterestMealDetail(self, type):
        data = {"type": type}
        return self.client.get(url=self.url_builder.meal_getInterestMealDetail, params=data)

    def reward_rewardPopup(self):
        return self.client.get(url=self.url_builder.reward_rewardPopup)

    def reward_seriesPartakeRewardPopup(self):
        return self.client.get(url=self.url_builder.reward_seriesPartakeRewardPopup)

    def reward_seriesChallengeRewardPopup(self):
        return self.client.get(url=self.url_builder.reward_seriesChallengeRewardPopup)

    def answer_getAnswerCountsState(self):
        return self.client.get(url=self.url_builder.answer_getAnswerCountsState)

    def answer_beginAnswer(self):
        return self.client.get(url=self.url_builder.answer_beginAnswer)

    def answer_getTodayAnswerRank(self):
        return self.client.get(url=self.url_builder.answer_getTodayAnswerRank)

    def answer_getHistoryAnswerRank(self):
        return self.client.get(url=self.url_builder.answer_getHistoryAnswerRank)

    def read_getPcTuoZhanTiSheng(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getPcTuoZhanTiSheng, headers=header)

    def read_getAppTuoZhanTiSheng(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getAppTuoZhanTiSheng, headers=header)

    def read_getMasterpiece(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getMasterpiece, headers=header)

    def read_getRecommend(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getRecommend, headers=header)

    def read_getBanner(self):
        header = {"Content-Type": "application/json"}
        return self.client.post(url=self.url_builder.read_getBanner, headers=header)

    def read_getStudentPcBanner(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getStudentPcBanner, headers=header)

    def read_getStudentAppBanner(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        return self.client.post(url=self.url_builder.read_getStudentAppBanner, headers=header)

    def newStudent_getHomeworkState(self):
        header = {"Content-Type": "application/json	"}
        return self.client.get(url=self.url_builder.newStudent_getHomeworkState, headers=header)

    def live_getSingleLive(self):
        headers = {}
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['token'] = self.client.user_token
        return self.client.post(url=self.url_builder.live_getSingleLive, headers=headers)

    def newTeacher_getCategoryTree(self):
        return self.client.get(url=self.url_builder.newTeacher_getCategoryTree)

    def newTeacher_getStandardResource(self, versionId):
        headers = {"Content-Type": "application/json"}
        params = {"versionId": versionId}
        return self.client.get(url=self.url_builder.newTeacher_getStandardResource, headers=headers, params=params)

    def newStudent_getSchoolVideoInfo(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newStudent_getSchoolVideoInfo, headers=headers)

    def newStudent_getHomeworkProgress(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newStudent_getHomeworkProgress, headers=headers)

    def newTeacher_getState(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newTeacher_getState, headers=headers)

    def newTeacher_listLessonSchedule(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newTeacher_listLessonSchedule, headers=headers)

    def newTeacher_listSubjectVersion(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newTeacher_listSubjectVersion, headers=headers)

    def newTeacher_getTeacherCustom(self, textbookId, typeId):
        headers = {"Content-Type": "application/json"}
        params = {"textbookId": textbookId, "typeId": typeId}
        return self.client.get(url=self.url_builder.newTeacher_getTeacherCustom, headers=headers, params=params)

    def newTeacher_getAssignedHomeworkMaterial(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newTeacher_getAssignedHomeworkMaterial, headers=headers)

    def newStudent_getHomeworkInfo(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.newStudent_getHomeworkInfo, headers=headers)

    def newStudent_listJoinClass(self):
        return self.client.get(url=self.url_builder.newStudent_listJoinClass)

    # 德育中心
    def eteacherproduct_school_getSchoolUserInfo(self):
        headers = {"Content-Type": "application/json"}
        return self.client.get(url=self.url_builder.eteacherproduct_school_getSchoolUserInfo, headers=headers)

    def moralEdu_homepageStatistics(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_homepageStatistics, headers=headers, params=params)

    def moralEdu_listGrades(self, schoolId, filter, earlyRise, showDefault):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId, "filter": filter, "earlyRise": earlyRise, "showDefault": showDefault}
        return self.client.get(url=self.url_builder.moralEdu_listGrades, headers=headers, params=params)

    def moralEdu_getClassMeetingStatistics(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_getClassMeetingStatistics, headers=headers, params=params)

    def moralEdu_getClassMeetingList(self, grade, categoryFirst, categorySecond, type, pageIndex, pageSize, schoolId):
        headers = {"Content-Type": "application/json"}
        post_data = {"grade": grade, "categoryFirst": categoryFirst, "categorySecond": categorySecond, "type": type,
                     "pageIndex": pageIndex, "pageSize": pageSize, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.moralEdu_getClassMeetingList, headers=headers, data=post_data)

    def moralEdu_getClassMeetingDetail(self, classMeetingId):
        headers = {"Content-Type": "application/json"}
        params = {"classMeetingId": classMeetingId}
        return self.client.get(url=self.url_builder.moralEdu_getClassMeetingDetail, headers=headers, params=params)

    def moralEdu_getGetEvaluationList(self, schoolId):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId}
        return self.client.post(url=self.url_builder.moralEdu_getGetEvaluationList, headers=headers, data=post_data)

    def moralEdu_getGetEvaluationDetail(self, schoolId, evaluationId):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "evaluationId": evaluationId}
        return self.client.post(url=self.url_builder.moralEdu_getGetEvaluationDetail, headers=headers, data=post_data)

    def moralEdu_getTeacherClassRoomList(self, type, categoryFirst, categorySecond, pageIndex, pageSize, schoolId):
        headers = {"Content-Type": "application/json"}
        post_data = {"type": type, "categoryFirst": categoryFirst, "categorySecond": categorySecond,
                     "pageIndex": pageIndex, "pageSize": pageSize, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.moralEdu_getTeacherClassRoomList, headers=headers, data=post_data)

    def moralEdu_getMoralEduCourseList(self, currentSemesterId, grade, categoryId, isHomePage, schoolId):
        headers = {"Content-Type": "application/json"}
        post_data = {"currentSemesterId": currentSemesterId, "grade": grade, "categoryId": categoryId,
                     "isHomePage": isHomePage, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.moralEdu_getMoralEduCourseList, headers=headers, data=post_data)

    def moralEdu_getStudentProblemManual(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_getStudentProblemManual, headers=headers, params=params)

    def moralEdu_report_parentsCourseViews(self, schoolId, grade, classId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "grade": grade, "classId": classId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_parentsCourseViews, headers=headers,
                                data=post_data)

    def moralEdu_report_parentsCourseViewDetail(self, schoolId, grade, classId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "grade": grade, "classId": classId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_parentsCourseViewDetail, headers=headers,
                                data=post_data)

    def moralEdu_report_parentsCourseViewDetail_export(self, schoolId, grade, classId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "grade": grade, "classId": classId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_parentsCourseViewDetail_export, headers=headers,
                                data=post_data)

    def moralEdu_report_schoolCourseInfo(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_report_schoolCourseInfo, headers=headers, params=params)

    def moralEdu_report_schoolCourseInfo_export(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_report_schoolCourseInfo_export, headers=headers,
                               params=params)

    def moralEdu_report_resourceRank(self, schoolId, period, resourceType):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "period": period, "resourceType": resourceType}
        return self.client.post(url=self.url_builder.moralEdu_report_resourceRank, headers=headers, data=post_data)

    def moralEdu_report_teacherView_export(self, schoolId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_teacherView_export, headers=headers,
                                data=post_data)

    def moralEdu_gradeClassList(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_gradeClassList, headers=headers, params=params)

    def moralEdu_getCategory(self, categoryType, showFirstDefault, showSecondDefault, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"categoryType": categoryType, "showFirstDefault": showFirstDefault,
                  "showSecondDefault": showSecondDefault, "schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_getCategory, headers=headers, params=params)

    def moralEdu_parentsEdu_list(self, schoolId, pageIndex, pageSize):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "pageIndex": pageIndex, "pageSize": pageSize}
        return self.client.post(url=self.url_builder.moralEdu_parentsEdu_list, headers=headers, data=post_data)

    def moralEdu_report_teacherView(self, schoolId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_teacherView, headers=headers, data=post_data)

    def moralEdu_report_resourceRank_export(self, schoolId, period, resourceType):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "period": period, "resourceType": resourceType}
        return self.client.post(url=self.url_builder.moralEdu_report_resourceRank_export, headers=headers,
                                data=post_data)

    def moralEdu_report_parentsCourseViews_export(self, schoolId, grade, classId, period):
        headers = {"Content-Type": "application/json"}
        post_data = {"schoolId": schoolId, "grade": grade, "classId": classId, "period": period}
        return self.client.post(url=self.url_builder.moralEdu_report_parentsCourseViews_export, headers=headers,
                                data=post_data)

    def moralEdu_getMoralResource_list(self, schoolId):
        headers = {"Content-Type": "application/json"}
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.moralEdu_getMoralResource_list, headers=headers, params=params)
