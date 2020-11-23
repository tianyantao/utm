import unittest
import re
import logging
import time
import datetime
from common.helper import get_mac_address


class TestCaseV2(unittest.TestCase):
    maxDiff = 800 * 8

    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        result.startTest(self)

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, self, skip_why)
            finally:
                result.stopTest(self)
            return
        expecting_failure_method = getattr(testMethod,
                                           "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self,
                                          "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method
        # outcome = _Outcome(result)
        outcome = unittest.case._Outcome(result)
        elapsed = ''
        try:
            self._outcome = outcome

            with outcome.testPartExecutor(self):
                self.setUp()
            if outcome.success:
                outcome.expecting_failure = expecting_failure
                with outcome.testPartExecutor(self, isTest=True):
                    start_time = datetime.datetime.now()
                    testMethod()
                    stop_time = datetime.datetime.now()
                    elapsed = (stop_time - start_time).total_seconds()
                outcome.expecting_failure = False
                with outcome.testPartExecutor(self):
                    self.tearDown()

            self.doCleanups()
            for test, reason in outcome.skipped:
                self._addSkip(result, test, reason)
            self._feedErrorsToResult(result, outcome.errors)
            if outcome.success:
                if expecting_failure:
                    if outcome.expectedFailure:
                        self._addExpectedFailure(result, outcome.expectedFailure)
                    else:
                        self._addUnexpectedSuccess(result)
                else:
                    result.addSuccess(self)
            return result
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()


            try:
                r = 'P'
                if not self._outcome.success:
                    r = 'F'



                title = []
                url = []
                author = []
                if self._testMethodDoc:
                    try:
                        title = re.findall("(?<=title:).*", self._testMethodDoc)
                        url = re.findall("(?<=url:).*", self._testMethodDoc)
                        author = re.findall("(?<=author:).*", self._testMethodDoc)
                    except:
                        logging.warning("取不到用例信息: {}".format(self._testMethodName))
                title = "" if title == [] else title[0].strip()
                url = "" if url == [] else url[0].strip()
                author = "" if author == [] else author[0].strip()
                is_monitor = 0
                try:
                    from flask import current_app
                    if hasattr(current_app, 'monitor_run'):
                        is_monitor = 1
                        current_app.msgs.append("{0} status:{1} author:{2}".format(title, r, author, elapsed))
                except Exception as e:
                    logging.warning(e)
                try:
                    remark = 'monitor' if is_monitor else get_mac_address()
                    from common.log_upload import api_log
                    api_log.post(test_method_name=self._testMethodName, title=title, url=url, author=author,
                                 module=self.__class__.__module__, status=r, elapsed=elapsed, remark=remark)

                    logging.info("{0} {1} {2} status:{3} author:{4} 耗时:{5}s".format(self.__class__.__module__,
                                                                                    self._testMethodName, title, r,
                                                                                    author, elapsed))
                except Exception as e:
                    logging.error("用例执行结果上报失败: {0} \n {1}".format(self._testMethodName, e))

            except Exception:
                print("上报自动化测试数据异常")



            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None

            # clear the outcome, no more needed
            self._outcome = None


