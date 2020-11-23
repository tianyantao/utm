# from config.config_env import get_env


class ConfigWeb:

    # ENV = get_env()

    DATABASE_URI = 'mysql://dev_user:123456@10.96.166.194:3306/py_test_v2?charset=utf8'

    FRONT_FOLDER = 'front/dist'

    LOG_UPLOAD = True

    RETRY = True

    # 质量组内部提醒
    DING_WEBHOOK_ZHILIANGZU = "https://oapi.dingtalk.com/robot/send?access_token=83a007cf771b185ccd555282513d5ef9c2639e09880ec05d0b96f597a1f4b0f0"

    # B端业务告警群：
    DING_WEBHOOK_B = "https://oapi.dingtalk.com/robot/send?access_token=bd7007c33d5ca1eea770ee3df60262d7ee110cb60ec4005d299b048beb1f941d"

    # 正式提醒钉钉（zabbix）：
    DING_WEBHOOK_ZABBIX = "https://oapi.dingtalk.com/robot/send?access_token=5524c40ac8facefa0d4d7640f6a1fa40d4bbc724aa1a056aafb2e59973641851"

    CONFIG_DING = \
        {
            "b_end_testcases": {
                "webhook": DING_WEBHOOK_B,
                "ding_at": [
                    "13388601523",
                    "18258143797"
                ]
            },
            "school_user_service": {
                "webhook": DING_WEBHOOK_B,
                "ding_at": [
                    "13388601523",
                    "15906608944"
                ]
            },
            "tiku_testcases": {
                "webhook": DING_WEBHOOK_ZABBIX,
                "ding_at": [
                    "15868477646"
                ]
            },
            "usercenter_testcases": {
                "webhook": DING_WEBHOOK_ZABBIX,
                "ding_at": [
                    "15088738891"
                ]
            },
            "unittest": {
                "webhook": DING_WEBHOOK_ZHILIANGZU,
                "ding_at": [
                    "13388601523"
                ]
            }
        }


