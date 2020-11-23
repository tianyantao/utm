from config.config_env import get_env


ENV = get_env()

oa_uid = 412
expireyear = 2020
grade = 3
schoolid = 25729
current_school_year = 2020
# 校长账号
principal_user = {'username': '13800000004', 'password': '123456'}
new_senior_user = {'username': '13800000089', 'password': '123456'}
# 心理老师账号
psychologicalteacher_user = {'username': '13800000011', 'password': '123456'}
# 行政班班主任账号
headteacher_user = {'username': '13111111113', 'password': '123456'}
# 年级主任账号
grademaster_user = {'username': '13111111112', 'password': '123456'}
# g1年级主任账号
grademaster_user_of_g1 = {'username': '13111111111', 'password': '123456'}
# 学科老师账号
teacher_user = {'username': '13800000001', 'password': '123456'}
# 无角色老师账号
normalteacher_user = {'username': '13800000007', 'password': '123456'}
# 教学班班主任账号
classheadteacher_user = {'username': '13800000066', 'password': '123456'}
# 混合角色老师账号（既担任校领导，又担任多个老师角色）
teacher_mix_user = {'username': '13800000999', 'password': '123456'}
# 行政班班级id（行政班班主任所管理的班级）
groupid_xingzheng = 543529
# 教学班班级id
groupid_jiaoxue = 331268
# 已解散的班级
groupid_isdeleted = 865882
# 学生账号01：非注册会员，且存在于上述两个测试班级
student_user = {'username': 'xms100041', 'password': '123456'}
# 学生账号02：注册会员，且存在于上述两个测试班级
student02_user = {'username': 'testauto002', 'password': '123456'}
# 学生账号03：注册会员，且存在于上述两个测试班级
student03_user = {'username': 'testauto003', 'password': '123456'}
# 学生账号04：注册会员，且存在于上述两个测试班级
student04_user = {'username': 'testauto004', 'password': '123456'}
# 学生账号05：注册会员，且存在于上述两个测试班级
student05_user = {'username': 'testauto005', 'password': '123456'}
student06_user = {'username': 'testauto006', 'password': '123456'}
student07_user = {'username': 'testauto007', 'password': '123456'}
student08_user = {'username': 'testauto008', 'password': '123456'}
student09_user = {'username': 'testauto009', 'password': '123456'}
student10_user = {'username': 'testauto010', 'password': '123456'}
student11_user = {'username': 'testauto011', 'password': '123456'}
# 学生不存在于班级
student00_user = {'username': 'student00', 'password': 'student@00'}
student200_user = {'username': 'autozzj8500003', 'password': '123456'}  # 加过学校班级
# 新高一学生账号
new_course_student = {'username': 'zsqtestnew', 'password': '123456'}
old_course_student = {'username': 'zsqtestold', 'password': '123456'}
novip_student = {'username': 'zsqtest01', 'password': '123456'}
# url_teacher = 'http://teacher.{}.mistong.com'.format(env)
# 过期的年级主任账号:
expired_grademaster_user = {'username': 13800000059, 'password': '123456'}
# 既担任班主任，又担任过期的年级主任账号：
headteacher_and_expired_grademaster_user = {'username': 15858581110, 'password': '123456'}
# 既担任班主任又担任其他班级学科老师的账号:
headteacher_and_teacher_user = {'username': 13800000002, 'password': '123456'}
# 既担任班主任又担任年级主任的账号:
headteacher_and_grademaster_user = {'username': 13800000057, 'password': '123456'}


if ENV == 'prod':
    oa_uid = 1042
    expireyear = 2022
    grade = 2
    schoolid = 32835
    # 校长账号
    principal_user = {'username': '13283590099', 'password': '123456'}
    new_senior_user = {'username': '13283500089', 'password': '123456'}
    # 心理老师账号
    psychologicalteacher_user = {'username': '13283590098', 'password': '123456'}
    # 行政班班主任账号
    headteacher_user = {'username': '13283500001', 'password': '123456'}
    # 年级主任账号（高一）
    grademaster_user = {'username': '13283500000', 'password': '123456'}
    # 学科老师账号
    teacher_user = {'username': '13283590097', 'password': '123456'}
    # 无角色老师账号
    normalteacher_user = {'username': '13283500002', 'password': '123456'}
    # 教学班班主任账号
    classheadteacher_user = {'username': '13283500096', 'password': '123456'}
    # 混合角色老师账号（既担任校领导，又担任多个老师角色）
    teacher_mix_user = {'username': '13283500095', 'password': '123456'}
    # 无职务，用于老师管理-添加老师删除老师
    cellphone1 = 14100000003
    # 校长，密码会变（发送短信case），用于OA编辑老师、发送短信等case
    cellphone = 14100000004
    # 非老师
    cellphone3 = 14100000006


    # 行政班班级id（行政班班主任所管理的班级）
    groupid_xingzheng = 836256
    group_name_xingzheng = '高二（1）班'
    # 教学班班级id
    groupid_jiaoxue = 1013267
    group_name_jiaoxue = '语文教学（1）班'
    # 已解散的班级
    groupid_isdeleted = 1013268
    # 学生账号01：非注册会员，且存在于上述两个测试班级
    student_user = {'username': 'testtyta100001', 'password': '123456'}
    # 学生账号02：注册会员，且存在于上述两个测试班级
    student02_user = {'username': 'testtyta100002', 'password': '123456'}
    # 学生账号03：注册会员，且存在于上述两个测试班级
    student03_user = {'username': 'testtyta100003', 'password': '123456'}
    # 学生账号04：注册会员，且存在于上述两个测试班级
    student04_user = {'username': 'testtyta100004', 'password': '123456'}
    student05_user = {'username': 'testtyta100005', 'password': '123456'}
    student06_user = {'username': 'testtyta100006', 'password': '123456'}
    student07_user = {'username': 'testtyta100007', 'password': '123456'}
    student08_user = {'username': 'testtyta100008', 'password': '123456'}
    student09_user = {'username': 'testtyta100009', 'password': '123456'}
    student10_user = {'username': 'testtyta100010', 'password': '123456'}
    # 学生不存在于班级
    student00_user = {'username': 'student00', 'password': 'student@00'}  # 未加过学校班级
    student200_user = {'username': 'autozzj8500005', 'password': '123456'}  # 加过学校班级
    # 新高一学生账号
    new_course_student = {'username': 'zsqonlinenew', 'password': '123456'}
    old_course_student = {'username': 'zsqonlineold', 'password': '123456'}
    novip_student = {'username': 'zsqonline01', 'password': '123456'}
    # url_teacher = 'http://teacher.ewt360.com'
teacher_user_list = {}
teacher_user_list['principal_user'] = principal_user
teacher_user_list['psychologicalteacher_user'] = psychologicalteacher_user
teacher_user_list['headteacher_user'] = headteacher_user
teacher_user_list['grademaster_user'] = grademaster_user
teacher_user_list['teacher_user'] = teacher_user
teacher_user_list['classheadteacher_user'] = classheadteacher_user
gradename = '高一'
if expireyear - current_school_year == 1:
    gradename = '高三'
elif expireyear - current_school_year == 2:
    gradename = '高二'