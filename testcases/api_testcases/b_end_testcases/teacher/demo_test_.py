from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.case_services import *
from common.unittest_v2 import TestCaseV2


class PaperTest(TestCaseV2):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_p1_get_userinfo_principal(self):
        """
        title: 验证校长的userinfo接口
        url: /api/teacher/psychology/userinfo
        author: 田彦涛
        """
        teacher_web = teacher(web_client(username=principal_user['username']))
        res = teacher_web.get_userinfo()
        print(res)