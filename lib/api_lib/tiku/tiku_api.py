from lib.api_lib.tiku.tiku_urls import TikuUrls
from testcases.api_testcases.tiku_testcases import tiku_data


class Tiku:
    def __init__(self, client):
        self.client = client
        self.url_builder = TikuUrls()
    #答题服务
    def post_AnswerReport(self, **kwargs):
        return self.client.post(self.url_builder.PostAnswerReports, data=kwargs)
    def post_QuestionParse(self, **kwargs):
        return self.client.post(self.url_builder.PostQuestionParse, data=kwargs)
    def get_CreateReport(self, **kwargs):
        return self.client.get(self.url_builder.GetCreateReport, params=kwargs)
    def get_AnswerReportDetail(self, **kwargs):
        return self.client.get(self.url_builder.GetAnswerReportDetail, params=kwargs)
    def get_QuestionInfosByIds(self, **kwargs):
        return self.client.get(self.url_builder.GetQuestionInfosByIds, params=kwargs)
    def get_QuestionIdsByPaperId(self, **kwargs):
        return self.client.get(self.url_builder.GetQuestionIdsByPaperId, params=kwargs)
    def get_OrCreateReport(self, **kwargs):
        return self.client.get(self.url_builder.GetOrCreateReport, params=kwargs)
    #题库
    def post_Unioncheck(self, **kwargs):
        headers = {'token': tiku_data.get_login_for_admin()}
        return self.client.post(self.url_builder.PostUnioncheck, data=kwargs,headers=headers)
    #卷库
    def post_getnewpaperinfo(self, **kwargs):
        return self.client.post(self.url_builder.PostPaperinfo, data=kwargs)
    def post_addpaperusecount(self, **kwargs):
        return self.client.post(self.url_builder.PostAddpaperusecount, data=kwargs)
    def post_batchInfo(self, **kwargs):
        return self.client.post(self.url_builder.PostBatchinfo, data=kwargs)
    def get_top(self, **kwargs):
        return self.client.get(self.url_builder.GetTop, params=kwargs)
    def get_childrenChapterByRelativeLevel(self, **kwargs):
        return self.client.get(self.url_builder.GetChapterByRelativeLevel, params=kwargs)
    def get_childrenChapter(self, **kwargs):
        return self.client.get(self.url_builder.GetChildrenChapter, params=kwargs)
    def get_childrenChapterIds(self, **kwargs):
        return self.client.get(self.url_builder.GetChildrenChapterIds, params=kwargs)
    def get_paperTypeSearchParam(self, **kwargs):
        return self.client.get(self.url_builder.GetTypeSearchParam, params=kwargs)
    def post_selectpaper(self, **kwargs):
        return self.client.post(self.url_builder.PostSelectpaper, data=kwargs)
    def get_detail(self, **kwargs):
        return self.client.get(self.url_builder.GetDetail, params=kwargs)
    def post_getbaseinfo(self, **kwargs):
        return self.client.post(self.url_builder.PostGetbaseinfo, data=kwargs)
    def post_getpaperdetailinfo(self, **kwargs):
        return self.client.post(self.url_builder.PostGetpaperdetailinfo, data=kwargs)
    def post_getpaperusecount(self, **kwargs):
        return self.client.post(self.url_builder.PostGetpaperusecount, data=kwargs)
    def post_addpublishedpaperc(self, **kwargs):
        return self.client.post(self.url_builder.PostAddpublishedpaperc, data=kwargs)


