from config.config_env import get_env
import time


def time_slot():
    pass

rolelistNeedALL = [{'index': -1, 'value': '全部'}, {'index': 1, 'value': '校领导'}, {'index': 2, 'value': '年级主任'},{'index': 5, 'value': '心理老师'}, {'index': 6, 'value': '班主任'}, {'index': 7, 'value': '任课老师'}]
rolelistNotALL = [{'index': 1, 'value': '校领导'}, {'index': 2, 'value': '年级主任'}, {'index': 5, 'value': '心理老师'}, {'index': 6, 'value': '班主任'}, {'index': 7, 'value': '任课老师'}]
subjectlistNeedAll = [{'index': -1, 'value': '全部'}, {'index': 1, 'value': '语文'}, {'index': 2, 'value': '数学'}, {'index': 3, 'value': '英语'}, {'index': 4, 'value': '物理'}, {'index': 5, 'value': '化学'}, {'index': 6, 'value': '生物'}, {'index': 7, 'value': '政治'}, {'index': 8, 'value': '历史'}, {'index': 9, 'value': '地理'}]
subjectlistNotAll = [ {'index': 1, 'value': '语文'}, {'index': 2, 'value': '数学'}, {'index': 3, 'value': '英语'}, {'index': 4, 'value': '物理'}, {'index': 5, 'value': '化学'}, {'index': 6, 'value': '生物'}, {'index': 7, 'value': '政治'}, {'index': 8, 'value': '历史'}, {'index': 9, 'value': '地理'}]
classconfig_add = [{'value': 0, 'description': '不限制'}, {'value': 1, 'description': '禁止注册用户加班'}, {'value': 2, 'description': '禁止学生自主加班'}]
classconfig_name = [{'value': 0, 'description': '允许学生改名'}, {'value': 1, 'description': '禁止学生改名'}]
classconfig_sort = [{'value': 1, 'description': '看课时长从高到低'}, {'value': 2, 'description': '看课时长从低到高'}, {'value': 3, 'description': '学科答题数从高到低'}, {'value': 4, 'description': '学科答题数从低到高'}, {'value': 5, 'description': 'FM收听时长从高到低'}, {'value': 6, 'description': 'FM收听时长从低到高'}, {'value': 7, 'description': '心灵板报阅读数从高到低'}, {'value': 8, 'description': '心灵板报阅读数从低到高'}]
classconfig_subject = [{'value': 1, 'description': '语文'}, {'value': 2, 'description': '数学'}, {'value': 3, 'description': '英语'}, {'value': 4, 'description': '物理'}, {'value': 5, 'description': '化学'}, {'value': 6, 'description': '生物'}, {'value': 7, 'description': '政治'}, {'value': 8, 'description': '历史'}, {'value': 9, 'description': '地理'}]



if get_env() == 'prod':
    cellphone1 = 14100000003 #无职务，用于老师管理-添加老师删除老师
    userIdTest1 = 112421139 #手机号14100000003对应的userId
    cellphone = 14100000004 #校长，密码会变（发送短信case），用于OA编辑老师、发送短信等case
    userIdTest = 112421147  #手机号14100000004对应的userId
    cellphone3 = 14100000006 #非老师
    classIdTest = 1018921 #oa_teacher_test.py 添加老师任课老师时选择班级用
    schoolconf = [{'key': 'SCHOOL_BASED_VIDEO_PERMISSION', 'value': 'true'},
                  {'key': 'LIGHT_WEIGHT_ONLINE_SCHOOL_PERMISSION', 'value': 'true'},
                  {'key': 'SCHOOL_BASED_PAPERS_PERMISSION', 'value': 'true'},
                  {'key': 'COURSE_SCHEDULING_SYSTEM_PERMISSION', 'value': 'true'}]
    classId_xz = 1018920 #2022年毕业的行政班
    classId_jx = 1019592 #校长账号创建的2022年毕业的语文教学班
    teacherNameKeyword = "hh" #用于教师列表搜索用例 oa_teacher_test.py -- test_p1_x_oateacher_listTeacher
    teacherName = "3283500001" #用于教师列表搜索用例（班主任老师名称）
    classNameKeyword = "高一" #用于教师列表搜索用例
    studentIds = [112775971,112775972,112986922,112775979]
    menuNum = [12, 7, 11, 12, 6, 4]  # 校领导、心理老师、行政班主任、年级主任、学科老师、无角色老师账号
    student200_user = {'username': 'autozzj8500005', 'password': '123456'} #未加班学生

else:
    cellphone1 = 14100000001
    userIdTest1 = 100094871 #手机号14100000001对应的userId
    cellphone = 14100000002
    userIdTest = 100094882  #手机号14100000002对应的userId
    classIdTest = 999967
    cellphone3 = 14100000004 #非老师会员
    schoolconf = [{'key': 'SCHOOL_BASED_VIDEO_PERMISSION', 'value': 'true'},
                  {'key': 'LIGHT_WEIGHT_ONLINE_SCHOOL_PERMISSION', 'value': 'false'},
                  {'key': 'SCHOOL_BASED_PAPERS_PERMISSION', 'value': 'true'},
                  {'key': 'COURSE_SCHEDULING_SYSTEM_PERMISSION', 'value': 'false'}]

    classId_xz = 999987 #2022年毕业的行政班
    classId_jx = 1000082 #校长账号创建的2022年毕业的语文教学班
    teacherNameKeyword = "x" #用于教师列表搜索用例 oa_teacher_test.py -- test_p1_x_oateacher_listTeacher
    teacherName = "666" #用于根据班主任姓名搜索班级列表 oa_classes_test
    classNameKeyword = "高二" #用于教师列表搜索用例
    studentIds = [100095094,100095095,100095096,100095097,100095098,100095099,100095100,100095101,
                  100095102,100095103,100095104,100095105,100095106,100095107,100095108,100095109,
                  100095110,100095111,100095112,100095113]
    menuNum = [13, 8, 12, 13, 7, 4]  # 校领导、心理老师、行政班主任、年级主任、学科老师、无角色老师账号
    student200_user = {'username': 'autozzj8500003', 'password': '123456'}  # 未加班学生