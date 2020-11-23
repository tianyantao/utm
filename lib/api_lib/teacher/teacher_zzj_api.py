from lib.api_lib.teacher.teacher_urls import TeacherUrls
import time


def timestampms():
    # 返回延迟一天的时间戳（ms）
    timestamp = time.time()
    timestamp1 = int(timestamp) + 86400
    return int(round(timestamp1 * 1000))


class TeacherZzj:
    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()

    # B端模拟选科
    def analogtea_getquestionnaireinfo(self, grade, type):
        post_data = {"grade": grade, "type": type}
        return self.client.post(url=self.url_builder.analogtea_getquestionnaireinfo, data=post_data)

    def analogtea_submithomework(self, grade, type, title, subjectgroups, endtime):
        post_data = {"grade": grade, "type": type, "title": title, "subjectgroups": subjectgroups, "endtime": endtime}
        return self.client.post(url=self.url_builder.analogtea_submithomework, data=post_data)

    def analogtea_getsuccesshomeworkdetail(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogtea_getsuccesshomeworkdetail, data=post_data)

    def analogstu_getlist(self):
        return self.client.get(url=self.url_builder.analogstu_getlist)

    def analogstu_gethomeworkinfo(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogstu_gethomeworkinfo, data=post_data)

    def analogstu_submithomework(self, homeworkid, lastsubjects, type, subjectgroupid):
        post_data = {"homeworkid": homeworkid, "lastsubjects": lastsubjects, "type": type,
                     "subjectgroupid": subjectgroupid}
        return self.client.post(url=self.url_builder.analogstu_submithomework, data=post_data)

    def analogtea_GetConditions(self):
        return self.client.post(url=self.url_builder.analogtea_GetConditions)

    def analogtea_GetListByPage(self, keyword, starttime, endtime, grade, type, status, pageindex):
        post_data = {"keyword": keyword, "starttime": starttime, "endtime": endtime, "grade": grade, "type": type,
                     "status": status, "pageindex": pageindex}
        return self.client.post(url=self.url_builder.analogtea_GetListByPage, data=post_data)

    def analogtea_gethomeworkstatisticsinfo(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogtea_gethomeworkstatisticsinfo, data=post_data)

    def analogtea_posthomeworkstatistics(self, homeworkid, classId):
        post_data = {"homeworkid": homeworkid, "classId": classId}
        return self.client.post(url=self.url_builder.analogtea_posthomeworkstatistics, data=post_data)

    def analogtea_postselectedsubjectlist(self, homeworkid, classid, type, pageindex, pagesize, singlesubject,
                                          subjectgroupid):
        post_data = {"homeworkid": homeworkid,
                     "classid": classid,
                     "type": type,
                     "pageindex": pageindex,
                     "pagesize": pagesize,
                     "singlesubjectid": singlesubject,
                     "subjectgroupid": subjectgroupid
                     }
        return self.client.post(url=self.url_builder.analogtea_postselectedsubjectlist, data=post_data)

    def analogtea_HomeworkRecordClasses(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogtea_HomeworkRecordClasses, data=post_data)

    def analogtea_posthomeworkstatisticsdetail(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogtea_posthomeworkstatisticsdetail, data=post_data)

    def analogtea_cancelsubject(self, homeworkid):
        post_data = {"homeworkid": homeworkid}
        return self.client.post(url=self.url_builder.analogtea_cancelsubject, data=post_data)

    # B端常规
    def ads_getbanners(self):
        return self.client.post(url=self.url_builder.ads_GetBanners)

    def overview_getlatesthomework(self):
        return self.client.post(url=self.url_builder.overview_getlatesthomework, data={})

    # B端生涯视频作业
    def career_postheadertypelist(self, newclsid):
        post_data = {"newclsid": newclsid}
        return self.client.post(url=self.url_builder.career_postheadertypelist, data=post_data)

    def career_gethomworklist(self, typeid, parentid, childid, pageindex, pagesize):
        post_data = {"typeid": typeid, "parentid": parentid, "childid": childid, "pageindex": pageindex,
                     "pagesize": pagesize}
        return self.client.post(url=self.url_builder.career_gethomworklist, data=post_data)

    def career_addbasket(self, basketforteaaddinput):
        post_data = {"basketforteaaddinput": basketforteaaddinput}
        return self.client.post(url=self.url_builder.career_addbasket, data=post_data)

    def career_removebaseket(self, qid, typeid, kemu):
        post_data = {"qid": qid, "typeid": typeid, "kemu": kemu}
        return self.client.post(url=self.url_builder.career_removebaseket, data=post_data)

    def career_clearbasket(self, typeid, kemu):
        post_data = {"typeid": typeid, "kemu": kemu}
        return self.client.post(url=self.url_builder.career_clearbasket, data=post_data)

    def career_getbaseketvideolist(self, typeid, kemu):
        post_data = {"typeid": typeid, "kemu": kemu}
        return self.client.post(url=self.url_builder.career_getbaseketvideolist, data=post_data)

    def career_submithomework(self, json, homeworkxueketype, submiting):
        post_data = {"json": json, "homeworkxueketype": homeworkxueketype, "submiting": submiting}
        return self.client.post(url=self.url_builder.career_submithomework, data=post_data)

    # B端教师端习题作业
    def exercises_classhomeworkcompletion(self, homeworkid, sort, page, pagesize, classid, studentname):
        post_data = {"homeworkid": homeworkid, "sort": sort, "page": page, "pagesize": pagesize, "classid": classid,
                     "studentname": studentname}
        return self.client.post(url=self.url_builder.exercises_ClassHomeworkCompletion, data=post_data)

    def exercises_homeworkcompletion(self, sort, homeworkid, page, pagesize):
        post_data = {"sort": sort, "homeworkid": homeworkid, "page": page, "pagesieze": pagesize}
        return self.client.post(url=self.url_builder.exercises_homeworkcompletion, data=post_data)

    def exercises_KnowledgeErrorRate(self, homeworkid, classid):
        post_data = {"homeworkid": homeworkid, "classid": classid}
        return self.client.post(url=self.url_builder.exercises_KnowledgeErrorRate, data=post_data)

    def exercises_QuestionAnswerDetail(self, classid, homeworkid, sort):
        post_data = {"classid": classid, "homeworkid": homeworkid, "sort": sort}
        return self.client.post(url=self.url_builder.exercises_QuestionAnswerDetail, data=post_data)

    # B端教师端学科视频作业
    def video_StudentHomeworkCompletion(self, classid, homeworkid, page, pagesize, sort, studentuserid):
        post_data = {"classid": classid, "homeworkId": homeworkid, "page": page, "pagesize": pagesize, "sort": sort,
                     "studentuserid": studentuserid}
        return self.client.post(url=self.url_builder.video_StudentHomeworkCompletion, data=post_data)

    def video_StudentList(self, classid, homeworkid, searchname, sort):
        post_data = {"classid": classid, "homeworkid": homeworkid, "searchname": searchname, "sort": sort}
        return self.client.post(url=self.url_builder.video_StudentList, data=post_data)

    def video_VideoPalyViewing(self, homeworkid, classid, page, pagesize, sort):
        post_data = {"homeworkid": homeworkid, "classid": classid, "page": page, "pagesize": pagesize, "sort": sort}
        return self.client.post(url=self.url_builder.video_VideoPalyViewing, data=post_data)

    def video_homeworkcompletion(self, homeworkid, page, pagesize, sort):
        post_data = {"homeworkId": homeworkid, "page": page, "pagesize": pagesize, "sort": sort}
        return self.client.post(url=self.url_builder.video_homeworkcompletion, data=post_data)

    def video_ClassStudentVideoPlayDetail(self, homeworkid, videoid, sort, page, pagesize, classid):
        post_data = {"homeworkId": homeworkid, "videoId": videoid, "sort": sort, "page": page, "pagesize": pagesize,
                     "classid": classid}
        return self.client.post(url=self.url_builder.video_ClassStudentVideoPlayDetail, data=post_data)

    # B端校本视频作业
    def sbrvideo_getvideos(self, kemu, grades, page, pagesize, **kwargs):
        post_data = {"KeMu": kemu, "Grades": grades, "page": page, "pagesize": pagesize}
        for k in kwargs:
            post_data[k] = kwargs[k]
        return self.client.post(url=self.url_builder.sbrvideo_getvideos, data=post_data)

    def sbrvideo_gesbrbasketitems(self, page, pagesize, homeworksbrtype, kemu):
        post_data = {"page": page, "pagesize": pagesize, "homeworksbrtype": homeworksbrtype, "kemu": kemu}
        return self.client.post(url=self.url_builder.sbrvideo_gesbrbasketitems, data=post_data)

    def sbrvideo_getavailablegrades(self):
        return self.client.post(url=self.url_builder.sbrvideo_getavailablegrades)

    def sbrvideo_addtosbrbasket(self, homeworksbrtype, basketaddinputs):
        post_data = {"HomeworkSbrType": homeworksbrtype, "BasketAddInputs": basketaddinputs}
        return self.client.post(url=self.url_builder.sbrvideo_addtosbrbasket, data=post_data)

    def sbrvideo_removefromsbrbasket(self, rid, homeworksbrtype, kemu):
        post_data = {"rid": rid, "homeworksbrtype": homeworksbrtype, "kemu": kemu}
        return self.client.post(url=self.url_builder.sbrvideo_removefromsbrbasket, data=post_data)

    def sbrvideo_clearsbrbasket(self, homeworksbrtype, kemu):
        post_data = {"homeworksbrtype": homeworksbrtype, "kemu": kemu}
        return self.client.post(url=self.url_builder.sbrvideo_clearsbrbasket, data=post_data)

    def sbrvideo_set_homework(self, arrangetype, classtype, title, isgradehomework, deadline, kemu, expireyears,
                              gradeclasses):
        post_data = {"arrangetype": arrangetype, "classtype": classtype, "title": title,
                     "isgradehomework": isgradehomework,
                     "deadline": deadline, "kemu": kemu, "ExpireYears": expireyears, "GradeClasses": gradeclasses}
        return self.client.post(url=self.url_builder.sbrvideo_set_homework, data=post_data)

    # 用户体系_B端_web教师管理
    def manageteacher_pagerQueryTeacherInfo(self, schoolId, pageIndex, pageSize, **kwargs):
        post_data = {"schoolId": schoolId, "pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.manageteacher_pagerQueryTeacherInfo, data=post_data)

    def manageteacher_verifyCellphone(self, cellphone, schoolId):
        params = {"cellphone": cellphone, "schoolId": schoolId}
        return self.client.get(url=self.url_builder.manageteacher_verifyCellphone, params=params)

    def manageteacher_addTeacher(self, userId, schoolId, cellphone, teacherName, roleList):
        post_data = {"userId": userId, "schoolId": schoolId, "cellphone": cellphone, "teacherName": teacherName,
                     "roleList": roleList}
        return self.client.post(url=self.url_builder.manageteacher_addTeacher, data=post_data)

    def manageteacher_removeTeacher(self, userId, schoolId):
        params = {"userId": userId, "schoolId": schoolId}
        return self.client.get(url=self.url_builder.manageteacher_removeTeacher, params=params)

    def manageteacher_listRole(self, needAll):
        params = {"needAll": needAll}
        return self.client.get(url=self.url_builder.manageteacher_listRole, params=params)

    def manageteacher_listTeachSubject(self, needAll):
        params = {"needAll": needAll}
        return self.client.get(url=self.url_builder.manageteacher_listTeachSubject, params=params)

    def manageteacher_updateTeacher(self, userId, schoolId, cellphone, teacherName, roleList):
        post_data = {"userId": userId, "schoolId": schoolId, "cellphone": cellphone, "teacherName": teacherName,
                     "roleList": roleList}
        return self.client.post(url=self.url_builder.manageteacher_updateTeacher, data=post_data)

    def manageteacher_queryTeacherRoleInfo(self, schoolId, userId):
        params = {"schoolId": schoolId, "userId": userId}
        return self.client.get(url=self.url_builder.manageteacher_queryTeacherRoleInfo, params=params)

    def manageteacher_queryMenuInfo(self):
        return self.client.get(url=self.url_builder.manageteacher_queryMenuInfo)

    def manageteacher_queryTeacherGradeClassRole(self, schoolId, userId):
        params = {"schoolId": schoolId, "userId": userId}
        return self.client.get(url=self.url_builder.manageteacher_queryTeacherGradeClassRole, params=params)

    def manageteacher_joinExecutiveClass(self, userId, role, classId, schoolId):
        post_data = {"schoolId": schoolId, "userId": userId, "role": role, "classId": classId}
        return self.client.post(url=self.url_builder.manageteacher_joinExecutiveClass, data=post_data)

    def manageteacher_removeTeacherClassRole(self, schoolId, userId, classId, role):
        post_data = {"schoolId": schoolId, "userId": userId, "classId": classId, "role": role}
        return self.client.post(url=self.url_builder.manageteacher_removeTeacherClassRole, data=post_data)

    def manageteacher_listGrades(self, checkEarlyRise):
        params = {"checkEarlyRise": checkEarlyRise}
        return self.client.get(url=self.url_builder.manageteacher_listGrades, params=params)

    def manageteacher_getClassTeacherRole(self, userId, classId, schoolId):
        params = {"userId": userId, "classId": classId, "schoolId": schoolId}
        return self.client.get(url=self.url_builder.manageteacher_getClassTeacherRole, params=params)

    def manageteacher_updateStudentName(self, schoolId, classId, studentId, name):
        post_data = {"schoolId": schoolId, "classId": classId, "studentId": studentId, "name": name}
        return self.client.post(url=self.url_builder.manageteacher_updateStudentName, data=post_data)

    def manageteacher_queryTeacherRoleAndSchoolInfo(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.manageteacher_queryTeacherRoleAndSchoolInfo, params=params)

    def manageteacher_getSchoolUserInfo(self):
        return self.client.get(url=self.url_builder.manageteacher_getSchoolUserInfo)

    def manageteacher_updateUserName(self, userId, name):
        params = {"userId": userId, "name": name}
        return self.client.get(url=self.url_builder.manageteacher_updateUserName, params=params)

    def manageteacher_queryCurrentSchoolConf(self):
        return self.client.get(url=self.url_builder.manageteacher_queryCurrentSchoolConf)

    # 用户体系_B端_web班级管理
    def classesManager_listClassStudent(self, schoolId, classId, keyword, sort, pageIndex, pageSize):
        post_data = {"schoolId": schoolId, "classId": classId, "keyword": keyword, "sort": sort, "pageIndex": pageIndex,
                     "pageSize": pageSize}
        return self.client.post(url=self.url_builder.classesManager_listClassStudent, data=post_data)

    def classesManager_pageClasses(self, className, classType, graduationYear, pageIndex, pageSize):
        post_data = {"className": className, "classType": classType,
                     "graduationYear": graduationYear, "pageIndex": pageIndex, "pageSize": pageSize}
        return self.client.post(url=self.url_builder.classesManager_pageClasses, data=post_data)

    def classesManager_create(self, schoolId, type, graduationYear, allowUserJoinValue, allowStudentChangeValue,
                              **kwargs):
        post_data = {"schoolId": schoolId, "type": type, "graduationYear": graduationYear,
                     "allowUserJoinValue": allowUserJoinValue, "allowStudentChangeValue": allowStudentChangeValue}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.classesManager_create, json=post_data)

    def classesManager_kickStudent(self, schoolId, classId, userId):
        post_data = {"schoolId": schoolId, "classId": classId, "userId": userId}
        return self.client.post(url=self.url_builder.classesManager_kickStudent, data=post_data)

    def classesManager_dissolveClass(self, classId):
        post_data = {"classId": classId}
        return self.client.post(url=self.url_builder.classesManager_dissolveClass, data=post_data)

    def classesManager_addStudentToTeachingClass(self, classId, userIdList):
        post_data = {"classId": classId, "userIdList": userIdList}
        return self.client.post(url=self.url_builder.classesManager_addStudentToTeachingClass, data=post_data)

    def classesManager_listClassesByGrade(self, schoolId, graduationYear):
        params = {"schoolId": schoolId, "graduationYear": graduationYear}
        return self.client.get(url=self.url_builder.classesManager_listClassesByGrade, params=params)

    def classesManager_queryClassInfo(self, classId):
        params = {"classId": classId}
        return self.client.get(url=self.url_builder.classesManager_queryClassInfo, params=params)

    def classesManager_getEnumDetailList(self, type):
        params = {"type": type}
        return self.client.get(url=self.url_builder.classesManager_getEnumDetailList, params=params)

    def classesManager_queryAdminStudentList(self, classId):
        post_data = {"classId": classId}
        return self.client.post(url=self.url_builder.classesManager_queryAdminStudentList, data=post_data)

    def classesManager_modifyClassConfig(self, classIdList, classConfig, updateUser):
        post_data = {"classIdList": classIdList, "classConfig": classConfig, "updateUser": updateUser}
        return self.client.post(url=self.url_builder.classesManager_modifyClassConfig, data=post_data)

    def classesManager_getSchoolClassList(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.classesManager_getSchoolClassList, params=params)

    def classesManager_modify(self, id, schoolId, type, graduationYear, allowUserJoinValue, allowStudentChangeValue,
                              **kwargs):
        post_data = {"id": id, "schoolId": schoolId, "type": type, "graduationYear": graduationYear,
                     "allowUserJoinValue": allowUserJoinValue, "allowStudentChangeValue": allowStudentChangeValue}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.classesManager_modify, data=post_data)

    # def classesManager_listStudentByHomeworkRange(self, schoolId, gradeYearInfo, classIdList):
    #     post_data = {"schoolId":schoolId, "gradeYearInfo":gradeYearInfo, "classIdList":classIdList}
    #     return self.client.post(url=self.url_builder.classesManager_listStudentByHomeworkRange, data=post_data)

    def studentManage_info(self):
        return self.client.get(url=self.url_builder.studentManage_info)

    def studentManage_studentChangeName(self, schoolId, userId, name):
        params = {"schoolId": schoolId, "userId": userId, "name": name}
        return self.client.get(url=self.url_builder.studentManage_studentChangeName, params=params)

    # def studentManage_canStudentChangeName(self, schoolId, userId):
    #     params = {"schoolId":schoolId, "userId":userId}
    #     return self.client.get(url=self.url_builder.studentManage_canStudentChangeName, params=params)
    def studentManage_getJoinedClassesAndExtendedInfo(self):
        return self.client.get(url=self.url_builder.studentManage_getJoinedClassesAndExtendedInfo)

    def studentManage_getMyClassList(self):
        return self.client.get(url=self.url_builder.studentManage_getMyClassList)

    def studentManage_getMySchoolAndGradeClassList(self):
        return self.client.get(url=self.url_builder.studentManage_getMySchoolAndGradeClassList)

    def studentManage_getSchoolAndGradeClassList(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.studentManage_getSchoolAndGradeClassList, params=params)

    def studentManage_checkAddSingleStudentToClass(self, classId):
        post_data = {"classId": classId}
        return self.client.post(url=self.url_builder.studentManage_checkAddSingleStudentToClass, data=post_data)

    def studentManage_joinClass(self, token, headMasterName):
        post_data = {"token": token, "headMasterName": headMasterName}
        return self.client.post(url=self.url_builder.studentManage_joinClass, data=post_data)

    def studentManage_oldJoinClass(self, classId, headMasterName, **kwargs):
        post_data = {"classId": classId, "headMasterName": headMasterName}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.studentManage_oldJoinClass, data=post_data)

    # '''用户体系_教师端后台(pm使用)'''
    def admin_pageStudentList(self, schoolId, classId, pageIndex, pageSize, **kwargs):
        post_data = {"schoolId": schoolId, "classId": classId, "pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.admin_pageStudentList, data=post_data)

    def admin_pageSchoolList(self, schoolName, pageIndex, pageSize, **kwargs):
        post_data = {"schoolName": schoolName, "pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.admin_pageSchoolList, data=post_data)

    def admin_pageClasses(self, schoolId, pageIndex, pageSize, **kwargs):
        post_data = {"schoolId": schoolId, "pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.admin_pageClasses, data=post_data)

    def admin_updateSchoolConf(self, schoolId, confKey, confValue):
        post_data = {"schoolId": schoolId, "confKey": confKey, "confValue": confValue}
        return self.client.post(url=self.url_builder.admin_updateSchoolConf, data=post_data)

    def admin_changeClassByExcel(self, files):
        return self.client.post(url=self.url_builder.admin_changeClassByExcel, file=files)

    def admin_getExcelTemplateInfo(self):
        return self.client.get(url=self.url_builder.admin_getExcelTemplateInfo)

    def admin_querySchoolInfo(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.admin_querySchoolInfo, params=params)

    def admin_queryClassInfo(self, classId):
        params = {"classId": classId}
        return self.client.get(url=self.url_builder.admin_queryClassInfo, params=params)

    # 用户体系_第三方接口-class
    def class_getClassStudentListByUid(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.class_getClassStudentListByUid, params=params)

    def class_listTeachingClassByUid(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.class_listTeachingClassByUid, params=params)

    def class_getClassInfoAndHeadTeacherByClassIdList(self, classIdList):
        params = {"classIdList": classIdList}
        return self.client.get(url=self.url_builder.class_getClassInfoAndHeadTeacherByClassIdList, params=params)

    def class_getClassStudentListBySchoolAndUid(self, schoolId, userId):
        params = {"schoolId": schoolId, "userId": userId}
        return self.client.get(url=self.url_builder.class_getClassStudentListBySchoolAndUid, params=params)

    def class_getClassStudentListBySchoolAndGrade(self, schoolId, graduationYear):
        params = {"schoolId": schoolId, "graduationYear": graduationYear}
        return self.client.get(url=self.url_builder.class_getClassStudentListBySchoolAndGrade, params=params)

    def class_listClassDetailAndStudentsByClassIdList(self, classIdList, schoolId):
        post_data = {"classIdList": classIdList, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.class_listClassDetailAndStudentsByClassIdList, data=post_data)

    def class_listClassDetailAndStudentsByClassIdListContainLeft(self, classIdList, schoolId):
        post_data = {"classIdList": classIdList, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.class_listClassDetailAndStudentsByClassIdListContainLeft,
                                data=post_data)

    def class_listClassDetailAndStudents(self, classAndStudentList):
        post_data = {"classAndStudentList": classAndStudentList}
        return self.client.post(url=self.url_builder.class_listClassDetailAndStudents, data=post_data)

    def class_listClassInfoBySchoolAndGradeContainDisbanded(self, gradeYearList, schoolId):
        post_data = {"gradeYearList": gradeYearList, "schoolId": schoolId}
        return self.client.post(url=self.url_builder.class_listClassInfoBySchoolAndGradeContainDisbanded,
                                data=post_data)

    def class_listGradeAndClassBySchoolIdAndGrade(self, schoolId, graduationYearList):
        params = {"schoolId": schoolId, "graduationYearList": graduationYearList}
        return self.client.get(url=self.url_builder.class_listGradeAndClassBySchoolIdAndGrade, params=params)

    def class_listGradeAndClassBySchoolId(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.class_listGradeAndClassBySchoolId, params=params)

    def class_batchAddStudentToClass(self, schoolId, studentList):
        post_data = {"schoolId": schoolId, "studentList": studentList}
        return self.client.post(url=self.url_builder.class_batchAddStudentToClass, data=post_data)

    def class_addSingleStudentToAdminClass(self, userId, classId):
        post_data = {"userId": userId, "classId": classId}
        return self.client.post(url=self.url_builder.class_addSingleStudentToAdminClass, data=post_data)

    def class_listClassesContainDisbanded(self, classIdList):
        post_data = {"classIdList": classIdList}
        return self.client.post(url=self.url_builder.class_listClassesContainDisbanded, data=post_data)

    def class_getClassInfoListByClassIdList(self, classIdList):
        post_data = {"classIdList": classIdList}
        return self.client.post(url=self.url_builder.class_getClassInfoListByClassIdList, data=post_data)

    # 用户体系_第三方接口-role
    def role_getUserRoleWithGrade(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.role_getUserRoleWithGrade, params=params)

    def role_getUserRoleWithGradeAndTeachClass(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.role_getUserRoleWithGradeAndTeachClass, params=params)

    def role_getUserRoleWithGradeAndClass(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.role_getUserRoleWithGradeAndClass, params=params)

    def role_getUserRole(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.role_getUserRole, params=params)

    # 用户体系_第三方接口-teacher
    def teacher_queryHeadTeacherByClassId(self, classId):
        params = {"classId": classId}
        return self.client.get(url=self.url_builder.teacher_queryHeadTeacherByClassId, params=params)

    def teacher_queryHeadTeacherByClassIdList(self, classIdList):
        params = {"classIdList": classIdList}
        return self.client.get(url=self.url_builder.teacher_queryHeadTeacherByClassIdList, params=params)

    def teacher_getTeachInfoListBySchoolAndClass(self, schoolId, classId):
        params = {"schoolId": schoolId, "classId": classId}
        return self.client.get(url=self.url_builder.teacher_getTeachInfoListBySchoolAndClass, params=params)

    # 用户体系_第三方接口-school
    def school_listPrincipalsUid(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.school_listPrincipalsUid, params=params)

    def school_batchSchoolStat(self, schoolIdList):
        post_data = {"schoolIdList": schoolIdList}
        return self.client.post(url=self.url_builder.school_batchSchoolStat, data=post_data)

    def school_getDetailInfoAndConf(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.school_getDetailInfoAndConf, params=params)

    def school_getSchoolStaffs(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.school_getSchoolStaffs, params=params)

    def school_getConfigs(self, schoolId):
        params = {"schoolId": schoolId}
        return self.client.get(url=self.url_builder.school_getConfigs, params=params)

    def school_getSchoolUserInfo(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.school_getSchoolUserInfo, params=params)

    def school_getSchoolStudentInfo(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.school_getSchoolStudentInfo, params=params)

    # 用户体系_第三方接口-student
    def students_getJoinClassList(self, schoolId, userId):
        params = {"schoolId": schoolId, "userId": userId}
        return self.client.get(url=self.url_builder.students_getJoinClassList, params=params)

    def students_getClassInfoByUserIdList(self, schoolId, userIdList):
        params = {"schoolId": schoolId, "userIdList": userIdList}
        return self.client.get(url=self.url_builder.students_getClassInfoByUserIdList, params=params)

    def students_getAdminClassInfoByUserIdList(self, schoolId, userIdList):
        params = {"schoolId": schoolId, "userIdList": userIdList}
        return self.client.get(url=self.url_builder.students_getAdminClassInfoByUserIdList, params=params)

    # def students_deleteStudent(self, userId, schoolId):
    #     post_data = {"userId":userId, "schoolId":schoolId}
    #     return self.client.post(url=self.url_builder.students_deleteStudent, data=post_data)

    # 用户体系_第三方接口-其他
    def students_hasJoinedClass(self, userId):
        post_data = {
            "now": 15533562626,
            "sign": "34055fee31712e930d6dc36d6789d6b3",
            "payload": 80034664
        }
        params = {"userId": userId}
        return self.client.post(url=self.url_builder.students_hasJoinedClass, json=post_data, params=params)

    def manageteacher_teacherGradeList(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.manageteacher_teacherGradeList, params=params)

    # 用户体系_OA教师端
    def oateacher_querySchoolInfo(self):
        return self.client.get(url=self.url_builder.oateacher_querySchoolInfo)

    def oateacher_addTeacher(self, userId, cellphone, teacherName, roleList):
        post_data = {"userId": userId, "cellphone": cellphone, "teacherName": teacherName, "roleList": roleList}
        header = {"Content-Type": "application/json"}
        return self.client.post(url=self.url_builder.oateacher_addTeacher, json=post_data, headers=header)

    def oateacher_queryUserInfoByCellphone(self, cellphone):
        params = {"cellphone": cellphone}
        return self.client.get(url=self.url_builder.oateacher_queryUserInfoByCellphone, params=params)

    def oateacher_listTeacher(self, pageIndex, pageSize, **kwargs):
        post_data = {"pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.oateacher_listTeacher, json=post_data)

    def oateacher_updateTeacher(self, userId, cellphone, teacherName, roleList):
        post_data = {"userId": userId, "cellphone": cellphone, "teacherName": teacherName, "roleList": roleList}
        return self.client.post(url=self.url_builder.oateacher_updateTeacher, json=post_data)

    def oateacher_listSimpleTeacher(self):
        return self.client.get(url=self.url_builder.oateacher_listSimpleTeacher)

    def oateacher_removeTeacher(self, teacherId):
        params = {"teacherId": teacherId}
        return self.client.get(url=self.url_builder.oateacher_removeTeacher, params=params)

    def oateacher_sendMessages(self, userIdList):
        post_data = {"userIdList": userIdList}
        return self.client.post(url=self.url_builder.oateacher_sendMessages, json=post_data)

    def oateacher_queryTeacherRoleInfo(self, userId):
        params = {"userId": userId}
        return self.client.get(url=self.url_builder.oateacher_queryTeacherRoleInfo, params=params)

    def oateacher_querySubjectInfo(self):
        return self.client.get(url=self.url_builder.oateacher_querySubjectInfo)

    def oateacher_queryPositionInfo(self, needAll):
        params = {"needAll": needAll}
        return self.client.get(url=self.url_builder.oateacher_queryPositionInfo, params=params)

    def oateacher_teacherRegister(self):
        return self.client.get(url=self.url_builder.oateacher_teacherRegister)

    # 用户体系_OA班级管理
    def oaclass_list(self, schoolId, pageIndex, pageSize, **kwargs):
        post_data = {"schoolId": schoolId, "pageIndex": pageIndex, "pageSize": pageSize}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.oaclass_list, json=post_data)

    def oaclass_listGrades(self):
        return self.client.get(url=self.url_builder.oaclass_listGrades)

    def oaclass_dissolveClass(self, classId):
        post_data = {"classId": classId}
        return self.client.post(url=self.url_builder.oaclass_dissolveClass, json=post_data)

    def oaclass_create(self, schoolId, type, graduationYear, allowUserJoinValue, allowStudentChangeValue, **kwargs):
        post_data = {"schoolId": schoolId, "type": type, "graduationYear": graduationYear,
                     "allowUserJoinValue": allowUserJoinValue, "allowStudentChangeValue": allowStudentChangeValue}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.oaclass_create, json=post_data)

    def oaclass_modify(self, id, schoolId, type, graduationYear, allowUserJoinValue, allowStudentChangeValue, **kwargs):
        post_data = {"id": id, "schoolId": schoolId, "type": type, "graduationYear": graduationYear,
                     "allowUserJoinValue": allowUserJoinValue,
                     "allowStudentChangeValue": allowStudentChangeValue}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.oaclass_modify, json=post_data)

    def oaclass_getEnumDetailList(self, type):
        params = {"type": type}
        return self.client.get(url=self.url_builder.oaclass_getEnumDetailList, params=params)

    def oaclass_modifyClassConfig(self, classIdList, classConfig, updateUser):
        post_data = {"classIdList": classIdList, "classConfig": classConfig, "updateUser": updateUser}
        return self.client.post(url=self.url_builder.oaclass_modifyClassConfig, json=post_data)

    def oaclass_listClassStudent(self, classId, account, userId, userName, pageIndex, pageSize):
        post_data = {"classId": classId, "account": account, "userId": userId, "userName": userName,
                     "pageIndex": pageIndex, "pageSize": pageSize}
        return self.client.post(url=self.url_builder.oaclass_listClassStudent, json=post_data)

    def oaclass_queryStudent(self, account, userId, mobile, classId):
        post_data = {"account": account, "userId": userId, "mobile": mobile, "classId": classId}
        return self.client.post(url=self.url_builder.oaclass_queryStudent, json=post_data)

    def oaclass_kickStudent(self, classId, userId, updateUser):
        post_data = {"classId": classId, "userId": userId, "updateUser": updateUser}
        return self.client.post(url=self.url_builder.oaclass_kickStudent, json=post_data)

    def oaclass_queryClassInfo(self, classId):
        params = {"classId": classId}
        return self.client.get(url=self.url_builder.oaclass_queryClassInfo, params=params)

    def oaclass_addSingleStudentToClass(self, schoolId, classId, userId, createUser):
        post_data = {"schoolId": schoolId, "classId": classId, "userId": userId, "createUser": createUser}
        return self.client.post(url=self.url_builder.oaclass_addSingleStudentToClass, json=post_data)

    def oaclass_getSchoolClassList(self):
        return self.client.get(url=self.url_builder.oaclass_getSchoolClassList)

   #校本直播
    def sbrlive_listTeacherLiveRecord(self, liveId):
        params = {"liveId":liveId}
        return self.client.get(url=self.url_builder.sbrlive_listTeacherLiveRecord, params=params)

    def sbrlive_create(self, liveName, roomStyle, startTime, finishTime, classType, numberOfStudent, gradeClassList, **kwargs):
        post_data = {"liveName":liveName, "roomStyle":roomStyle, "startTime":startTime, "finishTime":finishTime,
                     "classType":classType, "numberOfStudent":numberOfStudent, "gradeClassList":gradeClassList}
        if kwargs:
            post_data.update(kwargs)
            header = {"token" : self.client.user_token}
        return self.client.post(url=self.url_builder.sbrlive_create, data=post_data, headers=header)

    def sbrlive_listTeacherClasses(self):
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_listTeacherClasses, headers=header)

    def sbrlive_getLiveInfo(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_getLiveInfo, params=params, headers=header)

    def sbrlive_edit(self, liveName, roomStyle, startTime, finishTime, classType, numberOfStudent, gradeClassList, **kwargs):
        post_data = { "liveName":liveName, "roomStyle":roomStyle, "startTime":startTime, "finishTime":finishTime,
                     "classType":classType, "numberOfStudent":numberOfStudent, "gradeClassList":gradeClassList}
        if kwargs:
            post_data.update(kwargs)
            header = {"token": self.client.user_token}
        return self.client.post(url=self.url_builder.sbrlive_edit, data=post_data, headers=header)

    def sbrlive_delete(self, liveId):
        post_data = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.post(url=self.url_builder.sbrlive_delete, data=post_data, headers=header)

    def sbrlive_pageQueryMyLive(self,  liveStatus,  pageIndex, pageSize, **kwargs):
        post_data = { "liveStatus":liveStatus, "pageIndex":pageIndex, "pageSize":pageSize}
        header = {"token": self.client.user_token}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.sbrlive_pageQueryMyLive, data=post_data, headers=header)

    def sbrlive_pageQuerySchoolLive(self, liveStatus, pageIndex, pageSize, **kwargs):
        post_data = {"liveStatus":liveStatus, "pageIndex":pageIndex, "pageSize":pageSize}
        header = {"token": self.client.user_token}
        if kwargs:
            post_data.update(kwargs)
        return self.client.post(url=self.url_builder.sbrlive_pageQuerySchoolLive, data=post_data, headers=header)

    def sbrlive_getLiveToken(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_getLiveToken, params=params, headers=header)

    def sbrlive_getTeacherLiveToken(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_getTeacherLiveToken, params=params, headers=header)

    def sbrlive_listLiveRecord(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_listLiveRecord, params=params, headers=header)

    def sbrlive_listLiveState(self, liveIdList):
        post_data = {"liveIdList":liveIdList}
        header = {"token": self.client.user_token}
        return self.client.post(url=self.url_builder.sbrlive_listLiveState, data=post_data, headers=header)

    def sbrlive_uncompleted(self, liveId, classId, pageIndex, pageSize):
        params = {"liveId":liveId, "classId":classId, "pageIndex":pageIndex, "pageSize":pageSize}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_uncompleted, params=params, headers=header)

    def sbrlive_arrangingClassList(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_arrangingClassList, params=params, headers=header)

    def sbrlive_overview(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_overview, params=params, headers=header)

    def sbrlive_online(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_online, params=params, headers=header)

    def sbrlive_details(self, liveId, classId, pageIndex, pageSize):
        params = {"liveId":liveId, "classId":classId, "pageIndex":pageIndex, "pageSize":pageSize}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_details, params=params, headers=header)

    def sbrlive_getRecordAvgDuration(self, liveId):
        params = {"liveId":liveId}
        header = {"token": self.client.user_token}
        return self.client.get(url=self.url_builder.sbrlive_getRecordAvgDuration, params=params, headers=header)

    def sbrlive_pageQueryRecordDetails(self, liveId, classId, order, pageIndex, pageSize):
        post_data = {"liveId":liveId, "classId":classId, "order":order, "pageIndex":pageIndex, "pageSize":pageSize}
        header = {"token": self.client.user_token}
        return self.client.post(url=self.url_builder.sbrlive_pageQueryRecordDetails, data=post_data, headers=header)