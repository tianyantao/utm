from common.unittest_v2 import TestCaseV2
import random

from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from lib.api_lib.ewt_client import AppClient as app_client
from testcases.api_testcases.b_end_testcases.case_services import *
from testcases.api_testcases.b_end_testcases.testcases_data import *


class UsingMapsTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass
        # cls.student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        # # cls.student_app = teacher(app_client(username='test0063', password='123456'))
        # cls.student_app = teacher(app_client(username='test0053', password='123456'))

    @classmethod
    def tearDownClass(cls):
        pass


    def test_hp_getclasseswithgradeinfo_by_principal(self):
        """
        title: 校长获取使用地图-学科提分可布置范围
        url: /api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo
        author: 田彦涛
        """
        teacher_principal = teacher(
            web_client(username=principal_user['username'], password=principal_user['password']))
        res = teacher_principal.hp_getclasseswithgradeinfo(actiontype=2, promotionmoduletype=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(4, len(res['data']))
        self.assertEqual(1, res['data'][0]['homeworksetstate'])
        self.assertEqual(current_school_year + 4, res['data'][0]['expireyear'])
        self.assertEqual(current_school_year + 3, res['data'][1]['expireyear'])
        self.assertEqual(current_school_year + 2, res['data'][2]['expireyear'])
        self.assertEqual(current_school_year + 1, res['data'][3]['expireyear'])
        self.assertEqual('新高一({}年入学)'.format(current_school_year + 1), res['data'][0]['name'])
        self.assertEqual('高一({}年入学)'.format(current_school_year), res['data'][1]['name'])
        self.assertEqual('高二({}年入学)'.format(current_school_year - 1), res['data'][2]['name'])
        self.assertEqual('高三({}年入学)'.format(current_school_year - 2), res['data'][3]['name'])
        for i in res['data']:
            if i['expireyear'] == expireyear:
                self.assertIn(groupid_xingzheng, [x['classid'] for x in i['classlist']])
                self.assertNotIn(groupid_jiaoxue, [x['classid'] for x in i['classlist']])
                self.assertNotIn(groupid_isdeleted, [x['classid'] for x in i['classlist']])
                for j in i['classlist']:
                    if j['classid'] == groupid_xingzheng:
                        self.assertEqual(1, j['type'])
                        self.assertTrue(j['members'] > 0)

    def test_hp_getclasseswithgradeinfo_by_grademaster(self):
        """
        title: 年级主任获取使用地图-学科提分可布置范围
        url: /api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo
        author: 田彦涛
        """
        teacher_principal = teacher(
            web_client(username=grademaster_user['username'], password=grademaster_user['password']))
        res = teacher_principal.hp_getclasseswithgradeinfo(actiontype=2, promotionmoduletype=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(1, len(res['data']))
        self.assertEqual(1, res['data'][0]['homeworksetstate'])
        self.assertEqual(expireyear, res['data'][0]['expireyear'])
        for i in res['data']:
            if i['expireyear'] == expireyear:
                self.assertIn(groupid_xingzheng, [x['classid'] for x in i['classlist']])
                self.assertNotIn(groupid_jiaoxue, [x['classid'] for x in i['classlist']])
                self.assertNotIn(groupid_isdeleted, [x['classid'] for x in i['classlist']])
                for j in i['classlist']:
                    if j['classid'] == groupid_xingzheng:
                        self.assertEqual(1, j['type'])
                        self.assertTrue(j['members'] > 0)

    def test_hp_getclasseswithgradeinfo_by_headteacher(self):
        """
        title: 行政班班主任获取使用地图-学科提分可布置范围
        url: /api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo
        author: 田彦涛
        """
        teacher_principal = teacher(
            web_client(username=headteacher_user['username'], password=headteacher_user['password']))
        res = teacher_principal.hp_getclasseswithgradeinfo(actiontype=2, promotionmoduletype=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(1, len(res['data']))
        self.assertEqual(1, res['data'][0]['homeworksetstate'])
        self.assertEqual(expireyear, res['data'][0]['expireyear'])
        self.assertEqual(groupid_xingzheng, res['data'][0]['classlist'][0]['classid'])
        self.assertTrue(res['data'][0]['classlist'][0]['members'] > 0)

    def test_hp_getclasseswithgradeinfo_by_teacher(self):
        """
        title: 任课老师获取使用地图-学科提分可布置范围（无权限）
        url: /api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo
        author: 田彦涛
        """
        teacher_principal = teacher(
            web_client(username=teacher_user['username'], password=teacher_user['password']))
        res = teacher_principal.hp_getclasseswithgradeinfo(actiontype=2, promotionmoduletype=1)
        print(res)
        self.assertEqual(131, res['code'])

    def test_hp_getclasseswithgradeinfo_by_classheadteacher(self):
        """
        title: 教学班班主任获取使用地图-学科提分可布置范围（无权限）
        url: /api/services/homeworkpromotion/homeworkpromotion/getclasseswithgradeinfo
        author: 田彦涛
        """
        teacher_principal = teacher(
            web_client(username=classheadteacher_user['username'], password=classheadteacher_user['password']))
        res = teacher_principal.hp_getclasseswithgradeinfo(actiontype=2, promotionmoduletype=1)
        print(res)
        self.assertEqual(131, res['code'])



    def test_p3_get_grades_by_principal(self):
        """
        title: 校长获取使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        except_data = [
            {'text': '高一({}年入学)'.format(current_school_year), 'value': 1, 'checked': False},
            {'text': '高二({}年入学)'.format(current_school_year-1), 'value': 2, 'checked': False},
            {'text': '高三({}年入学)'.format(current_school_year-2), 'value': 3, 'checked': False}
        ]
        self.assertEqual(except_data, res['data'])

    def test_p3_get_grades_by_grademaster(self):
        """
        title: 年级主任获取使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        except_data = [
            {'text': '{0}({1}年入学)'.format(gradename, expireyear-3), 'value': grade, 'checked': False}
        ]
        self.assertEqual(except_data, res['data'])

    def test_p3_get_grades_by_headteacher(self):
        """
        title: 行政班班主任获取使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        except_data = [
            {'text': '{0}({1}年入学)'.format(gradename, expireyear-3), 'value': grade, 'checked': False}
        ]
        self.assertEqual(except_data, res['data'])

    def test_p3_get_grades_by_psychologicalteacher(self):
        """
        title: 心理老师获取使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        except_data = [
            {'text': '高一({}年入学)'.format(current_school_year), 'value': 1, 'checked': False},
            {'text': '高二({}年入学)'.format(current_school_year-1), 'value': 2, 'checked': False},
            {'text': '高三({}年入学)'.format(current_school_year-2), 'value': 3, 'checked': False}
        ]
        self.assertEqual(except_data, res['data'])

    def test_p3_get_grades_by_teacher(self):
        """
        title: 学科老师获取使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        # except_data = [
        #     {'text': '{0}({1}年入学)'.format(gradename, expireyear - 3), 'value': grade, 'checked': False}
        # ]
        self.assertEqual([], res['data'])

    def test_p3_get_grades_by_classheadteacher(self):
        """
        title: 教学班班主任无法看到使用地图可选年级列表
        url: /api/services/homeworkpromotion/homeworkpromotion/grades
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.hp_grades()
        print(res)
        except_data = []
        self.assertEqual(except_data, res['data'])

    def test_p3_get_GetTimeAxis(self):
        """
        title: 获取使用地图时间轴上的主题列表
        url: /api/services/homeworkpromotion/homeworkpromotion/GetTimeAxis
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.hp_GetTimeAxis(grade=1)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']) > 0)

    def test_p3_get_ThemeMapData_principal(self):
        """
        title: 校长能看到使用地图所有标签
        url: /api/services/homeworkpromotion/homeworkpromotion/ThemeMapData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.hp_ThemeMapData(grade=1, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(except_modules_length, len(res['data']['modules']))

    def test_p3_get_ThemeMapData_psychologicalteacher(self):
        """
        title: 心理老师不能看到学科提分、生涯规划、模拟选课的地图模块
        url: /api/services/homeworkpromotion/homeworkpromotion/ThemeMapData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.hp_ThemeMapData(grade=1, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        modules = [i['modulename'] for i in res['data']['modules']]
        self.assertNotIn('学科提分', modules)
        self.assertNotIn('生涯规划', modules)
        self.assertNotIn('模拟选课', modules)

    def test_p3_get_ThemeMapData_grademaster(self):
        """
        title: 年级主任能看到使用地图所有标签
        url: /api/services/homeworkpromotion/homeworkpromotion/ThemeMapData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.hp_ThemeMapData(grade=grade, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertEqual(except_modules_length, len(res['data']['modules']))

    def test_p3_get_ThemeMapData_headteacher(self):
        """
        title: 行政班班主任不能看到模拟选课
        url: /api/services/homeworkpromotion/homeworkpromotion/ThemeMapData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.hp_ThemeMapData(grade=grade, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        modules = [i['modulename'] for i in res['data']['modules']]
        self.assertNotIn('模拟选课', modules)

    def test_p3_get_ThemeMapData_teacher(self):
        """
        title: 学科老师不能看到生涯规划、心灵成长、模拟选课
        url: /api/services/homeworkpromotion/homeworkpromotion/ThemeMapData
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.hp_ThemeMapData(grade=grade, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        modules = [i['modulename'] for i in res['data']['modules']]
        self.assertNotIn('生涯规划', modules)
        self.assertNotIn('心灵成长', modules)
        self.assertNotIn('模拟选课', modules)

    def test_p3_get_themerecord_principal(self):
        """
        title: 校长获取使用地图布置记录
        url: /api/services/homeworkpromotion/homeworkpromotion/themerecord
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.hp_themerecord(moduleid=promotion_moduleid_xueke, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['homeworkrecords']) > 0)
        self.assertTrue(res['data']['homeworkrecords'][0]['homeworkname'])
        self.assertTrue(res['data']['homeworkrecords'][0]['homeworktype'])

    def test_p3_get_themehomeworkdetail_principal(self):
        """
        title: 查看专题详情_提分标签下の视频内容
        url: /api/services/homeworkpromotion/homeworkpromotion/themehomeworkdetail
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.hp_themehomeworkdetail(moduleid=promotion_moduleid_xueke, themeid=promotion_themeid)
        print(res)
        self.assertEqual(200, res['code'])
        self.assertTrue(len(res['data']['videohomework']['videos']) > 0)
        self.assertTrue(res['data']['videohomework']['totalduration'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['duration'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['id'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['kemu'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['kemuid'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['name'])
        self.assertTrue(res['data']['videohomework']['videos'][0]['previewurl'])

    def test_p1_setxuekevideohomework_headteacher(self):
        """
        title: 使用地图班主任布置到班级_提分の视频内容，学生查看作业列表是否收到
        url: /api/services/homeworkpromotion/homeworkpromotion/setxuekehomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.hp_themehomeworkdetail(moduleid=promotion_moduleid_xueke, themeid=promotion_themeid)
        videoid = res['data']['videohomework']['videos'][0]['id']
        videokemuid = res['data']['videohomework']['videos'][0]['kemuid']
        homeworktitle = 'test{}'.format(random.randint(100000, 999999))
        res = teacher_web.hp_setxuekevideohomework(isgradehomework=False, gradeyear=expireyear,
                                                   classlist=[groupid_xingzheng], videohomeworktitle=homeworktitle,
                                                   videoid=videoid, kemuid=videokemuid, deadline=CaseServices.get_deadlinetime(),
                                                   themeid=promotion_themeid, moduleid=promotion_moduleid_xueke)
        print(res)
        self.assertEqual(200, res['code'])
        time.sleep(40)
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=1, pagesize=100)
        print(res)
        homeworktitles = [i['title'] for i in res['data']['list']]
        self.assertIn(homeworktitle, homeworktitles)

    def test_p1_setxuekevideohomework_principal(self):
        """
        title: 使用地图校长布置到年级_提分の视频内容，学生查看作业列表是否收到
        url: /api/services/homeworkpromotion/homeworkpromotion/setxuekehomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_getgradeandclassinfo()
        classlist = []
        for data in res['data']:
            if data['grade'] == grade:
                for classdetail in data['classlist']:
                    classlist.append(classdetail['classid'])
        res = teacher_web.hp_themehomeworkdetail(moduleid=promotion_moduleid_xueke, themeid=promotion_themeid)
        videoid = res['data']['videohomework']['videos'][0]['id']
        videokemuid = res['data']['videohomework']['videos'][0]['kemuid']
        homeworktitle = 'test{}'.format(random.randint(100000, 999999))
        res = teacher_web.hp_setxuekevideohomework(isgradehomework=True, gradeyear=expireyear,
                                                   classlist=classlist, videohomeworktitle=homeworktitle,
                                                   videoid=videoid, kemuid=videokemuid,
                                                   themeid=promotion_themeid, moduleid=promotion_moduleid_xueke)
        print(res)
        self.assertEqual(200, res['code'])
        time.sleep(40)
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=1, pagesize=100)
        homeworktitles = [i['title'] for i in res['data']['list']]
        self.assertIn(homeworktitle, homeworktitles)

    def test_p1_setshengyavideohomework_principal(self):
        """
        title: 使用地图校长布置到年级_生涯の视频内容，学生查看作业列表是否收到
        url: /api/services/homeworkpromotion/homeworkpromotion/setxuekehomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_getgradeandclassinfo()
        classlist = []
        for data in res['data']:
            if data['grade'] == grade:
                for classdetail in data['classlist']:
                    classlist.append(classdetail['classid'])
        res = teacher_web.hp_themehomeworkdetail(moduleid=promotion_moduleid_shengya, themeid=promotion_themeid)
        videoid = res['data']['videohomework']['videos'][0]['id']
        videokemuid = res['data']['videohomework']['videos'][0]['kemuid']
        homeworktitle = 'test{}'.format(random.randint(100000, 999999))
        res = teacher_web.hp_setshengyavideohomework(isgradehomework=True, gradeyear=expireyear,
                                                     classlist=classlist, videohomeworktitle=homeworktitle,
                                                     videoid=videoid, kemuid=videokemuid,
                                                     themeid=promotion_themeid, moduleid=promotion_moduleid_shengya)
        print(res)
        self.assertEqual(200, res['code'])
        time.sleep(30)
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=1, pagesize=100)
        homeworktitles = [i['title'] for i in res['data']['list']]
        self.assertIn(homeworktitle, homeworktitles)

    def test_p1_setshengyavideohomework_principal_appversion(self):
        """
        title: 使用地图校长布置到年级_生涯の视频内容，学生7.5.0以上查看作业列表是否收到
        url: /api/services/homeworkpromotion/homeworkpromotion/setxuekehomework
        author: 吴丽燕
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.career_getgradeandclassinfo()
        classlist = []
        for data in res['data']:
            if data['grade'] == grade:
                for classdetail in data['classlist']:
                    classlist.append(classdetail['classid'])
        res = teacher_web.hp_themehomeworkdetail(moduleid=promotion_moduleid_shengya, themeid=promotion_themeid)
        videoid = res['data']['videohomework']['videos'][0]['id']
        videokemuid = res['data']['videohomework']['videos'][0]['kemuid']
        homeworktitle = 'test{}'.format(random.randint(100000, 999999))
        res = teacher_web.hp_setshengyavideohomework(isgradehomework=True, gradeyear=expireyear,
                                                     classlist=classlist, videohomeworktitle=homeworktitle,
                                                     videoid=videoid, kemuid=videokemuid,
                                                     themeid=promotion_themeid, moduleid=promotion_moduleid_shengya)
        print(res)
        self.assertEqual(200, res['code'])
        time.sleep(30)
        student_app = teacher(app_client(username=student_user['username'], password=student_user['password']))
        res = student_app.get_app_myhomework(status=1, pagesize=100)
        homeworktitles = [i['title'] for i in res['data']['list']]
        self.assertIn(homeworktitle, homeworktitles)

    # def test__(self):
    #     res2 = self.student_app.get_app_myhomework(status=2, pagesize=100, version="7.6.1", page=1)
    #     res1 = self.student_app.get_app_myhomework(status=2, pagesize=100, version="6.8.1", page=1)
    #     a = res1['data']['list']
    #
    #     b = res2['data']['list']
    #     res1_homeworklist = sorted([i['homeworkid'] for i in a])
    #     res2_homeworklist = sorted([i['homeworkid'] for i in b])
    #     print(res1_homeworklist)
    #     print(res2_homeworklist)
    #
    #     for i in a:
    #         for j in b:
    #             if i['homeworkid'] == j['homeworkid']:
    #                 differ = []
    #                 for k in i:
    #                     if k != 'idwithnomeaning' and k != 'image' and k != 'teacherid' and k != 'istop':
    #                         if i[k] != j[k]:
    #                             differ.append("{0}, 新逻辑:{1}, 老逻辑:{2}".format(k, i[k], j[k]))
    #                 if differ != []:
    #                     print("对比 {0}: {1}".format(i['homeworkid'], differ))

