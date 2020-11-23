from config.config_env import get_env
from testcases.api_testcases.b_end_testcases.schooluser_data import current_school_year

# expireyear = 2020
# studentzzj_user = {'username': 'testautozzj001', 'password': '123456'}
student_name = '田彦涛a'
classinfo = {'classId': 173713, 'className': '新高一（1）班'} if get_env() != 'prod' else {'classId': 907448,
                                                                                     'className': '高一（1）班'}

# 3+3 自由选科
# subjectlist_33_1 = [{"id":1,"name":"物理"},{"id":2,"name":"化学"},{"id":3,"name":"生物"},{"id":4,"name":"历史"},{"id":5,"name":"地理"},{"id":6,"name":"政治"},{"id":7,"name":"技术"}]
subjectlist_33_1 = [{"id": 8, "name": "物理"}, {"id": 9, "name": "化学"}, {"id": 10, "name": "生物"},
                    {"id": 11, "name": "历史"}, {"id": 12, "name": "地理"}, {"id": 13, "name": "政治"}]
# 3+3 定二走一
subjectlist_33_2 = [{"id": 36, "name": "物理、化学"}, {"id": 37, "name": "物理、生物"}, {"id": 38, "name": "物理、历史"},
                    {"id": 39, "name": "物理、地理"}, {"id": 40, "name": "物理、政治"}, {"id": 41, "name": "物理、技术"},
                    {"id": 42, "name": "化学、生物"}, {"id": 43, "name": "化学、历史"}, {"id": 44, "name": "化学、地理"},
                    {"id": 45, "name": "化学、政治"}, {"id": 46, "name": "化学、技术"}, {"id": 47, "name": "生物、历史"},
                    {"id": 48, "name": "生物、地理"}, {"id": 49, "name": "生物、政治"}, {"id": 50, "name": "生物、技术"},
                    {"id": 51, "name": "历史、地理"}, {"id": 52, "name": "历史、政治"}, {"id": 53, "name": "历史、技术"},
                    {"id": 54, "name": "地理、政治"}, {"id": 55, "name": "地理、技术"}, {"id": 56, "name": "政治、技术"}]
# 3+3 固定套餐
subjectlist_33_3 = [{"id": 1, "name": "物理、化学、生物"}, {"id": 2, "name": "物理、化学、历史"}, {"id": 3, "name": "物理、化学、地理"},
                    {"id": 4, "name": "物理、化学、政治"}, {"id": 5, "name": "物理、化学、技术"}, {"id": 6, "name": "物理、生物、历史"},
                    {"id": 7, "name": "物理、生物、地理"}, {"id": 8, "name": "物理、生物、政治"}, {"id": 9, "name": "物理、生物、技术"},
                    {"id": 10, "name": "物理、历史、地理"}, {"id": 11, "name": "物理、历史、政治"}, {"id": 12, "name": "物理、历史、技术"},
                    {"id": 13, "name": "物理、地理、政治"}, {"id": 14, "name": "物理、地理、技术"}, {"id": 15, "name": "物理、政治、技术"},
                    {"id": 16, "name": "化学、生物、历史"}, {"id": 17, "name": "化学、生物、地理"}, {"id": 18, "name": "化学、生物、政治"},
                    {"id": 19, "name": "化学、生物、技术"}, {"id": 20, "name": "化学、历史、地理"}, {"id": 21, "name": "化学、历史、政治"},
                    {"id": 22, "name": "化学、历史、技术"}, {"id": 23, "name": "化学、地理、政治"}, {"id": 24, "name": "化学、地理、技术"},
                    {"id": 25, "name": "化学、政治、技术"}, {"id": 26, "name": "生物、历史、地理"}, {"id": 27, "name": "生物、历史、政治"},
                    {"id": 28, "name": "生物、历史、技术"}, {"id": 29, "name": "生物、地理、政治"}, {"id": 30, "name": "生物、地理、技术"},
                    {"id": 31, "name": "生物、政治、技术"}, {"id": 32, "name": "历史、地理、政治"}, {"id": 33, "name": "历史、地理、技术"},
                    {"id": 34, "name": "历史、政治、技术"}, {"id": 35, "name": "地理、政治、技术"}]
# 3+1+2模拟选科
subjectlist_312 = [{"id": 7, "name": "物理、化学、生物"}, {"id": 19, "name": "物理、化学、地理"}, {"id": 35, "name": "物理、化学、政治"},
                   {"id": 21, "name": "物理、生物、地理"}, {"id": 37, "name": "物理、生物、政治"}, {"id": 49, "name": "物理、地理、政治"},
                   {"id": 14, "name": "历史、化学、生物"}, {"id": 26, "name": "历史、化学、地理"}, {"id": 42, "name": "历史、化学、政治"},
                   {"id": 28, "name": "历史、生物、地理"}, {"id": 44, "name": "历史、生物、政治"}, {"id": 56, "name": "历史、地理、政治"}]
# 模拟选科筛选条件
conditions = {"gradelist": [{"id": 0, "name": "全部年级"},
                            {"id": (current_school_year + 4), "name": "新高一(" + str(current_school_year + 1) + "年入学)"},
                            {"id": (current_school_year + 3), "name": "高一(" + str(current_school_year) + "年入学)"},
                            {"id": (current_school_year + 2), "name": "高二(" + str(current_school_year - 1) + "年入学)"},
                            {"id": current_school_year + 1, "name": "高三(" + str(current_school_year - 2) + "年入学)"}],
              "typelist": [{"id": 0, "name": "全部", "children": []}, {"id": 4, "name": "3+1+2", "children": []},
                           {"id": 1, "name": "3+3", "children": [{"id": 1, "name": "自由选科"}, {"id": 2, "name": "定二走一"},
                                                                 {"id": 3, "name": "固定套餐"}]}],
              "statuslist": [{"id": 0, "name": "全部"}, {"id": 1, "name": "进行中"}, {"id": 2, "name": "已截止"},
                             {"id": 3, "name": "已撤回"}],
              "canpublishgrades": [{"id": 1, "name": "高一"}, {"id": 2, "name": "高二"}], "iscanpublish": True}
