from app import *
from flask_restful import Resource
from services.db_services import db_services
from services.response import *
from flask import request, jsonify, render_template
from threading import Thread
import time
import logging
import unittest
import os
from common import HTMLTestRunner
from config import config_env, config_web
from common.helper import ding


def app_run(host, port, debug):
    app.run(debug=debug, port=port, host=host)


def get_status_by_report_id(report_id=0):
    res = {
        "status": None,  # 1表示正在运行，0表示空闲, 2表示在排队
        "run_type": None,  # 0表示监控运行，1表示非监控的运行
        "progress": None,  # 执行进度，run_type=1会返回进度，范围0~100，保留2位小数
        "report_url": None,  # 报告地址，run_type=1且progress=100时会返回报告地址
        "total": None,  # 执行的用例总数，run_type=1且progress=100时会用
        "assert_fail": None,  # 断言失败用例个数，run_type=1且progress=100时会用
        "run_error": None,  # 执行报错用例个数，run_type=1且progress=100时会用
        "success": None,  # 跑成功的用例个数，run_type=1且progress=100时会用
        "skiped": None,  # 跳过的用例个数，run_type=1且progress=100时会用
        "result": None  # 'P'表示测试通过，'F'表示测试结果未通过，run_type=1且progress=100时会用
    }
    if report_id:
        # 返回跑用例的状态
        report_detail = db_services.query_report_detail_by_id(report_id)
        if not report_detail:
            return res
        res['run_type'] = 1
        if not report_detail.status:
            with app.app_context():
                if hasattr(app, "report_id") and int(report_id) == app.report_id:
                    res['progress'] = round(app.count / app.count_all * 100, 2)
                    res['status'] = 1
                else:
                    res['progress'] = 0
                    res['status'] = 2
        else:
            res['result'] = report_detail.status
            res['status'] = 0
            res['report_url'] = report_detail.report_url
            res['total'] = report_detail.total
            res['assert_fail'] = report_detail.assert_fail
            res['run_error'] = report_detail.run_error
            res['success'] = report_detail.success
            res['skiped'] = report_detail.skiped
            res['progress'] = 100
    else:
        # 返回监控的状态
        res['run_type'] = 0
        with app.app_context():
            if hasattr(app, 'monitor'):
                res['status'] = 1
            else:
                res['status'] = 0
    return res


def run_cases(report_id, case_list=None, suite=None, env='prod'):  # 运行case
    with app.app_context():
        app.report_id = report_id

        if case_list and not suite:
            case_names = db_services.get_name_from_ids(case_list)

        if int(report_id):
            # 跑用例，保留报告，跑完后要写入report表
            app.run_env = env
            if app.run_env == 'pre':  # 支持预发环境跑用例，手动指定hosts
                app.pre = 1
                app.run_env = 'prod'
            if suite == 'b':
                suite = unittest.defaultTestLoader.discover(start_dir="./testcases/api_testcases/b_end_testcases",
                                                            pattern="*_test.py", top_level_dir="./testcases")
            elif suite == 'tiku':
                suite = unittest.defaultTestLoader.discover(start_dir="./testcases/api_testcases/tiku_testcases",
                                                            pattern="*_test.py", top_level_dir="./testcases")
            elif suite == 'all':
                suite = unittest.defaultTestLoader.discover(start_dir="./testcases", pattern="*_test.py")
            elif case_list and not suite:
                unittest.defaultTestLoader.discover(start_dir="./testcases", pattern="*_test.py")
                suite = unittest.defaultTestLoader.loadTestsFromNames(names=case_names)

            app.count_all = suite.countTestCases()
            REPORT_FOLDER = '{}/report'.format(config_web.ConfigWeb.FRONT_FOLDER)
            if not os.path.exists(REPORT_FOLDER):
                os.mkdir(REPORT_FOLDER)

            output = 'auto_test_report_' + time.strftime('%Y-%m-%d_%H-%M-%S_{}.html').format(env)
            if not output.endswith('.html'):
                output = output + '.html'
            report_file = os.path.join(REPORT_FOLDER, output)

            with open(report_file, 'wb') as fp:
                runner = HTMLTestRunner.HTMLTestRunner(fp, title='auto test report ({}环境)'.format(env))
                result = runner.run(suite)
            try:
                if hasattr(app, 'pre'):
                    del app.pre
                db_services.update_report(total=suite.countTestCases(), assert_fail=result.failure_count,
                                          run_error=result.error_count,
                                          skiped=suite.countTestCases() - result.success_count - result.failure_count - result.error_count,
                                          success=result.success_count,
                                          report_url='/report/{}'.format(output),
                                          status='P' if result.failure_count == 0 and result.error_count == 0 else 'F',
                                          id=report_id)
            except Exception as e:
                print(e)


        else:
            # 跑监控，不保留报告，跑完后要有钉钉提醒
            app.run_env = env
            unittest.defaultTestLoader.discover(start_dir="./testcases", pattern="*_test.py")
            suite = unittest.defaultTestLoader.loadTestsFromNames(names=case_names)
            REPORT_FOLDER = '{}/report'.format(config_web.ConfigWeb.FRONT_FOLDER)
            if not os.path.exists(REPORT_FOLDER):
                os.mkdir(REPORT_FOLDER)
            output = 'auto_test_report_' + time.strftime('%Y-%m-%d_%H-%M-%S_{}.html').format(env)
            if not output.endswith('.html'):
                output = output + '.html'
            report_file = os.path.join(REPORT_FOLDER, output)

            with open(report_file, 'wb') as fp:
                runner = HTMLTestRunner.HTMLTestRunner(fp, title='auto test report ({}环境)'.format(env))
                app.monitor_run = 1
                runner.run(suite)
            try:
                os.remove(report_file)
                del app.monitor_run
            except Exception as e:
                print(e)


