class ResponseCode:
    SUCCESS = 200
    FAIL = 500
    MONITOR = 200001  # 业务监控运行中
    RUNNING = 200002  # 正在跑用例
    REPORT = 200003   # 刚跑完用例生成了报告
    NORUN = 200004  # 系统空闲，没有用例在跑


class ResponseMsg:
    SUCCESS = '成功'
    FAIL = '失败'
    INVALID_PARAMETER = "参数无效"
    MONITOR = '业务监控运行中'
    RUNNING = '当前正在执行用例'
    REPORT = '用例执行完成'
    NORUN = '当前没有运行用例'


class ResMsg(object):
    """
    封装响应文本
    """

    def __init__(self, data=None, code=ResponseCode.SUCCESS, msg=ResponseMsg.SUCCESS):
        self._data = data
        self._msg = msg
        self._code = code

    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应状态码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if code is not None:
            self._code = code
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body

