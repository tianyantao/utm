from testcases.api_testcases.b_end_testcases.zzj_testcases_data import *
from testcases.api_testcases.b_end_testcases.case_services import *
from common.unittest_v2 import TestCaseV2
import unittest
from config.config_env import get_env


class SbrLive(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_1_sbrlive_listTeacherLiveRecord(self):
        """
        title: 查询教师端直播的回放列表
        url: /api/netschool/sbrlive/listTeacherLiveRecord
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_listTeacherLiveRecord(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        for i in range(0, len(res['data'])):
            self.assertEqual(str(liveId), res['data'][i]['liveId'])
            self.assertIn("片段%s" % (i + 1), res['data'][i]['recordName'])
            self.assertIsNotNone(res['data'][i]['beginTime'])
            self.assertIsNotNone(res['data'][i]['endTime'])
            self.assertIsNotNone(res['data'][i]['ccLiveId'])
            self.assertIsNotNone(res['data'][i]['ccRecordId'])
            self.assertTrue(res['data'][i]['duration'] > 10)

    def get_liveId(self, teacher_web, status):
        res = teacher_web.sbrlive_pageQueryMyLive(liveStatus=status, pageIndex=1, pageSize=100)
        print(res)
        liveIds = [i['id'] for i in res['data']]
        sorted(liveIds)
        print(liveIds)
        return liveIds[-1]

    def test_p1_1_sbrlive_create(self):
        """
        title: 校长给单个班级创建直播, 编辑直播, 删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        liveId = self.get_liveId(teacher_web, status=0)
        res2 = teacher_web.sbrlive_edit(id=liveId, liveName="直播自动化测试_编辑", roomStyle=1, startTime=startTime + 1000000,
                                        finishTime=finishTime, schoolId=schoolid,
                                        classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res2)
        self.assertEqual("200", res2['code'])
        self.assertTrue(res2['data'])
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_2_sbrlive_create(self):
        """
        title: 年级主任给年级创建直播, 编辑直播, 删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=1, numberOfStudent=12,
                                         gradeClassList=[{"graduationYear": expireyear, "isAll": 1, "classIdList": []}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        time.sleep(10)
        liveId = self.get_liveId(teacher_web, status=0)
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_3_sbrlive_create(self):
        """
        title: 教学班主任给单个教学班班级创建直播,  删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=2, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_jiaoxue)]}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        time.sleep(10)
        liveId = self.get_liveId(teacher_web, status=0)
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_4_sbrlive_create(self):
        """
        title: 行政班主任给单个教学班班级创建直播,  删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        time.sleep(10)
        liveId = self.get_liveId(teacher_web, status=0)
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_5_sbrlive_create(self):
        """
        title: 心理老师给单个班级创建直播, 编辑为年级直播作业, 删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        time.sleep(10)
        liveId = self.get_liveId(teacher_web, status=0)
        res2 = teacher_web.sbrlive_edit(id=liveId, liveName="直播自动化测试_编辑", roomStyle=1, startTime=startTime + 1000000,
                                        finishTime=finishTime, schoolId=schoolid,
                                        classType=1, numberOfStudent=12,
                                        gradeClassList=[{"graduationYear": expireyear, "isAll": 1, "classIdList": []}])
        print(res2)
        self.assertEqual("501", res2['code'])
        self.assertIn("已被布置为班级作业，不能切换为年级作业", res2['msg'])
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_6_sbrlive_create_edit(self):
        """
        title: 混合角色老师给单个教学班班级创建直播, 编辑为年级直播作业, 删除直播
        url: /api/netschool/sbrlive/create,/api/netschool/sbrlive/edit,/api/netschool/sbrlive/delete
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        startTime = CaseServices.get_deadlinetime()
        finishTime = CaseServices.get_deadlinetime() + 3000000
        res = teacher_web.sbrlive_create(liveName="直播自动化测试", roomStyle=1, startTime=startTime, finishTime=finishTime,
                                         schoolId=schoolid,
                                         classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['data'])
        time.sleep(10)
        liveId = self.get_liveId(teacher_web, status=0)
        res2 = teacher_web.sbrlive_edit(id=liveId, liveName="直播自动化测试_编辑", roomStyle=1, startTime=startTime + 1000000,
                                        finishTime=finishTime, schoolId=schoolid,
                                        classType=1, numberOfStudent=12, gradeClassList=[
                {"graduationYear": expireyear, "isAll": 0, "classIdList": [str(groupid_xingzheng)]}])
        print(res2)
        self.assertEqual("200", res2['code'])
        self.assertTrue(res2['data'])
        res3 = teacher_web.sbrlive_delete(liveId=liveId)
        print(res3)
        self.assertEqual("200", res3['code'])
        self.assertTrue(res['data'])

    def test_p1_1_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_校长返回新高一、高一、高二、高三所有年级班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']]
        self.assertIn(len(graduationYears), (3, 4))
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertTrue(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertIsNotNone(j['className'])
                self.assertIn(j['classType'], (1, 2))
                self.assertIsNotNone(j['classId'])
                if j['classId'] == str(groupid_xingzheng):
                    self.assertIsNotNone(j['className'])
                    self.assertTrue(j['numberOfStudent'] > 5)
                    self.assertIn(j['classType'], (1, 2))

    def test_p1_2_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_年级主任返回对应年级的所有年级班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertTrue(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertIsNotNone(j['className'])
                self.assertIn(j['classType'], (1, 2))
                self.assertIsNotNone(j['classId'])
                if j['classId'] == str(groupid_xingzheng):
                    self.assertIsNotNone(j['className'])
                    self.assertTrue(j['numberOfStudent'] > 5)
                    self.assertIn(j['classType'], (1, 2))

    def test_p1_3_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_班主任对应的班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertFalse(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertEqual(1, len(i['classInfoList']))
                if j['classId'] == str(groupid_xingzheng):
                    self.assertIsNotNone(j['className'])
                    self.assertTrue(j['numberOfStudent'] > 5)
                    self.assertIn(j['classType'], (1, 2))

    def test_p1_4_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_接班主任对应的班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertFalse(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertEqual(str(groupid_xingzheng), j['classId'])
                self.assertIsNotNone(j['className'])
                self.assertTrue(j['numberOfStudent'] > 5)
                self.assertIn(j['classType'], (1, 2))

    def test_p1_5_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_接教学班主任对应的班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertFalse(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertEqual(str(groupid_jiaoxue), j['classId'])
                self.assertIsNotNone(j['className'])
                self.assertTrue(j['numberOfStudent'] > 5)
                self.assertIn(j['classType'], (1, 2))

    def test_p1_6_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_任课老师对应的班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(expireyear, res['data'][0]['graduationYear'])
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertFalse(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertEqual(str(groupid_xingzheng), j['classId'])
                self.assertIsNotNone(j['className'])
                self.assertTrue(j['numberOfStudent'] > 5)
                self.assertIn(j['classType'], (1, 2))

    def test_p1_7_sbrlive_listTeacherClasses(self):
        """
        title: 查询教师的班级列表_混合角色(校长、任课老师)返回新高一、高一、高二、高三所有年级班级
        url: /api/netschool/sbrlive/listTeacherClasses
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        res = teacher_web.sbrlive_listTeacherClasses()
        print(res)
        self.assertEqual("200", res['code'])
        graduationYears = [i['graduationYear'] for i in res['data']]
        self.assertIn(len(graduationYears), (3, 4))
        for i in res['data']:
            self.assertIsNotNone(i['gradeName'])
            self.assertTrue(i['isGradeLeader'])
            for j in i['classInfoList']:
                self.assertIsNotNone(j['className'])
                self.assertIn(j['classType'], (1, 2))
                self.assertIsNotNone(j['classId'])
                if j['classId'] == str(groupid_xingzheng):
                    self.assertIsNotNone(j['className'])
                    self.assertTrue(j['numberOfStudent'] > 5)
                    self.assertIn(j['classType'], (1, 2))

    def test_p1_sbrlive_getLiveInfo(self):
        """
        title: 查看直播信息
        url: /api/netschool/sbrlive/getLiveInfo
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_getLiveInfo(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(liveInfo, res['data'])

    def test_p1_1_sbrlive_pageQueryMyLive(self):
        """
        title: 我的直播_根据直播Id查询
        url: /api/netschool/sbrlive/pageQueryMyLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryMyLive(liveId=liveId, liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, res['totalRecords'])
        self.assertEqual(liveInfo['id'], res['data'][0]['id'])
        self.assertEqual(liveInfo['liveName'], res['data'][0]['liveName'])
        self.assertEqual(liveInfo['startTime'], res['data'][0]['startTime'])
        self.assertEqual(liveInfo['finishTime'], res['data'][0]['finishTime'])
        self.assertEqual(str(teacher_web.client.user_id), res['data'][0]['teacherId'])
        self.assertEqual(2, res['data'][0]['liveStatus'])
        self.assertEqual(3, res['data'][0]['liveDetailStatus'])
        self.assertTrue(res['data'][0]['numberOfStudent'] > 5)

    def test_p1_2_sbrlive_pageQueryMyLive(self):
        """
        title: 我的直播_根据直播名称查询
        url: /api/netschool/sbrlive/pageQueryMyLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryMyLive(liveName=liveInfo['liveName'], liveStatus="", pageIndex=1,
                                                  pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] >= 1)
        for i in res['data']:
            self.assertIn(liveInfo['liveName'], res['data'][0]['liveName'])

    def test_p1_3_sbrlive_pageQueryMyLive(self):
        """
        title: 我的直播_时间段筛选直播
        url: /api/netschool/sbrlive/pageQueryMyLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryMyLive(startTime=liveInfo['startTime'], finishTime=liveInfo['finishTime'],
                                                  liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] >= 1)
        for i in res['data']:
            self.assertTrue(liveInfo['startTime'] <= i['startTime'])
            self.assertTrue(i['startTime'] <= liveInfo['finishTime'])

    def test_p1_4_sbrlive_pageQueryMyLive(self):
        """
        title: 我的直播_筛选出已截止的直播
        url: /api/netschool/sbrlive/pageQueryMyLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryMyLive(liveStatus=2, pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] >= 1)
        for i in res['data']:
            self.assertTrue(2, i['liveStatus'])

    def test_p1_5_sbrlive_pageQueryMyLive(self):
        """
        title: 我的直播_混合查询
        url: /api/netschool/sbrlive/pageQueryMyLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryMyLive(liveId=liveId, liveName=liveInfo['liveName'],
                                                  startTime=liveInfo['startTime'],
                                                  finishTime=liveInfo['finishTime'], liveStatus=2, pageIndex=1,
                                                  pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, res['totalRecords'])
        for i in res['data']:
            self.assertTrue(2, i['liveStatus'])
            self.assertIn(liveInfo['liveName'], res['data'][0]['liveName'])

    def test_p1_1_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_无条件查询
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)

    def test_p1_2_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_根据liveId筛选直播
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveId=liveId, liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, res['totalRecords'])
        self.assertEqual(liveInfo['id'], res['data'][0]['id'])
        self.assertEqual(liveInfo['liveName'], res['data'][0]['liveName'])
        self.assertEqual(liveInfo['startTime'], res['data'][0]['startTime'])
        self.assertEqual(liveInfo['finishTime'], res['data'][0]['finishTime'])
        self.assertEqual(str(teacher_web.client.user_id), res['data'][0]['teacherId'])
        self.assertEqual(2, res['data'][0]['liveStatus'])
        self.assertTrue(res['data'][0]['numberOfStudent'] > 5)

    def test_p1_3_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_根据直播名称查询
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveName=liveInfo['liveName'], liveStatus="", pageIndex=1,
                                                      pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] >= 1)
        for i in res['data']:
            self.assertIn(liveInfo['liveName'], res['data'][0]['liveName'])

    def test_p1_4_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_混合查询
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveId=liveId, liveName=liveInfo['liveName'],
                                                      startTime=liveInfo['startTime'],
                                                      finishTime=liveInfo['finishTime'], liveStatus=2, pageIndex=1,
                                                      pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(1, res['totalRecords'])
        for i in res['data']:
            self.assertTrue(2, i['liveStatus'])
            self.assertIn(liveInfo['liveName'], res['data'][0]['liveName'])

    def test_p1_5_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_年级主任显示对应年级的校内直播列表
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=grademaster_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_6_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_班主任显示对应管理班级的直播列表
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=headteacher_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_7_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_心理老师直播列表空
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=psychologicalteacher_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(0, len(res['data']))
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_8_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_教学班主任老师直播列表空
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=classheadteacher_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(0, len(res['data']))
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_9_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_任课老师直播列表空
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(0, len(res['data']))
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_10_sbrlive_pageQuerySchoolLive(self):
        """
        title: 校内直播列表_混合角色显示直播列表
        url: /api/netschool/sbrlive/pageQuerySchoolLive
        author: 章志君
        """
        teacher_web = teacher(web_client(username=teacher_mix_user['username']))
        res = teacher_web.sbrlive_pageQuerySchoolLive(liveStatus="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)
        self.assertEqual(len(res['data']), res['totalRecords'])

    def test_p1_sbrlive_getLiveToken(self):
        """
        title: 获取直播令牌信息（c端）
        url: /api/netschool/sbrlive/getLiveToken
        author: 章志君
        """
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.sbrlive_getLiveToken(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIsNotNone(res['data']['adminUserId'])
        self.assertIsNotNone(res['data']['roomId'])
        self.assertIsNotNone(res['data']['viewerName'])
        self.assertIsNotNone(res['data']['viewerCustomua'])
        self.assertIsNotNone(res['data']['viewerToken'])
        self.assertIn(str(teacher_web.client.user_id), res['data']['viewerToken'])

    def test_p1_sbrlive_getTeacherLiveToken(self):
        """
        title: 获取直播令牌信息（讲师）
        url: /api/netschool/sbrlive/getTeacherLiveToken
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_getTeacherLiveToken(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIsNotNone(res['data']['adminUserId'])
        self.assertIsNotNone(res['data']['roomId'])
        self.assertIsNotNone(res['data']['realName'])
        self.assertIsNotNone(res['data']['publisherPass'])
        teacher_web = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res2 = teacher_web.sbrlive_getLiveToken(liveId=liveId)
        self.assertIsNotNone(res['data']['roomId'], res2['data']['roomId'])

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_listLiveRecord(self):
        """
        title: 查询直播的回放列表
        url: /api/netschool/sbrlive/listLiveRecord
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_listLiveRecord(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertIsNotNone(res['data']['roomId'])
        self.assertTrue(len(res['data']['recordList']) >= 1)

    def test_p1_sbrlive_listLiveState(self):
        """
        title: 根据直播id列表查询直播状态（c端）
        url: /api/netschool/sbrlive/listLiveState
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res2 = teacher_web.sbrlive_pageQueryMyLive(liveStatus="", pageIndex=1, pageSize=100)
        liveIds = [i['id'] for i in res2['data']]
        res = teacher_web.sbrlive_listLiveState(liveIdList=liveIds)
        print(res)
        self.assertEqual("200", res['code'])
        for i in res['data']:
            self.assertIn(i['liveId'], liveIds)
            self.assertIn(i['state'], [0, 1, 2, 3])

    def test_p1_sbrlive_uncompleted(self):
        """
        title: 直播未参与学生
        url: /api/netschool/sbrlive/uncompleted
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_uncompleted(liveId=liveId, classId="", pageIndex=1, pageSize=100)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] > 1)
        self.assertEqual(len(res['data']), res['totalRecords'])
        classIds = [i['classId'] for i in res['data']]
        self.assertIn(str(groupid_xingzheng), classIds)
        for i in res['data']:
            self.assertIsNotNone(i['studentId'])
            self.assertIsNotNone(i['studentName'])

    def test_p1_sbrlive_arrangingClassList(self):
        """
        title: 直播布置到的全部班级
        url: /api/netschool/sbrlive/arrangingClassList
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_arrangingClassList(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        classIds = [i['classId'] for i in res['data']]
        classNames = [i['className'] for i in res['data']]
        res2 = teacher_web.class_listClassesContainDisbanded(classIdList=[groupid_xingzheng])
        print(res2)
        self.assertIn(res2['data'][0]['classId'], classIds)
        self.assertIn(res2['data'][0]['className'], classNames)

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_overview(self):
        """
        title: 直播概况
        url: /api/netschool/sbrlive/statistics/overview
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_overview(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(liveId), res['data']['liveId'])
        self.assertTrue(res['data']['totalCount'] > 5)
        self.assertTrue(res['data']['participateCount'] >= 1)
        self.assertTrue(res['data']['maxConcurrentCount'] >= 1)
        self.assertTrue(res['data']['averageDuration'] >= 100)

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_online(self):
        """
        title: 直播在线人数
        url: /api/netschool/sbrlive/statistics/online
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_online(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertEqual(str(liveId), res['data']['liveId'])
        self.assertTrue(len(res['data']['onlineStatistics']) > 2)
        for i in res['data']['onlineStatistics']:
            self.assertIsNotNone(i['moment'])
            self.assertTrue(i['connectionCount'] >= 1)

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_details(self):
        """
        title: 直播明细
        url: /api/netschool/sbrlive/statistics/details
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        teacher_web2 = teacher(web_client(username=student_user['username'], password=student_user['password']))
        res = teacher_web.sbrlive_details(liveId=liveId, classId=groupid_xingzheng, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(len(res['data']) >= 1)
        self.assertEqual(str(groupid_xingzheng), res['data'][0]['classId'])
        self.assertEqual(str(teacher_web2.client.user_id), res['data'][0]['studentId'])
        self.assertTrue(res['data'][0]['completion'] > 10)
        self.assertTrue(int(res['data'][0]['watchTime']) > 10)
        self.assertTrue(res['data'][0]['enterLeaveCount'] >= 1)
        self.assertTrue(res['data'][0]['chatCount'] >= 1)
        self.assertTrue(res['data'][0]['rollcallCount'] >= 1)

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_getRecordAvgDuration(self):
        """
        title: 获取回放的平均观看时长
        url: /api/netschool/sbrlive/statistics/getRecordAvgDuration
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_getRecordAvgDuration(liveId=liveId)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(int(res['data']['avgDuration']) >= 1)
        self.assertTrue(int(res['data']['unCompleteAvgDuration']) >= 1)

    @unittest.skipIf(get_env() != 'prod', '线下跳过（(仅线上，测试环境没数据-cc只提供了一套环境)）')
    def test_p1_sbrlive_pageQueryRecordDetails(self):
        """
        title: 分页查询回放观看明细
        url: /api/netschool/sbrlive/statistics/pageQueryRecordDetails
        author: 章志君
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.sbrlive_pageQueryRecordDetails(liveId=liveId, classId=0, order=0, pageIndex=1, pageSize=20)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['totalRecords'] > 0)
        self.assertIn(str(groupid_xingzheng), str(res['data']))
        for i in res['data']:
            self.assertIsNotNone(i['userId'])
            self.assertIsNotNone(i['duration'])
            self.assertIsNotNone(i['rate'])
