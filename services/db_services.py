from services.db_model import *
from sqlalchemy import func, distinct
import logging
import datetime
import unittest
import re


class DbServices:

    @staticmethod
    def get_case_detail_by_ids(ids):
        case_data = []
        session.commit()
        res = session.query(CaseDetail).filter(CaseDetail.id.in_(ids), CaseDetail.is_deleted == 0).all()
        for i in res:
            case = {}
            case['case_id'] = i.id
            case['test_method_name'] = i.test_method_name
            case['title'] = i.title
            case['url'] = i.url
            case['author'] = i.author
            case['module'] = i.module
            case['create_time'] = i.create_time
            case_data.append(case)
        return case_data

    @staticmethod
    def get_name_by_ids(ids):
        names = []
        res = session.query(CaseDetail).filter(CaseDetail.id.in_(ids), CaseDetail.is_deleted == 0).with_entities(
            CaseDetail.module, CaseDetail.test_method_name).all()
        for i in res:
            name = "{0}.{1}".format(i.module, i.test_method_name)
            names.append(name)
        return names

    @staticmethod
    def get_all_cases():
        case_data = []
        session.commit()
        case_list_all = session.query(CaseDetail.id, CaseDetail.test_method_name, CaseDetail.title, CaseDetail.module,
                                      CaseDetail.author, CaseDetail.url, CaseDetail.update_time,
                                      func.group_concat(CaseSuite.suite_id)).outerjoin(CaseSuite,
                                                                                       CaseDetail.id == CaseSuite.case_id).filter(
            CaseDetail.is_deleted == 0).group_by(CaseDetail.id).order_by(CaseDetail.id.desc()).all()
        session.close()
        for i in case_list_all:
            case = {}
            case['case_id'] = i[0]
            case['test_method_name'] = i[1]
            case['title'] = i[2]
            case['module'] = i[3]
            case['author'] = i[4]
            case['url'] = i[5]
            case['update_time'] = str(i[6])
            case['suite_ids'] = i[7]
            case_data.append(case)
        return case_data

    @staticmethod
    def get_suite_list():
        suite_list = []
        res = session.query(Suite).filter(Suite.suite_name != '').order_by(Suite.time_interval.asc()).all()
        if len(res) > 0:
            for i in res:
                suite_list.append({
                    "suite_id": i.id,
                    "suite_name": i.suite_name,
                    "is_monitor": i.is_monitor,
                    "time_interval": i.time_interval
                })
        return suite_list

    @staticmethod
    def get_caseids_by_suite(suite_id):
        caseids = []
        res = session.query(CaseSuite.case_id).filter(CaseSuite.suite_id == suite_id).all()
        for i in res:
            caseids.append(i[0])
        return caseids

    @staticmethod
    def add_case_suite(case_id, suite_id):
        res = session.query(CaseSuite.id).filter(CaseSuite.case_id == case_id, CaseSuite.suite_id == suite_id).all()
        if len(res) > 0:
            return True
        else:
            try:
                case_suite = CaseSuite(case_id=case_id, suite_id=suite_id, update_time=datetime.datetime.now())
                session.add(case_suite)
                session.commit()
                return True
            except Exception as e:
                logging.error(e)
                return False

    @staticmethod
    def add_api_log(req_method='', req_url='', req_data='', req_headers='', res_status=0, res_content='', elapsed=0,
                    remark='', res_headers='', run_id=0):
        try:
            api_log = ApiLog(run_id=run_id, req_method=req_method, req_url=req_url, req_data=req_data,
                             req_headers=req_headers, res_status=res_status, res_content=res_content, elapsed=elapsed,
                             remark=remark, res_headers=res_headers, update_time=datetime.datetime.now())
            session.add(api_log)
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    def add_run_detail(test_method_name='', title='', url='', author='', module='', status='', elapsed=0, remark=''):
        try:
            run_detail = RunDetail(test_method_name=test_method_name, title=title, url=url, author=author,
                                   module=module, status=status, elapsed=elapsed, remark=remark,
                                   update_time=datetime.datetime.now())
            session.add(run_detail)
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    def add_urls(url='', belong='', remark='', is_cover=0, is_must_cover=0, count=0):
        try:
            urls = Urls(url=url, remark=remark, belong=belong, is_cover=is_cover, is_must_cover=is_must_cover,
                        count=count, update_time=datetime.datetime.now())
            session.add(urls)
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    def get_all_monitor_cases(self):
        monitor_cases = {}
        suites = session.query(Suite).filter(Suite.is_monitor == 1, Suite.is_deleted == 0).order_by(
            Suite.time_interval.asc()).all()
        for i in suites:
            monitor_cases[i.time_interval] = self.get_caseids_by_suite(i.id)
        session.close()
        return monitor_cases

    @staticmethod
    def get_name_from_ids(ids):
        names = []
        if isinstance(ids, list):
            for i in ids:
                i = int(i)
                try:
                    res = session.query(CaseDetail).filter(CaseDetail.id == i, CaseDetail.is_deleted == 0).first()
                    if res:
                        module = res.module
                        test_method = res.test_method_name
                        name = "{0}.{1}".format(module, test_method)
                        names.append(name)
                except Exception as e:
                    logging.error(e)
        return names

    @staticmethod
    def get_run_details(status=0, limit=20):
        details = []
        res = []
        session.commit()
        if status == 0:
            res = session.query(RunDetail).order_by(RunDetail.id.desc()).limit(limit).all()
        if status == 1:
            res = session.query(RunDetail).filter(RunDetail.status == 'F').order_by(RunDetail.id.desc()).limit(limit).all()
        if len(res) > 0:
            for i in res:
                detail = {}
                detail['test_method_name'] = i.test_method_name
                detail['id'] = i.id
                detail['title'] = i.title
                detail['url'] = i.url
                detail['author'] = i.author
                detail['status'] = i.status
                detail['elapsed'] = i.elapsed
                detail['is_monitor'] = 1 if i.remark == 'monitor' else 0
                detail['update_time'] = str(i.update_time)
                details.append(detail)
        return details

    @staticmethod
    def get_api_logs_by_run_id(run_id):
        logs = []
        session.commit()
        res = session.query(ApiLog).filter(ApiLog.run_id == run_id).all()
        if len(res) > 0:
            for i in res:
                log = {}
                log['req_method'] = i.req_method
                log['req_url'] = i.req_url
                log['req_data'] = i.req_data
                log['http_status'] = i.res_status
                log['elapsed'] = i.elapsed
                log['update_time'] = str(i.update_time)
                log['res_content'] = i.res_content
                log['res_headers'] = i.res_headers
                logs.append(log)
        return logs

    def count_cases(self):
        suite = unittest.defaultTestLoader.discover(start_dir="./testcases", pattern="*_test.py")
        cases = []
        for i in suite:
            for j in i:
                for a in j._tests:
                    case = {}
                    b = str(a)
                    testmethod = a._testMethodName
                    module = b.split(' ')[-1].replace('(', '').replace(')', '')
                    doc = a._testMethodDoc
                    title = None
                    url = None
                    author = None
                    try:
                        title = re.findall("(?<=title:).*", doc)[0]
                        url = re.findall("(?<=url:).*", doc)[0]
                        author = re.findall("(?<=author:).*", doc)[0]
                    except:
                        logging.error("统计出错: {}".format(testmethod))
                    case['testmethod'] = testmethod
                    case['module'] = module
                    case['title'] = '' if not title else title.strip()
                    case['url'] = '' if not url else url.strip()
                    case['author'] = '' if not author else author.strip()
                    cases.append(case)
        return cases

    def count_casedetail(self):
        cases = self.count_cases()
        remark1 = session.query(CaseDetail).filter(CaseDetail.is_deleted == 0).all()
        remark1 = list(map(lambda x: x.test_method_name + '|' + x.url, remark1))
        update_time = datetime.datetime.now()
        for case in cases:
            test_method_name = case['testmethod']
            module = case['module']
            title = case['title']
            author = case['author']
            url = case['url']
            remark2 = test_method_name + '|' + url
            if remark2 in remark1:
                case_detail = session.query(CaseDetail).filter(CaseDetail.test_method_name == test_method_name,
                                                               CaseDetail.url == url, CaseDetail.is_deleted == 0).all()
                for i in case_detail:
                    i.update_time = update_time
                    i.module = module
                    i.title = title
                    i.author = author
                session.commit()
                remark1.remove(remark2)
            else:
                case_detail = CaseDetail(update_time=update_time, module=module, title=title, author=author,
                                         test_method_name=test_method_name, url=url, create_time=update_time, is_deleted=0)
                session.add(case_detail)
                session.commit()
        if len(remark1) > 0:
            for i in remark1:
                method_name = i.split('|')[0]
                url = i.split('|')[1]
                case_detail = session.query(CaseDetail).filter(CaseDetail.test_method_name == method_name,
                                                               CaseDetail.url == url, CaseDetail.is_deleted == 0).first()
                case_detail.update_time = update_time
                case_detail.is_deleted = 1
                session.commit()


    @staticmethod
    def count_cover_rate():
        res = session.query(CaseDetail).filter(CaseDetail.is_deleted == 0).all()
        urls_covered = []
        for i in res:
            if ',' in i.url:
                url = i.url.split(',')
                for j in url:
                    urls_covered.append(j.strip())
            elif '，' in i.url:
                url = i.url.split('，')
                for j in url:
                    urls_covered.append(j.strip())
            else:
                urls_covered.append(i.url)
        res = session.query(Urls.url).filter(Urls.is_deleted == 0).distinct().all()
        urls_all = []
        for i in res:
            urls_all.append(i[0])
        urls_insert = [i for i in urls_covered if i not in urls_all]
        urls_insert = list(set(urls_insert))
        for url in urls_insert:
            url_data = Urls(url=url, is_deleted=0, is_cover=1, is_must_cover=1, count=0)
            session.add(url_data)
            session.commit()

        # 初始化覆盖次数
        urls_data = session.query(Urls).all()
        for i in urls_data:
            i.count = 0
        session.commit()

        for i in urls_covered:
            res = session.query(Urls).filter(Urls.url == i).all()
            for i in res:
                i.count = i.count+1
            session.commit()

    @staticmethod
    def add_report():
        report_data = ReportLog(create_time=datetime.datetime.now())
        session.add(report_data)
        session.flush()
        report_id = report_data.id
        return report_id

    @staticmethod
    def update_report(id, total, assert_fail, run_error, skiped, success, report_url, status):
        report_data = session.query(ReportLog).filter(ReportLog.id == id).first()
        report_data.total = total
        report_data.assert_fail = assert_fail
        report_data.run_error = run_error
        report_data.skiped = skiped
        report_data.success = success
        report_data.report_url = report_url
        report_data.status = status
        report_data.update_time = datetime.datetime.now()
        session.commit()

    @staticmethod
    def query_report_url_and_status_by_id(report_id):
        res = session.query(ReportLog).filter(ReportLog.id == report_id).first()
        return res.report_url, res.status

    @staticmethod
    def add_cases_suite(suiteid, caseids):
        try:
            for caseid in caseids:
                res = session.query(CaseSuite).filter(CaseSuite.suite_id == suiteid, CaseSuite.case_id == caseid).all()
                if len(res) == 0:
                    case_suite_data = CaseSuite(suite_id=suiteid, case_id=caseid, update_time=datetime.datetime.now())
                    session.add(case_suite_data)
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    def del_cases_suite(suiteid, caseids):
        try:

            for caseid in caseids:
                if int(suiteid) == 0:
                    session.query(CaseSuite).filter(CaseSuite.case_id == caseid).delete()
                else:
                    session.query(CaseSuite).filter(CaseSuite.suite_id == suiteid, CaseSuite.case_id == caseid).delete()
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    def get_all_urls():
        urls = []
        res = session.query(Urls).filter(Urls.is_deleted == 0).order_by(Urls.id.desc()).all()
        for i in res:
            urls.append({
                "id": i.id,
                "url": i.url,
                "belong": i.belong,
                "remark": i.remark,
                "is_cover": "已覆盖" if i.is_cover else "未覆盖",
                "count": i.count,
                "is_must_cover": i.is_must_cover
            })
        return urls

    @staticmethod
    def get_cover_rate():
        total = session.query(func.count(distinct(Urls.url))).filter(Urls.is_deleted == 0).first()[0]
        cover = session.query(func.count(distinct(Urls.url))).filter(Urls.is_deleted == 0, Urls.is_cover == 1).first()[0]
        return round(cover / total, 3)

    @staticmethod
    def get_cover_count():
        cover = session.query(func.count(distinct(Urls.url))).filter(Urls.is_deleted == 0, Urls.is_cover == 1).first()[
            0]
        return cover

    @staticmethod
    def get_case_count():
        count_cases = session.query(func.count(distinct(CaseDetail.id))).filter(CaseDetail.is_deleted == 0).first()[0]
        return count_cases

    @staticmethod
    def get_case_detail_by_caseids(caseids, suiteid=0):
        case_detail_list = []
        try:
            for caseid in caseids:
                try:
                    res = session.query(CaseDetail).filter(CaseDetail.id == caseid, CaseDetail.is_deleted == 0).first()
                    if res:
                        case_detail_list.append({
                            "case_id": res.id,
                            "test_method_name": res.test_method_name,
                            "title": res.title,
                            "url": res.url,
                            "author": res.author,
                            "module": res.module,
                            "update_time": str(res.update_time),
                            "suite_id": suiteid
                        })
                except:
                    session.rollback()
                finally:
                    session.close()
        except Exception as e:
            logging.error(e)
        return case_detail_list

    @staticmethod
    def query_report_detail_by_id(report_id):
        res = session.query(ReportLog).filter(ReportLog.id == report_id).first()
        return res

    def query_home_detail(self):
        data_detail = {}
        data_detail['count_total_case'] = self.get_case_count()
        data_detail['count_cover_urls'] = session.query(func.count(distinct(Urls.url))).filter(Urls.is_deleted == 0, Urls.is_cover == 1).first()[0]
        all_suite_cases = session.query(CaseSuite.case_id).all()
        all_s_c = []
        for i in all_suite_cases:
            all_s_c.append(i[0])
        all_suite_cases = tuple(all_s_c)
        data_detail['count_monitor_case'] = session.query(func.count(CaseDetail.id)).filter(CaseDetail.id.in_(all_suite_cases)).first()[0]
        session.close()
        return data_detail





db_services = DbServices()

# print(db_services.get_run_details())