def add_to_run_list(report_id, case_list=None, suite=None, env='prod'):  # 跑用例或跑监控时调用这个方法，往app.run_list里面添加要运行的内容
    run_data = {}
    with app.app_context():
        run_data['report_id'] = report_id
        run_data['case_list'] = case_list
        run_data['suite'] = suite
        run_data['env'] = env
        app.run_list.append(run_data)


def start_run_list():  # app启动时就调用这个方法，开启一个任务，循环运行app.run_list里面的case或suite
    with app.app_context():
        if not hasattr(app, 'start_run_list'):
            app.start_run_list = True
            logging.info("start run list")
            while True:
                if len(app.run_list) > 0:
                    for i in app.run_list:
                        run_cases(report_id=i['report_id'], case_list=i['case_list'], suite=i['suite'], env=i['env'])
                        app.run_list.remove(i)
                else:
                    time.sleep(1)


@app.before_first_request
def thread_start():
    app.run_env = 'prod'
    app.run_list = []
    app.api_records = []
    app.msgs = []
    thread_run = Thread(target=start_run_list, args=())
    thread_run.start()
    app.msgs = []


class CaseList(Resource):

    def get(self):
        res = ResMsg()
        try:
            data = {}
            caselist = db_services.get_all_cases()
            data['caselist'] = caselist
            data['count'] = len(caselist)
            res.update(data=data)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class GetEnv(Resource):
    def get(self):
        res = ResMsg()
        try:
            data = config_env.get_env()
            res.update(data=data)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class SetEnv(Resource):
    def get(self):
        res = ResMsg()
        try:
            with app.app_context():
                env = request.args.get("env")
                app.run_env = env
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class RunMonitor(Resource):

    def get(self):
        with app.app_context():
            cases_all = db_services.get_all_monitor_cases()
            thread_list = []
            res = ResMsg()
            start = 0
            if request.args.get('start'):
                start = int(request.args.get('start'))
            if start:
                if hasattr(app, 'monitor'):
                    res.update(code=ResponseCode.MONITOR, msg=ResponseMsg.MONITOR)
                else:
                    try:
                        app.monitor = 1
                        logging.info('获取到的监控组：{}'.format(cases_all))
                        for i in cases_all:
                            if len(cases_all[i]) > 0:
                                thread_list.append(
                                    Thread(target=self.add_to_monitor,
                                           args=(cases_all[i], i / len(cases_all[i]),)))
                        thread_msg = Thread(target=self.send_msg, args=())
                        thread_list.append(thread_msg)
                        for i in thread_list:
                            i.start()
                        res.update(code=ResponseCode.SUCCESS, msg=ResponseMsg.SUCCESS)
                    except Exception as e:
                        res.update(code=ResponseCode.FAIL, msg=str(e))
            else:
                del app.monitor
            res = jsonify(res.data)
            return res

    def send_msg(self):
        with app.app_context():
            while hasattr(app, 'monitor'):
                if len(app.msgs) > 0:
                    msgs = "用例执行结果:\n\n"
                    for i in app.msgs:
                        msgs = msgs + i + '\n\n'
                    logging.info(ding(msg=msgs, at=[]))
                    app.msgs = []
                time.sleep(10)

    def add_to_monitor(self, cases, time_interval):
        with app.app_context():
            while hasattr(app, 'monitor'):
                case_id = cases[0]
                add_to_run_list(report_id=0, case_list=[case_id], env='prod')
                cases.append(case_id)
                cases.remove(case_id)
                time.sleep(time_interval)


