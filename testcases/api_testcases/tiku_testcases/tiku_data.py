import requests
from config.config_env import get_env


user_vip = {"username": 'test0011', "password": 'lwl158646'} if get_env() == 'prod' else {"username": '13800000000', "password": '123456'}
# qbank的数据池
questionIdList = [1683946698346446966, 1683946698346446995, 2683947583109709925, 2683947583109709926,
                  2683947608879513602] if get_env() == 'prod' else [2678819443697336324]


def get_login_for_admin():
    admin_url = 'http://admin.mistong.com/api/ssoprod/auth/preLogin'
    try:
        headers = {"Content-Type": "application/json"}
        params = {"username": "2162", "password": "lwl158646"}
        response = requests.post(url=admin_url, headers=headers, json=params, timeout=20)  # 设置超时
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            result = response.json()['data']
            # base_operationdb_interface.op_sql("UPDATE token_total set value_config='%s' where id=4" % (result))
        else:
            result = {'message': '接口返回状态异常'}
        return result
    except:
        return "admin异常处理"


# paper的数据池
paperId = 43739 if get_env() == 'prod' else 43740
reportIdList = [718908960495640580] if get_env() == 'prod' else [718908960495640580]
reportId = '718908960495640580' if get_env() == 'prod' else '718908960495640580'
questionId = 714234 if get_env() == 'prod' else 714234

tagValueList = [{"tagValueId": "200000001"}, {"tagValueId": "200000382"}] if get_env() == 'prod' else [
    {"tagValueId": "200000001"}, {"tagValueId": "200000382"}]
