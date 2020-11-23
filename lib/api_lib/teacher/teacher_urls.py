from lib.api_lib.teacher.teacher_wly_urls import TeacherWlyUrls
from lib.api_lib.teacher.teacher_zzj_urls import TeacherZzjUrls
from lib.api_lib.teacher.teacher_zsq_urls import TeacherZsqUrls
from config.config_case import ConfigCase


class TeacherUrls(TeacherZsqUrls, TeacherWlyUrls, TeacherZzjUrls):

    def __init__(self):
        self.__init_urls()
        self.init_wly_urls()
        self.init_zzj_urls()
        self.init_zsq_urls()

    def __init_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TEACHER)
        gateway_url = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_GATEWAY)
        inside_url = "http://{}".format(configcase.HOST_INSIDEGATEWAY)
        self.homework_GetHomeworkDetailInfo = baseurl + '/api/services/HomeworkService/homework/GetHomeworkDetailInfo'
        self.userinfo = baseurl + '/api/teacher/psychology/userinfo'
        self.userinfoforpsychology = baseurl + '/api/teacher/psychology/userinfoforpsychology'
        self.userinfo_student = baseurl + '/api/student/students/userinfo'
        self.modifyteachername = baseurl + '/api/teacher/overview/modifyteachername'
        self.permissionmenu = baseurl + '/api/menu/permissionmenu'
        self.menu = baseurl + '/api/teacher/menu'
        self.naviandmenus = baseurl + '/api/menu/naviandmenus'
        self.getkemu = baseurl + '/api/teacher/homework/getkemu'
        self.getknowledgelist = baseurl + '/api/teacher/homework/getknowledgelist'
        self.getteachers = baseurl + '/api/teacher/homework/getteachers'
        self.gettikuquestionfilter = baseurl + '/api/teacher/homework/xueke/gettikuquestionfilter'
        self.getclasseswithgradeinfo = baseurl + '/api/teacher/homework/xueke/getclasseswithgradeinfo'
        self.getcourses = baseurl + '/api/teacher/homework/xueke/getcourses'
        self.addtobasket = baseurl + '/api/teacher/homework/xueke/addtobasket'
        self.clearbasket = baseurl + '/api/teacher/homework/xueke/clearbasket'
        self.getbasketitems = baseurl + '/api/teacher/homework/xueke/getbasketitems'
        self.setxuekehomeworkjson = baseurl + '/api/teacher/homework/xueke/setxuekehomeworkjson'
        self.qSearch_Subjects = baseurl + '/api/BQSearch/QSearch/Subjects'
        self.qSearch_Regions = baseurl + '/api/BQSearch/QSearch/Regions'
        self.qSearch_GetJYDegree = baseurl + '/api/BQSearch/QSearch/GetJYDegree'
        self.qSearch_GetJYTilei = baseurl + '/api/BQSearch/QSearch/GetJYTilei'
        self.qSearch_GetJYSources = baseurl + '/api/BQSearch/QSearch/GetJYSources'
        self.qSearch_GetJYCates = baseurl + '/api/BQSearch/QSearch/GetJYCates'
        self.qSearch_Points = baseurl + '/api/BQSearch/QSearch/Points'
        self.qSearch_QuestionsByPoint = baseurl + '/api/BQSearch/QSearch/QuestionsByPoint'
        # 章节选题
        self.qSearch_TextbookEditions = baseurl + '/api/BQSearch/QSearch/TextbookEditions'
        self.qSearch_Years = baseurl + '/api/BQSearch/QSearch/Years'
        self.qSearch_Textbooks = baseurl + '/api/BQSearch/QSearch/Textbooks'
        self.qSearch_QuestionsByChapter = baseurl + '/api/BQSearch/QSearch/QuestionsByChapter'
        self.qSearch_ConciseTextbooks = baseurl + '/api/BQSearch/QSearch/ConciseTextbooks'
        self.qSearch_Categorys = baseurl + '/api/BQSearch/QSearch/Categorys'
        self.getquestions = baseurl + '/api/teacher/homework/xueke/getquestions'
        self.myhomework_app = baseurl + '/app/v1/homework/myhomework'
        self.homeworkinfo_app = baseurl + '/app/v1/homework/info'
        self.homeworklist = baseurl + '/api/student/homework/homeworklist'
        self.homeworkrecord = baseurl + '/api/teacher/homework/homeworkrecord'
        self.deletehomework = baseurl + '/api/teacher/homework/deletehomework'
        self.sbr_getavailablegrades = baseurl + '/api/teacher/homework/sbr/getavailablegrades'
        self.sbr_getvideos = baseurl + '/api/teacher/homework/sbr/getvideos'
        self.sbr_addtosbrbasket = baseurl + '/api/teacher/homework/sbr/addtosbrbasket'
        self.sbr_gesbrbasketitems = baseurl + '/api/teacher/homework/sbr/gesbrbasketitems'
        self.sbr_sethomework = baseurl + '/api/teacher/homework/sbr/set/homework'
        self.selectclasstypeoptions = baseurl + '/api/teacher/SelectOptions'
        self.GetSbrPaperFilter = baseurl + '/api/teacher/homework/sbrpaper/GetSbrPaperFilter'
        self.getSbrPaperPagingList = baseurl + '/api/teacher/homework/sbrpaper/getSbrPaperPagingList'
        self.SetSbrPaperHomework = baseurl + '/api/teacher/homework/sbrpaper/SetSbrPaperHomework'
        self.getsbrpaperquestioncard = baseurl + '/api/mobi/homework/getsbrpaperquestioncard'
        self.SubmitSbrPaperAnswer = baseurl + '/api/mobi/homework/SubmitSbrPaperAnswer'
        self.GetSbrPaperExam = baseurl + '/student/MyHomework/GetSbrPaperExam'
        self.SubmitSbrPaperExam_pc = baseurl + '/student/MyHomework/SubmitSbrPaperExam'
        self.homeworkvideolist = baseurl + '/api/student/homework/homeworkvideolist'
        self.gethomeworksetlist = baseurl + '/api/mobi/homework/gethomeworksetlist'
        self.GetQuestionListByHomeworkId = baseurl + '/api/student/homework/GetQuestionListByHomeworkId'
        self.submithomeworkpaper_student = baseurl + '/api/student/homework/submithomeworkpaper'
        self.GetQuestionIdsByHomeworkId = baseurl + '/api/mobi/Homework/GetQuestionIdsByHomeworkId'
        self.GetQuestionInfoByQid = baseurl + '/api/h5/homework/GetQuestionInfoByQid'
        self.submithomeworkpaper_mobi = baseurl + '/api/mobi/Homework/submithomeworkpaper'
        self.UploadSubjectiveAnswerPic = baseurl + '/api/mobi/Homework/UploadSubjectiveAnswerPic'
        self.homeworkinfo_teacher = baseurl + '/api/teacher/homework/homeworkinfo'
        self.HomeworkRecordClasses = baseurl + '/api/teacher/homework/HomeworkRecordClasses'
        self.homeworkcompletion_exercises = baseurl + '/api/teacher/homework/exercises/homeworkcompletion'
        self.UnCompleted = baseurl + '/api/teacher/homework/UnCompleted'
        self.ClassHomeworkCompletion = baseurl + '/api/teacher/homework/exercises/ClassHomeworkCompletion'
        self.gethomeworkpaperreport_teacher = baseurl + '/api/teacher/homeworkpaper/gethomeworkpaperreport'
        self.gethomeworkpaperreport_student = baseurl + '/api/student/homework/gethomeworkpaperreport'
        self.courserecommendations4fraud = baseurl + '/api/shared/SharedHomework/CourseRecommendations4Fraud'
        self.analysis_xueke_pc = baseurl + '/api/student/homework/xueke/analysis'
        self.searchschoolclasses = baseurl + '/api/student/classes/searchschoolclasses'
        self.submitjoinclassdata = baseurl + '/api/student/classes/submitjoinclassdata'
        self.winter2019_getuserrole = baseurl + '/api/services/Winter2019/Winter2019/GetUserRole'
        self.winter2019_getprerecordinfos = baseurl + '/api/services/Winter2019/Winter2019/GetPreRecordInfos'
        self.winter2019_setstandardhomework = baseurl + '/api/services/Winter2019/Winter2019/SetStandardHomework'
        self.winter2019_setgradepersonalizedhomework = baseurl + '/api/services/Winter2019/Winter2019/SetGradePersonalizedHomework'
        self.winter2019_getpersonalquestionsinfos = baseurl + '/api/services/Winter2019/Winter2019/GetPersonalQuestionsInfos'
        self.winter2019_studentanswer = baseurl + '/api/services/Winter2019/Winter2019/StudentAnswer'
        self.winter2019_getquestionrecommends = baseurl + '/api/services/Winter2019/winter2019/GetQuestionRecommends'
        self.winter2019_pointanswerrate = baseurl + '/api/services/Winter2019/Winter2019/PointAnswerRate'
        # self.psychology_sethomework = baseurl + '/api/teacher/psychology/sethomework'
        self.evaluation_sethomework = baseurl + '/api/services/HomeworkService/evaluation/SetHomework'
        # self.psychology_homeworklist = baseurl + '/api/teacher/psychology/homeworklist'
        self.evaluation_GetHomeworkLogList = baseurl + '/api/services/HomeworkService/evaluation/GetHomeworkLogList'
        # self.psychology_deletehomework = baseurl + '/api/teacher/psychology/deletehomework'
        self.evaluation_deletehomework = baseurl + '/api/services/HomeworkService/evaluation/DeleteHomework'
        self.psychology_html = baseurl + '/student/home/psychologywork'
        # self.psychology_evaluationlist = baseurl + '/api/teacher/psychology/evaluationlist'
        self.evaluation_GetEvaluationList = baseurl + '/api/services/HomeworkService/evaluation/GetEvaluationList'
        # self.psychology_evaluationdetail = baseurl + '/api/teacher/psychology/evaluationdetail'
        self.evaluation_GetEvaluationDetail = baseurl + '/api/services/HomeworkService/evaluation/GetEvaluationDetail'
        # self.psychology_gradeclassstateinfo = baseurl + '/api/teacher/psychology/gradeclassstateinfo'
        self.evaluation_GradeClassStateInfo = baseurl + '/api/services/HomeworkService/evaluation/GradeClassStateInfo'
        self.evaluation_GetClassCompletion = baseurl + '/api/services/HomeworkService/evaluation/GetClassCompletion'
        self.homeworkservice_getuserrole = baseurl + '/api/services/HomeworkService/AnalogSelection/GetUserRole'
        self.homeworkservice_homeworkrecordclasses = baseurl + '/api/services/HomeworkService/AnalogSelection/HomeworkRecordClasses'
        self.homeworkservice_getpapaerinfo = baseurl + '/api/services/HomeworkService/homework/GestPaperInfo'
        self.homeworkservice_getexercisehomeworclasscompletion = baseurl + '/api/services/HomeworkService/homework/GetExerciseHomeworClassCompletion'
        self.homeworkservice_xueKeClassHomeworkStudentCompletion = baseurl + '/api/services/HomeworkService/homework/XueKeClassHomeworkStudentCompletion'
        self.homeworkservice_teacherKnowledgeErrorRate = baseurl + '/api/services/HomeworkService/homework/TeacherKnowledgeErrorRate'
        self.homeworkservice_GetPersonalQuestionsInfos = baseurl + '/api/services/HomeworkService/homework/GetPersonalQuestionsInfos'
        self.homeworkservice_GetPaperErrorStudentsWithErrorRate = baseurl + '/api/services/HomeworkService/homework/GetPaperErrorStudentsWithErrorRate'
        self.homeworkservice_GetPaperQuestionErrorStudents = baseurl + '/api/services/HomeworkService/homework/GetPaperQuestionErrorStudents'
        self.homeworkservice_uncompleted = baseurl + '/api/services/HomeworkService/homework/UnCompleted'
        self.modifystudentinfo = baseurl + '/api/services/EduOrgan/Student/ModifyStudentInfo'
        self.getstudentname = baseurl + '/api/services/EduOrgan/Student/GetStudentName'
        self.career_postheadertypelist = baseurl + '/api/teacher/assignhomeworkfortea/postheadertypelist'
        self.career_gethomworklist = baseurl + '/api/teacher/assignhomeworkfortea/gethomworklist'
        self.career_addbasket = baseurl + '/api/teacher/assignhomeworkfortea/addbasket'
        self.career_removebaseket  = baseurl + '/api/teacher/assignhomeworkfortea/removebaseket'
        self.career_clearbasket = baseurl + '/api/teacher/assignhomeworkfortea/clearbaseket'
        self.career_getbaseketvideolist = baseurl + '/api/teacher/assignhomeworkfortea/getbaseketvideolist'
        self.career_submithomework = baseurl + '/api/teacher/assignhomeworkfortea/submithomework'
        self.career_getgradeandclassinfo = baseurl + '/api/teacher/assignhomeworkfortea/getgradeandclassinfo'
        #B端地图
        self.hp_grades = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/grades'
        self.hp_GetTimeAxis = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/GetTimeAxis'
        self.hp_ThemeMapData = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/ThemeMapData'
        self.hp_themerecord = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/themerecord'
        self.hp_themehomeworkdetail = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/themehomeworkdetail'
        self.hp_setxuekehomework = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/setxuekehomework'
        self.hp_setshengyahomework = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/setshengyahomework'
        self.hp_setfmhomework = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/setfmhomework'
        self.hp_getclasseswithgradeinfo = baseurl + '/api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo'

        # 卷库v2.0：
        self.paper_papertype = baseurl + '/api/services/HomeworkService/paperHomework/PaperType'
        self.paper_kemu = baseurl + '/api/services/HomeworkService/paperHomework/Kemu'
        self.paper_GetUserSubjects = baseurl + '/api/services/EduOrgan/schoolStaff/GetUserSubjects'
        self.paper_GetPaperDetailInfo = baseurl + '/api/services/HomeworkService/paperHomework/GetPaperDetailInfo'
        self.paper_Sorts = baseurl + '/api/services/HomeworkService/paperHomework/Sorts'
        self.paper_TextBook = baseurl + '/api/services/HomeworkService/paperHomework/TextBook'
        self.paper_Degree = baseurl + '/api/services/HomeworkService/paperHomework/Degree'
        self.paper_year = baseurl + '/api/services/HomeworkService/paperHomework/Year'
        self.paper_area = baseurl + '/api/services/HomeworkService/paperHomework/Area'
        self.paper_Semester = baseurl + '/api/services/HomeworkService/paperHomework/Semester'
        self.paper_SetPaperHomeWork = baseurl + '/api/services/HomeworkService/paperHomework/SetPaperHomeWork'
        self.paper_GetPaperHomeworkDetailInfo = baseurl + '/api/services/HomeworkService/paperHomework/GetPaperHomeworkDetailInfo'
        self.paper_papers = baseurl + '/api/services/HomeworkService/paperHomework/Papers'

        # 未截止作业列表(分页) app首页服务端调用
        self.homeworkservice_StudentUnClosedHomeworks = baseurl + '/api/services/HomeworkService/studentHomework/StudentUnClosedHomeworks'

        # B&C题型完善：
        self.receive_paper_report = baseurl + '/api/services/HomeworkService/Homework/ReceivePaperReport'

        # oa教师端管理：
        # self.oaview_oauth = "http://{}".format(host) + '/oaview/oauth'
        self.oaview_oauth = baseurl + '/oaview/oauth'
        self.oaview_schoollist = baseurl + '/oaview/oamanage/schoollist'
        self.oaview_disband = baseurl + '/oaview/oamanage/disband'
        self.oaview_classlist = baseurl + '/oaview/oamanage/classlist'
        self.oaview_AddSchoolLeader = baseurl + '/oaview/oamanage/AddSchoolLeader'
        self.oaview_AddGradeLeader = baseurl + '/oaview/oamanage/AddGradeLeader'
        self.oaview_ModifyClass = baseurl + '/oaview/oamanage/ModifyClass'
        self.oaview_LoadLeaderList = baseurl + '/oaview/oamanage/LoadLeaderList'


        # 新版作业篮：
        self.basket_remove = baseurl + '/api/eteacherproduct/basket/remove'
        self.basket_add = baseurl + '/api/eteacherproduct/basket/add'
        self.basket_listallexercise = baseurl + '/api/eteacherproduct/basket/listallexercise'
        self.basket_listall = baseurl + '/api/eteacherproduct/basket/listall'

        # java布置作业接口
        self.sethomework = baseurl + '/api/eteacherproduct/homework/setHomework'



        # 2020新高一：
        self.holidayprod_getAssignState = gateway_url + '/api/holidayprod/teacher/getAssignState'
        self.holidayprod_getCategoryTree = gateway_url + '/api/holidayprod/teacher/getCategoryTree'
        self.holidayprod_getStandardResource = gateway_url + '/api/holidayprod/teacher/getStandardResource'
        self.holidayprod_getAssignDetail = gateway_url + '/api/holidayprod/teacher/getAssignDetail'
        self.holidayprod_assign = gateway_url + '/api/holidayprod/teacher/assign'




        # 反向代理的外部接口（ng配置修改后回归）：
        self.study_Subjects = baseurl + '/api/study/Exercises/Subjects'
        self.study_Regions = baseurl + '/api/study/Exercises/Regions'
        self.study_GetJYDegree = baseurl + '/api/study/Exercises/GetJYDegree'
        self.study_GetJYTilei = baseurl + '/api/study/Exercises/GetJYTilei'
        self.study_GetJYSources = baseurl + '/api/study/Exercises/GetJYSources'
        self.study_GetJYCates = baseurl + '/api/study/Exercises/GetJYCates'
        self.study_Points = baseurl + '/api/study/Exercises/Points'
        self.study_TextbookEditions = baseurl + '/api/study/Exercises/TextbookEditions'
        self.study_Years = baseurl + '/api/study/Exercises/Years'
        self.study_Textbooks = baseurl + '/api/study/Exercises/Textbooks'
        self.study_QuestionsByChapter = baseurl + '/api/study/Exercises/QuestionsByChapter'
        self.study_ConciseTextbooks = baseurl + '/api/study/Exercises/ConciseTextbooks'
        self.study_Categorys = baseurl + '/api/study/Exercises/Categorys'

        self.study_paperlist = baseurl + '/api/study/paperlibrary/paperlist'
        self.study_PaperType = baseurl + '/api/study/paperlibrary/PaperType'
        self.study_SearchCondition = baseurl + '/api/study/paperlibrary/SearchCondition'
        self.study_Textbook = baseurl + '/api/study/paperlibrary/Textbook'
        self.study_papertype = baseurl + '/api/study/paperlibrary/PaperType'

        self.study_GetCategoryAndEdition = baseurl + '/api/study/subject/GetCategoryAndEdition'
        self.study_GetBookAndChapter = baseurl + '/api/study/subject/GetBookAndChapter'
        self.study_sorttype = baseurl + '/api/study/subject/sorttype'
        self.study_GetLevels = baseurl + '/PCCourseListService/GetLevels'
        self.study_GetTeachers = baseurl + '/PCCourseListService/GetTeachers'
        self.study_courselist = baseurl + '/api/study/course/courselist'

        self.study_getpaperinfo = baseurl + '/externalapi/wholepaperservice/getpaperinfo'
        self.study_getquestionmethodInfo = baseurl + '/externalapi/wholepaperservice/getquestionmethodInfo'

        self.getTeacherUserRole = baseurl + '/api/services/EduOrgan/schoolStaff/GetTeacherUserRole'
        self.GetUserManagerRole = baseurl + '/api/services/EduOrgan/schoolStaff/GetUserManagerRole'
        self.GetUserManagerAndClassRole = baseurl + '/api/services/EduOrgan/schoolStaff/GetUserManagerAndClassRole'

        # strategymarket的接口：
        self.rank_all = gateway_url + '/api/strategymarket/activity/solution/rank/all'
        self.rank_person = gateway_url + '/api/strategymarket/activity/solution/rank/person'
        self.activity_user_list = gateway_url + '/api/strategymarket/teacher/activity/homework/user/list'

        # 校本试卷升级
        self.getSbrHomeworkInfo4Answer = baseurl + '/api/services/HomeworkService/homework/getSbrHomeworkInfo4Answer'
        self.submitQuestionAnswers = baseurl + '/api/services/HomeworkService/homework/submitQuestionAnswers'
        self.SubmitQuestionAnswerRating = baseurl + '/api/services/HomeworkService/homework/SubmitQuestionAnswerRating'
        self.GetSbrHomeworkInfo4SelfRating = baseurl + '/api/services/HomeworkService/homework/GetSbrHomeworkInfo4SelfRating'
        self.GetStudentSbrHomeworkReport = baseurl + '/api/services/HomeworkService/homework/GetStudentSbrHomeworkReport'

        self.SubmitSubjectiveFileUrls = baseurl + '/api/services/HomeworkService/homework/SubmitSubjectiveFileUrls'
        self.GetExamPaperStaticByPaperId = baseurl + '/api/services/HomeworkService/homework/GetExamPaperStaticByPaperId'




        # 用户权限重构
        self.queryMenuInfo = baseurl + '/api/eteacherproduct/teacher/manage/queryMenuInfo'
        self.queryTeacherRoleAndSchoolInfo = baseurl + '/api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo'
        self.getSchoolUserInfo = baseurl + '/api/eteacherproduct/school/getSchoolUserInfo'
        self.queryCurrentSchoolConf = baseurl + '/api/eteacherproduct/school/queryCurrentSchoolConf'
        self.listGrades = baseurl + '/api/eteacherproduct/teacher/manage/listGrades'
        self.pageClasses = baseurl + '/api/eteacherproduct/classesManager/pageClasses'
        self.listRole = baseurl + '/api/eteacherproduct/teacher/manage/listRole'
        self.listRole = baseurl + '/api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo'
        self.listRole = baseurl + '/api/eteacherproduct/teacher/manage/listTeachSubject'

        self.oa_auth = inside_url + '/api/eteacherproduct/oa/auth'
        self.querySchoolInfo = baseurl + '/api/eteacherproduct/oa/schoolManage/querySchoolInfo'

        # 题卷库升级

        self.homeworkprod_getQuestionProvince = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionProvince'
        self.homeworkprod_pageQueryQuesAtChapterOrPoint = baseurl + '/bendbff/api/homeworkprod/resource/question/pageQueryQuesAtChapterOrPoint'
        self.homeworkprod_getQuestionSubject = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionSubject'
        self.homeworkprod_getQuestionPointBySubject = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionPointBySubject'
        self.homeworkprod_getQuestionBookBySubject = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionBookBySubject'
        self.homeworkprod_getQuestionChapterByBook = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionChapterByBook'
        self.homeworkprod_getQuestionFilterList = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionFilterList'
        self.homeworkprod_querySameQues = baseurl + '/bendbff/api/homeworkprod/resource/question/querySameQues'
        self.homeworkprod_queryQuestionDetail = baseurl + '/bendbff/api/homeworkprod/resource/question/queryQuestionDetail'

        self.homeworkprod_pageWrongQuestions = baseurl + '/bendbff/api/homeworkprod/resource/wrongQuestion/pageWrongQuestions'
        self.homeworkprod_getWrongQuestionChapter = baseurl + '/bendbff/api/homeworkprod/resource/wrongQuestion/getWrongQuestionChapter'
        self.homeworkprod_getWrongQuestionPoints = baseurl + '/bendbff/api/homeworkprod/resource/wrongQuestion/getWrongQuestionPoints'
        self.homeworkprod_getWrongQuestionSearchOption = baseurl + '/bendbff/api/homeworkprod/resource/wrongQuestion/getWrongQuestionSearchOption'

        self.homeworkprod_getPaperTreeByChapterId = baseurl + '/bendbff/api/homeworkprod/resource/paper/getPaperTreeByChapterId'
        self.homeworkprod_getChapterFilterPaperType = baseurl + '/bendbff/api/homeworkprod/resource/paper/getChapterFilterPaperType'
        self.homeworkprod_getPaperTreeCategory = baseurl + '/bendbff/api/homeworkprod/resource/paper/getPaperTreeCategory'
        self.homeworkprod_pagePaper = baseurl + '/bendbff/api/homeworkprod/resource/paper/pagePaper'
        self.homeworkprod_getPaperInfo = baseurl + '/bendbff/api/homeworkprod/resource/paper/getPaperInfo'
        self.homeworkprod_getPaperGroupInfo = baseurl + '/bendbff/api/homeworkprod/resource/paper/getPaperGroupInfo'
        self.homeworkprod_generatePaperByQuestionList = baseurl + '/bendbff/api/homeworkprod/resource/paper/generatePaperByQuestionList'

        self.homeworkprod_getErrorReason = baseurl + '/bendbff/api/homeworkprod/resource/error/question/feedback/getErrorReason'
        self.homeworkprod_errorQuestionFeedback = baseurl + '/bendbff/api/homeworkprod/resource/error/question/feedback/errorQuestionFeedback'

        self.homeworkprod_removeBasketResourceById = baseurl + '/bendbff/api/homeworkprod/basket/removeBasketResourceById'
        self.homeworkprod_removeBasketResourceByContent = baseurl + '/bendbff/api/homeworkprod/basket/removeBasketResourceByContent'
        self.homeworkprod_addBasketItems = baseurl + '/bendbff/api/homeworkprod/basket/addBasketItems'
        self.homeworkprod_resort = baseurl + '/bendbff/api/homeworkprod/basket/resort'
        self.homeworkprod_listQuestionBasketItems = baseurl + '/bendbff/api/homeworkprod/basket/listQuestionBasketItems'

        # 学生端心理测评作业列表
        self.getpsychologyhomework = baseurl + '/api/student/homework/getpsychologyhomework'