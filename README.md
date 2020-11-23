#### 框架说明
用例层采用unittest框架，重写了requests.sessions.Session和unittest.TestCase。web层后端使用flask框架，前端采用vue框架。此框架的特点是用例层与web层相结合，方便线下写用例，线上回归执行。
-  common  
   - helper 常用的公共方法，如字符串加解密等
   - HTMLTestRunner 测试报告生成
   - requests_v2 重写requests.session，加入了每次请求的api日志收集、预发环境手动切换hosts等
   - unittest_v2 重写了unittest.TestCase，加入了每条用例执行的数据上报
   - log_upload 封装了用例执行结果与api调用详情上报的方法

- conf
   - config_case 用例使用到的配置项，比如各业务线的域名、协议名等
   - config_env 环境配置，本地运行时可以手动修改运行环境
   - config_hosts 预发环境hosts配置
   - config_web web层配置项，比如数据库连接字符串、日志收集开关等
- lib
   - api_lib
      - ewt_client 封装了适用于e网通的WebClient和AppClient对象
      - teacher
         - teacher_api 教师端接口定义
         - teacher_urls 教师端url列表
      - tiku
   - web_ui_lib  预留webUI自动化相关的页面和操作封装
- testcases 测试用例根目录，编写用例时创建好对应的业务线和系统目录
   - api_testcases 接口自动化case目录
      - b_end_testcases B端测试用例目录
         - homework_evaluation_test.py 心理测评作业模块的case示例，注意测试用例文件都以*_test.py结尾
         - homework_evaluation_data.py 测试数据文件示例，你可以在测试用例目录创建一些文件来存放某些用例所需的变量以及常量
      - tiku_testcases 中后台题库用例目录
   - ui_testcases 预留页面UI自动化case目录
- services 自动化测试平台后端服务，写case的质量人员可以先忽略
- front 自动化测试平台的前端服务，写case的质量人员可以先忽略

#### 示例

如果想要编写一个新系统的第一条测试用例，以B端作业系统为例，请参考以下步骤：

   - 1. 在/lib目录下更新响应的待测url与api定义，在/lib/api_lib/teacher/teacher_urls.py文件定义url类，示例如下：

```python
from config.config_case import ConfigCase

class TeacherUrls:

    def __init__(self):
        self.__init_urls()

    def __init_urls(self):
        configcase = ConfigCase()
        baseurl = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_TEACHER)
        gateway_url = "{}://{}".format(configcase.PROTOCOL, configcase.HOST_GATEWAY)
        self.homeworkprod_getQuestionProvince = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionProvince'
        self.homeworkprod_pageQueryQuesAtChapterOrPoint = baseurl + '/bendbff/api/homeworkprod/resource/question/pageQueryQuesAtChapterOrPoint'
        self.homeworkprod_getQuestionSubject = baseurl + '/bendbff/api/homeworkprod/resource/question/getQuestionSubject'
```

   - 2. 在/lib/api_lib/study/study_api.py文件定义要测试的api：

```python
from lib.api_lib.teacher.teacher_urls import TeacherUrls

class Teacher:

    def __init__(self, client):
        self.client = client
        self.url_builder = TeacherUrls()

    # 题卷库升级
    def homeworkprod_getQuestionSubject(self, schoolid):
        return self.client.get(url=self.url_builder.homeworkprod_getQuestionSubject, params={"schoolId": schoolid})
```

   - 3. 在/testcases目录下创建case，示例/testcases/api_testcasses/b_end_testcases/homeworkprod/resource_pick_test.py：

```python
from common.unittest_v2 import TestCaseV2
from lib.api_lib.teacher.teacher_api import Teacher as teacher
from lib.api_lib.ewt_client import WebClient as web_client
from testcases.api_testcases.b_end_testcases.schooluser_data import *


class HomeworkprodResourceQuestionTest(TestCaseV2):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_question_subjects_by_principal(self):
        """
        title: 题库挑题-获取学科列表-校长：获取全部学科
        url: /api/homeworkprod/resource/question/getQuestionSubject
        author: 田彦涛
        """
        teacher_web = teacher(web_client(principal_user['username'], principal_user['password']))
        res = teacher_web.homeworkprod_getQuestionSubject(schoolid=schoolid)
        print(res)
        self.assertEqual("200", res['code'])
        self.assertTrue(res['success'])
        self.assertEqual(9, len(res['data']))
```

#### 编写用例注意事项
1. 创建测试用例目录一定要按照业务线、系统划分
2. 每一个测试用例里面都要填写title、url和author以便于对测试结果和执行详情的统计
3. 注意测试用例目录下一定要有``__init__.py``文件
4. 针对同一个测试用例，线上和线下不要写2条，如果线上和线下测试数据不一致，建议走配置，可以在用例所在的目录下创建非_test结尾的py文件专门存放测试数据

#### 用例如何执行
##### 两种方法：
1. pycharm里面直接用unittest运行，适用于调试case阶段
2. 自动化平台提供的页面上面直接运行（下面会提到）  

---

#### 自动化平台
访问入口：http://qa.mistong.cn/pytest/  
本地启动命令：``` python start.py ```  
  
功能说明：
1. case列表展示、搜索
2. 单条/批量case执行
3. 结果报告查看
4. case执行支持选择环境（test、pre、prod）
5. 支持用例分组
6. 支持用例组监控，调整监控频率
7. 开启/关闭监控
8. 查看用例执行结果、监控用例执行结果
9. 查看某次用例执行调用的api详情
10. 支持监控异常钉钉告警
11. 支持不同模块的case配置不同的钉钉告警群（需在代码里配置）



mark:   
./front>npm run build  
.nohup python3.6 run.py
