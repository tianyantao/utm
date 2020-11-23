from config.config_env import get_env


new_evalution_id = 100000 if get_env() == 'prod' else 100001

if get_env() == 'prod':
    submit_url = 'http://gateway.ewt360.com/api/evaluation/eval/post/user/record'
    question_list_url = 'http://gateway.ewt360.com/api/evaluation/eval/get/user/questionlist'
    report_url = 'http://gateway.ewt360.com/api/evaluation/eval/get/group/report'

else:
    submit_url = 'http://10.0.11.86:8769/api/evaluation/eval/post/user/record'
    question_list_url = 'http://10.0.11.86:8769/api/evaluation/eval/get/user/questionlist'
    report_url = 'http://10.0.11.86:8769/api/evaluation/eval/get/group/report'
