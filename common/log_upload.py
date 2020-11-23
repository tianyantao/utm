import logging
from services.db_model import *
import datetime
from config.config_env import *



class PostApiLog:

    def post(self, test_method_name='', title='', url='', author='', module='', status='', elapsed=0, remark=''):
        if is_web() and ConfigWeb.LOG_UPLOAD:
            # 先上报到run_detail表：
            try:
                run_detail = RunDetail(test_method_name=test_method_name, title=title, url=url, author=author,
                                       module=module, status=status, elapsed=elapsed, remark=remark,
                                       update_time=datetime.datetime.now())
                session.add(run_detail)
                session.flush()
                run_id = run_detail.id
                # 再拿run_detail的id加上current_app.api_records的记录一起上报到api_log表
                if len(current_app.api_records) > 0:
                    for record in current_app.api_records:
                        record['run_id'] = run_id
                        api_record = ApiLog(run_id=run_id, req_method=record['req_method'], req_url=record['req_url'],
                                            req_data=record['req_data'], req_headers=record['req_headers'],
                                            res_status=record['res_status'], res_content=record['res_content'],
                                            elapsed=record['elapsed'], update_time=record['update_time'],
                                            remark=record['remark'], res_headers=record['res_headers'])
                        session.add(api_record)

                session.commit()
            except:
                session.rollback()
            finally:
                session.close()
            # 清空self.current_app.api_records
            current_app.api_records = []
        else:
            logging.info("跳过日志上报")

    def add_api_records(self, **kwargs):
        if is_web() and ConfigWeb.LOG_UPLOAD:
            try:
                from app import app
                with app.app_context():
                    current_app.api_records.append(kwargs)
            except Exception as e:
                logging.error("add_api_records报错:{}".format(e))


api_log = PostApiLog()