from config.config_env import get_env

role = {'principal_user': 1, 'psychologicalteacher_user': 5, 'headteacher_user': 6, 'grademaster_user': 2,
        'teacher_user': 7, 'classheadteacher_user': 4}

if get_env() == 'prod':
    liveId = 201  # sbrlive_test, 校长布置给groupid_xingzheng的直播，观看人数1人
    liveInfo = {'id': '201', 'liveName': 'zidonghuayongli', 'roomStyle': 1, 'startTime': '1598281720000',
                'finishTime': '1598284440000', 'classType': 1, 'numberOfStudent': None,
                'gradeClassList': [{'graduationYear': 2022, 'isAll': 1, 'classIdList': None}]}


else:
    liveId = 253  # sbrlive_test，校长布置给groupid_xingzheng的直播，观看人数1人253
    liveInfo = {'id': '253', 'liveName': 'iOS冒烟用例', 'roomStyle': 1, 'startTime': '1596502813000',
                'finishTime': '1596506413000', 'classType': 1, 'numberOfStudent': None,
                'gradeClassList': [{'graduationYear': 2020, 'isAll': 0, 'classIdList': ['543529']}]}  # sbrlive_test
