from config.config_case import ConfigCase


class TikuUrls:

    def __init__(self):
        self.__init_urls()

    def __init_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TIKU)
        baseurl_qbank = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_QBANK)
        #卷库接口
        self.PostPaperinfo = baseurl+'/api/paperservice/client/paper/info/getnewpaperinfo'
        self.PostAddpaperusecount = baseurl+'/api/paperservice/client/paper/info/addpaperusecount'
        self.PostBatchinfo = baseurl+'/api/paperservice/paper/chapter/batchInfo'
        self.GetTop = baseurl + '/api/paperservice/paper/chapter/top'
        self.GetChapterByRelativeLevel = baseurl + '/api/paperservice/paper/chapter/childrenChapterByRelativeLevel'
        self.GetChildrenChapter = baseurl + '/api/paperservice/paper/chapter/childrenChapter'
        self.GetChildrenChapterIds = baseurl + '/api/paperservice/paper/chapter/childrenChapterIds'
        self.GetTypeSearchParam = baseurl + '/api/paperservice/paper/chapter/paperTypeSearchParam'
        self.PostSelectpaper = baseurl + '/api/paperservice/client/paper/info/selectpaper'
        self.GetDetail = baseurl + '/api/paperservice/admin/paper/type/detail'
        self.PostGetbaseinfo = baseurl + '/api/paperservice/client/paper/info/getbaseinfo'
        self.PostGetpaperdetailinfo = baseurl + '/api/paperservice/client/paper/info/getpaperdetailinfo'
        self.PostGetpaperusecount = baseurl + '/api/paperservice/client/paper/info/getpaperusecount'
        self.PostAddpublishedpaperc = baseurl + '/api/paperservice/client/paper/info/addpublishedpaperc'
        #题库接口
        self.PostUnioncheck = baseurl_qbank + '/api/qbank/uniform/question/info'
        #答题服务接口
        self.GetOrCreateReport = baseurl + '/api/answerservice/answer/getOrCreateReport'
        self.GetQuestionIdsByPaperId = baseurl + '/api/answerservice/answer/getQuestionIdsByPaperId/'
        self.GetQuestionInfosByIds = baseurl + '/api/answerservice/answer/getQuestionInfosByIds'
        self.GetAnswerReportDetail = baseurl + '/api/answerservice/answer/getAnswerReportDetail'
        self.GetCreateReport = baseurl + '/api/answerservice/answer/createReport'
        self.PostQuestionParse = baseurl + '/api/answerservice/answer/getQuestionParse'
        self.PostAnswerReports = baseurl + '/api/answerservice/answer/queryAnswerReports'


if __name__ == '__main__':
    result = TikuUrls()
    print(result)