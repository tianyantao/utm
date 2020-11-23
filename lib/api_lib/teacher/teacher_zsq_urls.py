from config.config_case import ConfigCase


class TeacherZsqUrls:

    def init_zsq_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_WEB)
        edu_baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TEACHER)

        '''新高一'''
        self.answer_getAnswerCountsState = baseurl + '/api/holidayprod/answer/getAnswerCountsState'
        self.student_getTextbookVersion = baseurl + '/api/holidayprod/student/getTextbookVersion'
        self.student_getNotice = baseurl + '/api/holidayprod/student/getNotice'
        self.student_getMemberDetailsPage = baseurl + '/api/holidayprod/student/getMemberDetailsPage'
        self.meal_getMealDetail = baseurl + '/api/holidayprod/meal/getMealDetail'
        self.meal_getWeaknessMealDetail = baseurl + '/api/holidayprod/meal/getWeaknessMealDetail'
        self.meal_getInterestMealDetail = baseurl + '/api/holidayprod/meal/getInterestMealDetail'
        self.reward_rewardPopup = baseurl + '/api/holidayprod/reward/rewardPopup'
        self.reward_seriesPartakeRewardPopup = baseurl + '/api/holidayprod/reward/seriesPartakeRewardPopup'
        self.reward_seriesChallengeRewardPopup = baseurl + '/api/holidayprod/reward/seriesChallengeRewardPopup'
        self.answer_getAnswerCountsState = baseurl + '/api/holidayprod/answer/getAnswerCountsState'
        self.answer_beginAnswer = baseurl + '/api/holidayprod/answer/beginAnswer'
        self.answer_getTodayAnswerRank = baseurl + '/api/holidayprod/answer/getTodayAnswerRank'
        self.answer_getHistoryAnswerRank = baseurl + '/api/holidayprod/answer/getHistoryAnswerRank'
        self.read_getPcTuoZhanTiSheng = baseurl + '/api/holidayprod/read/getPcTuoZhanTiSheng'
        self.read_getAppTuoZhanTiSheng = baseurl + '/api/holidayprod/read/getAppTuoZhanTiSheng'
        self.read_getMasterpiece = baseurl + '/api/holidayprod/read/getMasterpiece'
        self.read_getRecommend = baseurl + '/api/holidayprod/read/getRecommend'
        self.read_getBanner = baseurl + '/api/holidayprod/read/getBanner'
        self.read_getStudentPcBanner = baseurl + '/api/holidayprod/read/getStudentPcBanner'
        self.read_getStudentAppBanner = baseurl + '/api/holidayprod/read/getStudentAppBanner'
        self.newStudent_getHomeworkState = baseurl + '/api/holidayprod/newStudent/getHomeworkState'
        self.live_getSingleLive = baseurl + '/api/holidayprod/live/getSingleLive'
        self.newTeacher_getCategoryTree = baseurl + '/api/holidayprod/newTeacher/getCategoryTree'
        self.newTeacher_getStandardResource = baseurl + '/api/holidayprod/newTeacher/getStandardResource'
        self.newStudent_getSchoolVideoInfo = baseurl + '/api/holidayprod/newStudent/getSchoolVideoInfo'
        self.newStudent_getHomeworkProgress = baseurl + '/api/holidayprod/newStudent/getHomeworkProgress'
        self.newTeacher_getState = baseurl + '/api/holidayprod/newTeacher/getState'
        self.newTeacher_listLessonSchedule = baseurl + '/api/holidayprod/newTeacher/listLessonSchedule'
        self.newTeacher_listSubjectVersion = baseurl + '/api/holidayprod/newTeacher/listSubjectVersion'
        self.newTeacher_getTeacherCustom = baseurl + '/api/holidayprod/newTeacher/getTeacherCustom'
        self.newTeacher_getAssignedHomeworkMaterial = baseurl + '/api/holidayprod/newTeacher/getAssignedHomeworkMaterial'
        self.newStudent_getHomeworkInfo = baseurl + '/api/holidayprod/newStudent/getHomeworkInfo'
        self.newStudent_listJoinClass = baseurl + '/api/holidayprod/newStudent/listJoinClass'
        '''德育中心'''
        self.moralEdu_homepageStatistics = edu_baseurl + '/api/eteacherproduct/moralEdu/homepageStatistics'
        self.moralEdu_listGrades = edu_baseurl + '/api/eteacherproduct/moralEdu/listGrades'
        self.moralEdu_getClassMeetingStatistics = edu_baseurl + '/api/eteacherproduct/moralEdu/getClassMeetingStatistics'
        self.moralEdu_getClassMeetingList = edu_baseurl + '/api/eteacherproduct/moralEdu/getClassMeetingList'
        self.moralEdu_getClassMeetingDetail = edu_baseurl + '/api/eteacherproduct/moralEdu/getClassMeetingDetail'
        self.moralEdu_getGetEvaluationList = edu_baseurl + '/api/eteacherproduct/moralEdu/getGetEvaluationList'
        self.moralEdu_getGetEvaluationDetail = edu_baseurl + '/api/eteacherproduct/moralEdu/getGetEvaluationDetail'
        self.moralEdu_getTeacherClassRoomList = edu_baseurl + '/api/eteacherproduct/moralEdu/getTeacherClassRoomList'
        self.moralEdu_getMoralEduCourseList = edu_baseurl + '/api/eteacherproduct/moralEdu/getMoralEduCourseList'
        self.moralEdu_getStudentProblemManual = edu_baseurl + '/api/eteacherproduct/moralEdu/getStudentProblemManual'
        self.moralEdu_report_parentsCourseViews = edu_baseurl + '/api/eteacherproduct/moralEdu/report/parentsCourseViews'
        self.moralEdu_report_parentsCourseViewDetail = edu_baseurl + '/api/eteacherproduct/moralEdu/report/parentsCourseViewDetail'
        self.moralEdu_report_parentsCourseViewDetail_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/parentsCourseViewDetail/export'
        self.moralEdu_report_schoolCourseInfo = edu_baseurl + '/api/eteacherproduct/moralEdu/report/schoolCourseInfo'
        self.moralEdu_report_schoolCourseInfo_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/schoolCourseInfo/export'
        self.moralEdu_report_teacherView = edu_baseurl + '/api/eteacherproduct/moralEdu/report/teacherView'
        self.moralEdu_report_teacherView_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/teacherView/export'
        self.moralEdu_report_resourceRank = edu_baseurl + '/api/eteacherproduct/moralEdu/report/resourceRank'
        self.moralEdu_report_teacherView_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/teacherView/export'
        self.moralEdu_gradeClassList = edu_baseurl + '/api/eteacherproduct/moralEdu/gradeClassList'
        self.moralEdu_getCategory = edu_baseurl + '/api/eteacherproduct/moralEdu/getCategory'
        self.moralEdu_parentsEdu_list = edu_baseurl + '/api/eteacherproduct/moralEdu/parentsEdu/list'
        self.moralEdu_report_teacherView = edu_baseurl + '/api/eteacherproduct/moralEdu/report/teacherView'
        self.moralEdu_report_resourceRank_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/resourceRank/export'
        self.moralEdu_report_parentsCourseViews_export = edu_baseurl + '/api/eteacherproduct/moralEdu/report/parentsCourseViews/export'
        self.moralEdu_getMoralResource_list = edu_baseurl + '/api/eteacherproduct/moralEdu/getMoralResource/list'
        self.eteacherproduct_school_getSchoolUserInfo = edu_baseurl + '/api/eteacherproduct/school/getSchoolUserInfo'