class GetRunDetail(Resource):

    def get(self):
        res = ResMsg()
        try:
            status = int(request.args.get("status"))
            limit = int(request.args.get("limit"))
            if status == 1:
                details = db_services.get_run_details(status=1, limit=limit)
            else:
                details = db_services.get_run_details(status=0, limit=limit)
            res.update(data=details)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class GetApiLogByRunId(Resource):

    def get(self):
        res = ResMsg()
        try:
            run_id = int(request.args.get("run_id"))
            logs = db_services.get_api_logs_by_run_id(run_id=run_id)
            res.update(data=logs)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class Count(Resource):
    def get(self):
        res = ResMsg()
        try:
            db_services.count_casedetail()
            db_services.count_cover_rate()
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class Run(Resource):
    reportid = 0

    def post(self):
        res = ResMsg()
        with app.app_context():
            try:
                req = eval(request.data.decode())
                suiteid = req.get("suiteid")
                suite = req.get("suite")
                caseids = req.get("caseids")
                run_env = req.get('env')

                if suiteid:
                    caseids = db_services.get_caseids_by_suite(suiteid)
                app.api_records = []
                self.reportid = db_services.add_report()
                add_to_run_list(report_id=self.reportid, case_list=caseids, suite=suite, env=run_env)
                res.update(code=ResponseCode.SUCCESS, msg=ResponseMsg.SUCCESS, data=self.reportid)
            except Exception as e:
                res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class GetReportById(Resource):

    def get(self):
        res = ResMsg()
        try:
            report_id = request.args.get('reportid')
            data = {}
            try:
                report_url, report_status = db_services.query_report_url_and_status_by_id(report_id)
            except Exception as e:
                print(e)
                report_url = None
                report_status = None
                res.update(code=ResponseCode.FAIL, msg="reportid无效")
            data['report_url'] = report_url
            data['status'] = report_status
            res.update(data=data)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class AddCases2Suite(Resource):

    def post(self):
        res = ResMsg()
        try:
            req = eval(request.data.decode())
            suiteid = req.get("suiteid")
            caseids = req.get("caseids")
            db_services.add_cases_suite(suiteid, caseids)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class DeleteCaseSuite(Resource):
    def post(self):
        res = ResMsg()
        try:
            req = eval(request.data.decode())
            suiteid = req.get("suiteid")
            caseids = req.get("caseids")
            db_services.del_cases_suite(suiteid, caseids)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class UrlsList(Resource):
    def get(self):
        res = ResMsg()
        try:
            url_list = db_services.get_all_urls()
            data_list = {}
            data_list['url_list'] = url_list
            data_list['total'] = len(url_list)
            data_list['cover_rate'] = db_services.get_cover_rate()
            cover_count = db_services.get_cover_count()
            case_count = db_services.get_case_count()
            data_list['detail'] = "共统计到url数量为 {0} 个，已覆盖 {1} 个，用例数量为 {2} 个，平均每个url覆盖的case数量为 {3} 个".format(
                data_list['total'],
                cover_count, case_count, round(case_count / cover_count, 2))
            res.update(data=data_list)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class Status(Resource):
    def get(self):
        res = ResMsg()
        try:
            report_id = request.args.get('reportid')
            data = get_status_by_report_id(int(report_id))
            res.update(data=data)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class SuiteList(Resource):
    def get(self):
        res = ResMsg()
        try:
            suite_list = db_services.get_suite_list()
            res.update(data=suite_list)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class CaseListBySuiteId(Resource):

    def get(self):
        res = ResMsg()
        try:
            data = {}
            suiteid = int(request.args.get('suiteid'))
            caseids = db_services.get_caseids_by_suite(suiteid)
            caselist = db_services.get_case_detail_by_caseids(caseids, suiteid)
            data['caselist'] = caselist
            data['count'] = len(caselist)
            res.update(data=data)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


class HomeDetail(Resource):
    def get(self):
        res = ResMsg()
        try:
            data_detail = db_services.query_home_detail()
            res.update(data=data_detail)
        except Exception as e:
            res.update(code=ResponseCode.FAIL, msg=str(e))
        res = jsonify(res.data)
        return res


@app.route('/', methods=["GET"])
def front_index():
    return render_template('index.html')
