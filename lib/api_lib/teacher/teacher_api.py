from lib.api_lib.teacher.teacher_urls import TeacherUrls
from lib.api_lib.teacher.teacher_tyt_api import TeacherTyt
from lib.api_lib.teacher.teacher_wly_api import TeacherWly
from lib.api_lib.teacher.teacher_zzj_api import TeacherZzj
from lib.api_lib.teacher.teacher_zsq_api import TeacherZsq


class Teacher(TeacherTyt, TeacherWly, TeacherZzj, TeacherZsq):

    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()
        super().__init__(client)
