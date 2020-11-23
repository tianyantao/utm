from config.config_env import get_env

svip_account = "qianshui" if get_env() == 'prod' else "qianyan"
unreactivated_account = "qianwan" if get_env() == 'prod' else "qianhe"
QQopenId = "B7A0621A87508E323DD098F279499336" if get_env() == 'prod' else "72F8A3C4625EE2171814CF078000D883"
mobile = "15088738891" if get_env() == 'prod' else '15011223344'
userid = "13726882" if get_env() == 'prod' else '100113705'
ontrial = "zpyxs315410" if get_env() == 'prod' else 'kcg200918001'
