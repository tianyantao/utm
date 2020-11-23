from config.config_case import ConfigCase



class TeacherZzjUrls:

    def init_zzj_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TEACHER)
        gateway_url = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_GATEWAY)

        '''B端模拟选科'''
        self.analogtea_getquestionnaireinfo = baseurl + '/api/teacher/analogselectionfortea/getquestionnaireinfo'
        self.analogtea_submithomework = baseurl + '/api/teacher/analogselectionfortea/submithomework'
        self.analogtea_getsuccesshomeworkdetail = baseurl + '/api/teacher/analogselectionfortea/getsuccesshomeworkdetail'
        self.analogstu_getlist = baseurl + '/student/subjectsystem/getlist'
        self.analogstu_gethomeworkinfo = baseurl + '/api/student/analogselectionforstu/gethomeworkinfo'
        self.analogstu_submithomework = baseurl + '/api/student/analogselectionforstu/submithomework'
        self.analogtea_GetConditions = baseurl + '/api/teacher/analogselectionfortea/GetConditions'
        self.analogtea_GetListByPage = baseurl + '/api/teacher/analogselectionfortea/GetListByPage'
        self.analogtea_gethomeworkstatisticsinfo = baseurl + '/api/teacher/analogselectionfortea/gethomeworkstatisticsinfo'
        self.analogtea_posthomeworkstatistics = baseurl + '/api/teacher/analogselectionfortea/posthomeworkstatistics'
        self.analogtea_postselectedsubjectlist = baseurl + '/api/teacher/analogselectionfortea/postselectedsubjectlist'
        self.analogtea_HomeworkRecordClasses = baseurl + '/api/services/HomeworkService/AnalogSelection/HomeworkRecordClasses'
        self.analogtea_posthomeworkstatisticsdetail = baseurl + '/api/teacher/analogselectionfortea/posthomeworkstatisticsdetail'
        self.analogtea_cancelsubject = baseurl + '/api/teacher/analogselectionfortea/cancelsubject'

        '''B端常规'''
        self.ads_GetBanners = baseurl + '/api/services/ads/ads/GetBanners'
        self.overview_getlatesthomework = baseurl + '/api/teacher/overview/getlatesthomework'

        '''B端教师查看习题作业'''
        self.exercises_homeworkcompletion = baseurl + '/api/teacher/homework/exercises/homeworkcompletion'
        self.exercises_QuestionAnswerDetail = baseurl + '/api/teacher/homework/exercises/QuestionAnswerDetail'
        self.exercises_KnowledgeErrorRate = baseurl + '/api/teacher/homework/exercises/KnowledgeErrorRate'
        self.exercises_ClassHomeworkCompletion = baseurl + '/api/teacher/homework/exercises/ClassHomeworkCompletion'

        '''B端教师查看视频作业'''
        self.video_StudentHomeworkCompletion = baseurl + "/api/teacher/homework/video/StudentHomeworkCompletion"
        self.video_StudentList = baseurl + "/api/teacher/homework/video/StudentList"
        self.video_VideoPalyViewing = baseurl + "/api/teacher/homework/video/VideoPalyViewing"
        self.video_homeworkcompletion = baseurl + "/api/teacher/homework/video/homeworkcompletion"
        self.video_ClassStudentVideoPlayDetail = baseurl + '/api/teacher/homework/video/ClassStudentVideoPlayDetail'

        '''B端校本视频作业'''
        self.sbrvideo_getvideos = baseurl + '/api/teacher/homework/sbr/getvideos'
        self.sbrvideo_gesbrbasketitems = baseurl + '/api/teacher/homework/sbr/gesbrbasketitems'
        self.sbrvideo_getavailablegrades = baseurl + '/api/teacher/homework/sbr/getavailablegrades'
        self.sbrvideo_addtosbrbasket = baseurl + '/api/teacher/homework/sbr/addtosbrbasket'
        self.sbrvideo_removefromsbrbasket = baseurl + '/api/teacher/homework/sbr/removefromsbrbasket'
        self.sbrvideo_clearsbrbasket = baseurl + '/api/teacher/homework/sbr/clearsbrbasket'
        self.sbrvideo_set_homework = baseurl + '/api/teacher/homework/sbr/set/homework'

        '''用户体系_B端_web教师管理'''
        self.manageteacher_pagerQueryTeacherInfo = gateway_url + '/api/eteacherproduct/teacher/manage/pagerQueryTeacherInfo'
        self.manageteacher_verifyCellphone = gateway_url + '/api/eteacherproduct/teacher/manage/verifyCellphone'
        self.manageteacher_addTeacher = gateway_url + '/api/eteacherproduct/teacher/manage/addTeacher'
        self.manageteacher_removeTeacher = gateway_url + '/api/eteacherproduct/teacher/manage/removeTeacher'
        self.manageteacher_listRole = gateway_url + '/api/eteacherproduct/teacher/manage/listRole'
        self.manageteacher_listTeachSubject = gateway_url + '/api/eteacherproduct/teacher/manage/listTeachSubject'
        self.manageteacher_updateTeacher = gateway_url + '/api/eteacherproduct/teacher/manage/updateTeacher'
        self.manageteacher_queryTeacherRoleInfo = gateway_url + '/api/eteacherproduct/teacher/manage/queryTeacherRoleInfo'
        self.manageteacher_queryMenuInfo = gateway_url + '/api/eteacherproduct/teacher/manage/queryMenuInfo'
        self.manageteacher_queryTeacherGradeClassRole = gateway_url + '/api/eteacherproduct/teacher/manage/queryTeacherGradeClassRole'
        self.manageteacher_joinExecutiveClass = gateway_url + '/api/eteacherproduct/teacher/manage/joinExecutiveClass'
        self.manageteacher_removeTeacherClassRole = gateway_url + '/api/eteacherproduct/teacher/manage/removeTeacherClassRole'
        self.manageteacher_listGrades = gateway_url + '/api/eteacherproduct/teacher/manage/listGrades'
        self.manageteacher_getClassTeacherRole = gateway_url + '/api/eteacherproduct/teacher/manage/getClassTeacherRole'
        self.manageteacher_updateStudentName = gateway_url + '/api/eteacherproduct/teacher/manage/updateStudentName'
        self.manageteacher_queryTeacherRoleAndSchoolInfo = gateway_url + '/api/eteacherproduct/teacher/manage/queryTeacherRoleAndSchoolInfo'
        self.manageteacher_getSchoolUserInfo = gateway_url + '/api/eteacherproduct/school/getSchoolUserInfo'
        self.manageteacher_updateUserName = gateway_url + '/api/eteacherproduct/teacher/manage/updateUserName'
        self.manageteacher_queryCurrentSchoolConf = gateway_url + '/api/eteacherproduct/school/queryCurrentSchoolConf'


        '''用户体系_B端班级管理'''
        self.classesManager_listClassStudent = gateway_url + '/api/eteacherproduct/classesManager/listClassStudent'
        self.classesManager_pageClasses = gateway_url + '/api/eteacherproduct/classesManager/pageClasses'
        self.classesManager_create = gateway_url + '/api/eteacherproduct/classesManager/create'
        self.classesManager_kickStudent = gateway_url + '/api/eteacherproduct/classesManager/kickStudent'
        self.classesManager_dissolveClass = gateway_url + '/api/eteacherproduct/classesManager/dissolveClass'
        self.classesManager_addStudentToTeachingClass = gateway_url + '/api/eteacherproduct/classesManager/addStudentToTeachingClass'
        self.classesManager_listClassesByGrade = gateway_url + '/api/eteacherproduct/classesManager/listClassesByGrade'
        self.classesManager_queryClassInfo = gateway_url + '/api/eteacherproduct/classesManager/queryClassInfo'
        self.classesManager_getEnumDetailList = gateway_url + '/api/eteacherproduct/classesManager/getEnumDetailList'
        self.classesManager_queryAdminStudentList = gateway_url + '/api/eteacherproduct/classesManager/queryAdminStudentList'
        self.classesManager_modifyClassConfig = gateway_url + '/api/eteacherproduct/classesManager/modifyClassConfig'
        self.classesManager_getSchoolClassList = gateway_url + '/api/eteacherproduct/classesManager/getSchoolClassList'
        self.classesManager_modify = gateway_url + '/api/eteacherproduct/classesManager/modify'
        self.classesManager_getSalemanInfo = gateway_url + '/eteacherproduct/school/getSalemanInfo'  # 前端未使用
        self.classesManager_listStudentByHomeworkRange = gateway_url + '/api/eteacherproduct/classesManager/listStudentByHomeworkRange'  # 前端未调用
        # self.classesManager_vipActivated = gateway_url + '/api/eteacherprod/classesManager/vipActivated' #需要有效的激活码，且只能导入一次

        '''用户体系_学生管理'''
        self.studentManage_info = gateway_url + '/api/eteacherproduct/studentManage/info'
        self.studentManage_studentChangeName = gateway_url + '/api/eteacherproduct/studentManage/studentChangeName'
        # self.studentManage_canStudentChangeName = gateway_url + '/api/eteacherproduct/students/canStudentChangeName' #前端未使用，接口调用报404
        self.studentManage_getJoinedClassesAndExtendedInfo = gateway_url + '/api/eteacherproduct/studentManage/getJoinedClassesAndExtendedInfo'
        self.studentManage_getMyClassList = gateway_url + '/api/eteacherproduct/studentManage/getMyClassList'
        self.studentManage_getMySchoolAndGradeClassList = gateway_url + '/api/eteacherproduct/studentManage/getMySchoolAndGradeClassList'
        self.studentManage_getSchoolAndGradeClassList = gateway_url + '/api/eteacherproduct/studentManage/getSchoolAndGradeClassList'
        self.studentManage_checkAddSingleStudentToClass = gateway_url + '/api/eteacherproduct/studentManage/checkAddSingleStudentToClass'
        self.studentManage_joinClass = gateway_url + '/api/eteacherproduct/studentManage/joinClass'
        self.studentManage_oldJoinClass = gateway_url + '/api/eteacherproduct/studentManage/oldJoinClass'


        '''用户体系_教师端后台(pm使用)'''
        self.admin_pageStudentList = gateway_url + '/api/eteacherproduct/admin/classManage/pageStudentList'
        self.admin_pageSchoolList = gateway_url + '/api/eteacherproduct/admin/schoolManage/pageSchoolList'
        self.admin_pageClasses = gateway_url + '/api/eteacherproduct/admin/classManage/pageClasses'  # 仅按班级名称精准查询，按classId精准查询有效
        self.admin_updateSchoolConf = gateway_url + '/api/eteacherproduct/admin/schoolManage/updateSchoolConf'
        self.admin_changeClassByExcel = gateway_url + '/api/eteacherproduct/admin/classManage/changeClassByExcel'  # 文件待调试
        self.admin_getExcelTemplateInfo = gateway_url + '/api/eteacherproduct/admin/classManage/getExcelTemplateInfo'
        self.admin_querySchoolInfo = gateway_url + '/api/eteacherproduct/admin/schoolManage/querySchoolInfo'
        self.admin_queryClassInfo = gateway_url + '/api/eteacherproduct/admin/classManage/queryClassInfo'

        '''用户体系_OA学校教师管理'''
        self.oateacher_querySchoolInfo = gateway_url + '/api/eteacherproduct/oa/schoolManage/querySchoolInfo'
        self.oateacher_addTeacher = gateway_url + '/api/eteacherproduct/oa/teacherManage/addTeacher'
        self.oateacher_queryUserInfoByCellphone = gateway_url + '/api/eteacherproduct/oa/teacherManage/queryUserInfoByCellphone'
        self.oateacher_listTeacher = gateway_url + '/api/eteacherproduct/oa/teacherManage/listTeacher'
        self.oateacher_updateTeacher = gateway_url + '/api/eteacherproduct/oa/teacherManage/updateTeacher'
        self.oateacher_listSimpleTeacher = gateway_url + '/api/eteacherproduct/oa/teacherManage/listSimpleTeacher'
        self.oateacher_removeTeacher = gateway_url + '/api/eteacherproduct/oa/teacherManage/removeTeacher'
        self.oateacher_sendMessages = gateway_url + '/api/eteacherproduct/oa/teacherManage/sendMessages'
        self.oateacher_queryTeacherRoleInfo = gateway_url + '/api/eteacherproduct/oa/teacherManage/queryTeacherRoleInfo'
        self.oateacher_querySubjectInfo = gateway_url + '/api/eteacherproduct/oa/teacherManage/querySubjectInfo'
        self.oateacher_queryPositionInfo = gateway_url + '/api/eteacherproduct/oa/teacherManage/queryPositionInfo'
        self.oateacher_teacherRegister = gateway_url + '/api/eteacherproduct/oa/teacherManage/teacherRegister'  # 用户注册接口，未写

        '''用户体系_OA教师端_班级管理'''
        self.oaclass_list = gateway_url + '/api/eteacherproduct/oa/classManage/list'
        self.oaclass_listGrades = gateway_url + '/api/eteacherproduct/oa/classManage/listGrades'
        self.oaclass_dissolveClass = gateway_url + '/api/eteacherproduct/oa/classManage/dissolveClass'
        self.oaclass_create = gateway_url + '/api/eteacherproduct/oa/classManage/create'
        self.oaclass_modify = gateway_url + '/api/eteacherproduct/oa/classManage/modify'
        self.oaclass_getEnumDetailList = gateway_url + '/api/eteacherproduct/oa/classManage/getEnumDetailList'
        self.oaclass_modifyClassConfig = gateway_url + '/api/eteacherproduct/oa/classManage/modifyClassConfig'
        self.oaclass_listClassStudent = gateway_url + '/api/eteacherproduct/oa/classManage/listClassStudent'
        self.oaclass_queryStudent = gateway_url + '/api/eteacherproduct/oa/classManage/queryStudent'
        self.oaclass_kickStudent = gateway_url + '/api/eteacherproduct/oa/classManage/kickStudent'
        self.oaclass_queryClassInfo = gateway_url + '/api/eteacherproduct/oa/classManage/queryClassInfo'
        self.oaclass_addSingleStudentToClass = gateway_url + '/api/eteacherproduct/oa/classManage/addSingleStudentToClass'
        self.oaclass_getSchoolClassList = gateway_url + '/api/eteacherproduct/oa/classManage/getSchoolClassList'


        '''用户体系_第三方接口'''
        self.class_getClassStudentListByUid = gateway_url + '/schooluserservice/class/getClassStudentListByUid'
        self.class_listTeachingClassByUid = gateway_url + '/schooluserservice/class/listTeachingClassByUid'
        self.class_getClassInfoAndHeadTeacherByClassIdList = gateway_url + '/schooluserservice/class/getClassInfoAndHeadTeacherByClassIdList'
        self.class_getClassStudentListBySchoolAndUid = gateway_url + '/schooluserservice/class/getClassStudentListBySchoolAndUid'
        self.class_getClassStudentListBySchoolAndGrade = gateway_url + '/schooluserservice/class/getClassStudentListBySchoolAndGrade'
        self.class_listClassDetailAndStudentsByClassIdList = gateway_url + '/schooluserservice/class/listClassDetailAndStudentsByClassIdList'
        self.class_listClassDetailAndStudentsByClassIdListContainLeft = gateway_url + '/schooluserservice/class/listClassDetailAndStudentsByClassIdListContainLeft'
        self.class_listClassDetailAndStudents = gateway_url + '/schooluserservice/class/listClassDetailAndStudents'
        self.class_listClassInfoBySchoolAndGradeContainDisbanded = gateway_url + '/schooluserservice/class/listClassInfoBySchoolAndGradeContainDisbanded'
        self.class_listGradeAndClassBySchoolIdAndGrade = gateway_url + '/schooluserservice/class/listGradeAndClassBySchoolIdAndGrade'
        self.class_listGradeAndClassBySchoolId = gateway_url + '/schooluserservice/class/listGradeAndClassBySchoolId'
        self.class_batchAddStudentToClass = gateway_url + '/schooluserservice/class/oa/batchAddStudentToClass'
        self.class_addSingleStudentToAdminClass = gateway_url + '/schooluserservice/class/addSingleStudentToAdminClass'
        self.class_listClassesContainDisbanded = gateway_url + '/schooluserservice/class/listClassesContainDisbanded'
        self.class_getClassInfoListByClassIdList = gateway_url + '/schooluserservice/class/getClassInfoListByClassIdList'

        self.role_getUserRoleWithGrade = gateway_url + '/schooluserservice/role/getUserRoleWithGrade'
        self.role_getUserRoleWithGradeAndTeachClass = gateway_url + '/schooluserservice/role/getUserRoleWithGradeAndTeachClass'
        self.role_getUserRoleWithGradeAndClass = gateway_url + '/schooluserservice/role/getUserRoleWithGradeAndClass'
        self.role_getUserRole = gateway_url + '/schooluserservice/role/getUserRole'

        self.teacher_queryHeadTeacherByClassId = gateway_url + '/schooluserservice/teacher/queryHeadTeacherByClassId'
        self.teacher_queryHeadTeacherByClassIdList = gateway_url + '/schooluserservice/teacher/queryHeadTeacherByClassIdList'
        self.teacher_getTeachInfoListBySchoolAndClass = gateway_url + '/schooluserservice/teacher/getTeachInfoListBySchoolAndClass'


        self.school_listPrincipalsUid = gateway_url + '/schooluserservice/school/listPrincipalsUid'
        self.school_batchSchoolStat = gateway_url + '/schooluserservice/school/batchSchoolStat'
        self.school_getDetailInfoAndConf = gateway_url + '/schooluserservice/school/getDetailInfoAndConf'
        self.school_getSchoolStaffs = gateway_url + '/schooluserservice/school/getSchoolStaffs'
        self.school_getConfigs = gateway_url + '/schooluserservice/school/getConfigs'
        self.school_getSchoolUserInfo = gateway_url + '/schooluserservice/school/getSchoolUserInfo'
        self.school_getSchoolStudentInfo = gateway_url + '/schooluserservice/school/getSchoolStudentInfo'

        self.students_getJoinClassList = gateway_url + '/schooluserservice/students/getJoinClassList'
        self.students_getClassInfoByUserIdList = gateway_url + '/schooluserservice/students/getClassInfoByUserIdList'
        self.students_getAdminClassInfoByUserIdList = gateway_url + '/schooluserservice/students/getAdminClassInfoByUserIdList'
        # self.students_deleteStudent = gateway_url + '/schooluserservice/students/deleteStudent' #500，OA注册账号有限制，且操作账号需要UC开通权限

        self.students_hasJoinedClass = baseurl + '/openapi/student/hasjoinedclass'
        self.manageteacher_teacherGradeList = gateway_url + '/api/eteacherproduct/teacher/manage/teacherGradeList'

        '''校本直播'''
        self.sbrlive_listTeacherLiveRecord = gateway_url + '/api/netschool/sbrlive/listTeacherLiveRecord'
        self.sbrlive_create = gateway_url + '/api/netschool/sbrlive/create'
        self.sbrlive_listTeacherClasses = gateway_url + '/api/netschool/sbrlive/listTeacherClasses'
        self.sbrlive_getLiveInfo = gateway_url + '/api/netschool/sbrlive/getLiveInfo'
        self.sbrlive_edit = gateway_url + '/api/netschool/sbrlive/edit'
        self.sbrlive_delete = gateway_url + '/api/netschool/sbrlive/delete'
        self.sbrlive_pageQueryMyLive = gateway_url + '/api/netschool/sbrlive/pageQueryMyLive'
        self.sbrlive_pageQuerySchoolLive = gateway_url + '/api/netschool/sbrlive/pageQuerySchoolLive'
        self.sbrlive_getLiveToken = gateway_url + '/api/netschool/sbrlive/getLiveToken'
        self.sbrlive_getTeacherLiveToken = gateway_url + '/api/netschool/sbrlive/getTeacherLiveToken'
        self.sbrlive_listLiveRecord = gateway_url + '/api/netschool/sbrlive/listLiveRecord'
        self.sbrlive_listLiveState = gateway_url + '/api/netschool/sbrlive/listLiveState'
        self.sbrlive_uncompleted = gateway_url + '/api/netschool/sbrlive/statistics/uncompleted'
        self.sbrlive_arrangingClassList = gateway_url + '/api/netschool/sbrlive/statistics/arrangingClassList'
        self.sbrlive_overview = gateway_url + '/api/netschool/sbrlive/statistics/overview'
        self.sbrlive_online = gateway_url + '/api/netschool/sbrlive/statistics/online'
        self.sbrlive_details = gateway_url + '/api/netschool/sbrlive/statistics/details'
        self.sbrlive_getRecordAvgDuration = gateway_url + '/api/netschool/sbrlive/statistics/getRecordAvgDuration'
        self.sbrlive_pageQueryRecordDetails = gateway_url + '/api/netschool/sbrlive/statistics/pageQueryRecordDetails'



