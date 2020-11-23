from config.config_case import ConfigCase
from lib.api_lib.teacher.teacher_zzj_urls import TeacherZzjUrls


class TeacherWlyUrls(TeacherZzjUrls):

    def init_wly_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TEACHER)
        wxbaseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_WX)
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
        self.FetchBasicData = baseurl + '/api/teacher/StatisticsReport/FetchBasicData'
        self.FetchGeneralAndRank = baseurl + '/api/teacher/StatisticsReport/FetchGeneralAndRank'
        self.fetchtopstudent = baseurl + '/api/teacher/StatisticsReport/fetchtopstudent'
        self.fetchchartdata = baseurl + '/api/teacher/StatisticsReport/fetchchartdata'
        self.fetchvideolesson = baseurl + '/api/teacher/StatisticsReport/fetchvideolesson'

        # 班级管理
        self.getclasslist = baseurl + '/api/teacher/classes/classmanage/classlist'
        self.classstudents = baseurl + '/api/teacher/classes/classdetail/studentlist'
        self.createadministrationclass = baseurl + '/api/teacher/classes/classmanage/createadministrationclass'
        self.SubmitJoinClassInfo = baseurl + '/api/teacher/classes/joinclass/SubmitJoinClassInfo'
        self.TeacherRoleGroupList = baseurl + '/api/teacher/classes/joinclass/TeacherRoleGroupList'
        self.createteachingclass = baseurl + '/api/teacher/classes/classmanage/createteachingclass'
        self.disbandclass = baseurl + '/api/teacher/classes/classdetail/disbandclass'
        self.addedstudentlist = baseurl + '/api/teacher/classes/createclass/addedstudentlist'
        self.submitaddedstudentlist = baseurl + '/api/teacher/classes/createclass/submitaddedstudentlist'
        self.removestudent = baseurl + '/api/teacher/classes/classdetail/removestudent'
        self.classmanagegrades = baseurl + '/api/teacher/classes/classmanage/grades'
        self.classinfo = baseurl + '/api/teacher/classes/classdetail/classinfo'
        self.grades = baseurl + '/api/teacher/classes/createclass/grades'
        self.studentmyclasslist = baseurl + '/api/student/classes/myclasslist'
        self.studentmyclasslist_app = baseurl + '/app/v1/class/myclass'
        self.schoolandclassinfo = baseurl + '/api/student/classes/schoolandclassinfo'
        self.schoolandclassinfo_app = baseurl + '/api/mobi/classes/schoolandclassinfo'
        self.searchschools = baseurl + '/api/student/classes/searchschools'
        self.searchschools_app = baseurl + '/api/mobi/classes/searchschools'
        self.searchclasses = baseurl + '/api/student/classes/searchclasses'
        self.searchclasses_app = baseurl + '/api/mobi/classes/searchgradeclasses'

        # 学情报告
        self.breportgetuserrole = baseurl + '/api/services/bstudyreport/common/getuserrole'
        self.statisticsstudentnum = baseurl + '/api/services/bstudyreport/studentstatistics/StudentNumner'
        self.statisticsgeneraldata = baseurl + '/api/services/bstudyreport/studentstatistics/generaldata'
        self.statisticsvideo = baseurl + '/api/services/bstudyreport/studentstatistics/videoviewersubjectdistribution'
        self.statisticsexercise = baseurl + '/api/services/bstudyreport/studentstatistics/exercisesubjectdistribution'
        self.statisticspsychocate = baseurl + '/api/services/bstudyreport/studentstatistics/psychocategorydistribution'
        self.statisticscareer = baseurl + '/api/services/bstudyreport/studentstatistics/careercategorydistribution'
        self.usagegeneral = baseurl + '/api/services/bstudyreport/studentusage/general'
        self.usagedetails = baseurl + '/api/services/bstudyreport/studentusage/usagedetails'
        self.usagevideodetails = baseurl + '/api/services/bstudyreport/studentusage/videoviewdetails'
        self.usageexerciseanswer = baseurl + '/api/services/bstudyreport/studentusage/exerciseanswerdetails'
        self.usagehomeworklist = baseurl + '/api/services/bstudyreport/studentusage/homeworklist'
        self.staffusagesum = baseurl + '/api/services/bstudyreport/staffUsage/Summary'
        self.staffusagebehavior = baseurl + '/api/services/bstudyreport/staffUsage/OnlineBehavior'
        self.staffusagedetails = baseurl + '/api/services/bstudyreport/staffUsage/OnlineDetails'

        # 作业
        '''计划性大作业_教师端'''
        self.planhomework_getUserHomeworkScenes = baseurl + '/api/eteacherproduct/scene/getUserHomeworkScenes'
        self.planhomework_getHomeworkSceneInfo = baseurl + '/api/eteacherproduct/scene/getHomeworkScene'
        self.planhomework_getDefaultSubject = baseurl + '/api/eteacherproduct/scene/getDefaultSubject'
        self.planhomework_listBigHomeworkSummary = baseurl + '/api/eteacherproduct/basket/listBigHomeworkSummary'
        self.planhomework_listBigHomeworkItems = baseurl + '/api/eteacherproduct/basket/listBigHomeworkItems'
        self.planhomework_removeBasketContent = baseurl + '/api/eteacherproduct/basket/removeBasketContent'
        self.planhomework_addBasketContent = baseurl + '/api/eteacherproduct/basket/addBasketContent'
        self.planhomework_saveAssignContents = baseurl + '/api/eteacherproduct/scene/saveAssignContents'
        self.planhomework_getAssignData = baseurl + '/api/eteacherproduct/scene/getAssignData'
        self.planhomework_makeStudyPlan = baseurl + '/api/eteacherproduct/scene/makeStudyPlan'
        self.planhomework_assignHomework = baseurl + '/api/eteacherproduct/scene/assignHomework'
        self.planhomework_revokeHomework = baseurl + '/api/eteacherproduct/scene/revokeHomework'
        '''计划性大作业_学生端'''
        self.planhomework_getSceneHomeworks = baseurl + '/api/eteacherproduct/scene/getSceneHomeworks'
        self.planhomework_getSceneStatInfo = baseurl + '/api/eteacherproduct/scene/getSceneStatInfo'
        self.planhomework_getSceneStatInfo_wx = wxbaseurl + '/api/eteacherproduct/scene/getSceneStatInfo'
        '''计划性大作业_专题端'''
        self.planhomework_addBasketItems = baseurl + '/api/eteacherproduct/scene/addBasketItems'
        self.planhomework_removeBasketItems = baseurl + '/api/eteacherproduct/scene/removeBasketItems'
        self.planhomework_getBasketInfo = baseurl + '/api/eteacherproduct/scene/getBasketInfo'
        self.planhomework_saveHomeworkData = baseurl + '/api/eteacherproduct/scene/saveHomeworkData'
        self.planhomework_getHomeworkData = baseurl + '/api/eteacherproduct/scene/getHomeworkData'






        # openapi
        self.getuserclass = baseurl + '/api/services/EduOrgan/student/getuserclass'
        self.hasactivityhomeworkpublishpriviledge = baseurl + '/api/services/PromotionActivity/preparatory2022/hasactivityhomeworkpublishpriviledge'
        self.HomeworkPublishEstimated = baseurl + '/api/services/PromotionActivity/preparatory2022/HomeworkPublishEstimated'
        self.PublishActivityHomework = baseurl + '/api/services/PromotionActivity/preparatory2022/PublishActivityHomework'
        self.CheckActivityHomeworkPublish = baseurl + '/api/services/PromotionActivity/preparatory2022/CheckActivityHomeworkPublish'
        self.CheckStudentActivityHomework = baseurl + '/api/services/PromotionActivity/preparatory2022/CheckStudentActivityHomework'
        self.batchuserinfo = baseurl + '/api/services/OpenApi/student/batchuserinfo'
        self.queryTeacherClasses = baseurl + '/api/eteacherproduct/teacher/manage/queryTeacherClasses'

        '''openapi_用户中心'''
        self.vipactivated = baseurl + '/api/services/EduOrgan/OpenApi/vipactivated'

        # 微信端接口
        '''精选资源'''
        self.menuall = wxbaseurl + '/api/eteacherproduct/menu/all'
        self.menuselect = wxbaseurl + '/api/eteacherproduct/menu/select'
        self.solutionlist = wxbaseurl + '/api/eteacherproduct/solution/list'
        self.topicdetail = wxbaseurl + '/api/eteacherproduct/solution/content/topicDetail'
        self.solutioncontent = wxbaseurl + '/api/eteacherproduct/solution/contents'
        self.solutionintroduce = wxbaseurl + '/api/eteacherproduct/solution/introduce'
        self.papergetquestions = wxbaseurl + '/ExternalApi/PaperService/Get'
        self.createpaper = wxbaseurl + '/api/paperlibrary/createpaper'
        self.wxgetclasseswithgradeinfo = wxbaseurl + '/api/services/HomeworkService/weChatHomework/GetClassesWithGradeInfo'
        self.homeworkassign = wxbaseurl + '/api/eteacherproduct/homework/assignment'
        '''我的'''
        self.fetchuserinfo = wxbaseurl + '/api/eteacherproduct/my/fetchuserinfo'
        self.getuserrole = wxbaseurl + '/api/services/EduOrgan/schoolStaff/GetUserRole'
        self.myclasslist = wxbaseurl + '/api/eteacherproduct/my/classlist'
        '''假期调用的接口'''
        self.teacherinfo = wxbaseurl + '/api/eteacherproduct/activity/getTeacherInfo'
        self.schoolhomeworkassigncount = wxbaseurl + '/api/eteacherproduct/activity/getSchoolHomeworkAssignCount'
        self.gradetagAndassignInfo = wxbaseurl + '/api/eteacherproduct/activity/getGradeTagAndAssignInfo'
        self.gradetopcategoryid = wxbaseurl + '/api/eteacherproduct/activity/getGradeTopCategoryId'
        '''督学'''
        self.getteachergradeclassList = wxbaseurl + '/api/eteacherproduct/routine/getTeacherGradeClassList'
        self.gradeweeklydetails = wxbaseurl + '/api/eteacherproduct/routine/getGradeWeeklyDetails'
        self.pagestudenthomeworklist = wxbaseurl + '/api/eteacherproduct/routine/pageStudentHomeworkList'
        #self.studenthomeworkdetaillist = wxbaseurl + '/api/eteacherproduct/routine/studentHomeworkDetailList'
        self.teacherusedetaillist = wxbaseurl + '/api/eteacherproduct/routine/getTeacherUseDetailList'
        self.schoolgradeclasslist = wxbaseurl + '/api/eteacherproduct/routine/getSchoolGradeClassList'
        self.classweeklydetails = wxbaseurl + '/api/eteacherproduct/routine/getClassWeeklyDetails'
        self.reportpraise = wxbaseurl + '/api/eteacherproduct/routine/praise'
        self.homeworkurge = wxbaseurl + '/api/eteacherproduct/routine/urge'
        self.homeworkurgestate = wxbaseurl + '/api/eteacherproduct/routine/urgeState'

        # 错题本
        self.errorquestioncatrgories = baseurl + '/api/eteacherproduct/errorquestion/catrgories'
        self.errorquestionpoints = baseurl + '/api/eteacherproduct/errorquestion/points'
        self.errorquestions = baseurl + '/api/eteacherproduct/errorquestion/errorquestions'
        self.defaultsearchoption = baseurl + '/api/eteacherproduct/errorquestion/defaultsearchoption'



