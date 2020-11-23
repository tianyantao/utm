from config.config_env import get_env

basketforteaaddinput1 = [{"qid": 2397, "kemu": "10", "typeid": 1}] if get_env() != "prod" else [
    {"qid": 24525, "kemu": "10", "typeid": 1}]
basketforteaaddinput2 = [{"qid": 2355, "kemu": "10", "typeid": 1}, {"qid": 2356, "kemu": "10", "typeid": 1},
                         {"qid": 2357, "kemu": "10", "typeid": 1}] \
    if get_env() != "prod" else [{"qid": 24584, "kemu": "10", "typeid": 1}, {"qid": 24585, "kemu": "10", "typeid": 1},
                                 {"qid": 24602, "kemu": "10", "typeid": 1}]

typelist = [{'id': 17, 'title': '生涯规划',
             'childlist': [{'id': 17, 'title': '全部'}, {'id': 29, 'title': '认识自我'}, {'id': 31, 'title': '学会决策'},
                           {'id': 32, 'title': '学会管理'}, {'id': 49, 'title': '认识世界'}]}, {'id': 18, 'title': '志愿填报',
                                                                                        'childlist': [
                                                                                            {'id': 18, 'title': '全部'},
                                                                                            {'id': 33, 'title': '填报常识'},
                                                                                            {'id': 34, 'title': '填报技巧'},
                                                                                            {'id': 35,
                                                                                             'title': '填报案例'}]},
            {'id': 19, 'title': '大学风采', 'childlist': []}, {'id': 20, 'title': '职业介绍', 'childlist': []},
            {'id': 21, 'title': '专业解读',
             'childlist': [{'id': 21, 'title': '全部'}, {'id': 37, 'title': '工学'}, {'id': 38, 'title': '法学'},
                           {'id': 39, 'title': '教育学'}, {'id': 40, 'title': '经济学'}, {'id': 41, 'title': '文学'},
                           {'id': 42, 'title': '管理学'}, {'id': 43, 'title': '历史学'}, {'id': 44, 'title': '医学'},
                           {'id': 45, 'title': '农学'}, {'id': 46, 'title': '艺术学'}, {'id': 47, 'title': '理学'},
                           {'id': 48, 'title': '哲学'}]}] \
    if get_env() != "prod" else [{"id": 17, "title": "生涯规划",
                                  "childlist": [{"id": 17, "title": "全部"}, {"id": 31, "title": "认识自我"},
                                                {"id": 32, "title": "探索世界"}, {"id": 33, "title": "做好决策"},
                                                {"id": 34, "title": "学会管理"}]}, {"id": 18, "title": "志愿填报",
                                                                                "childlist": [{"id": 18, "title": "全部"},
                                                                                              {"id": 35,
                                                                                               "title": "填报常识"},
                                                                                              {"id": 36,
                                                                                               "title": "填报技巧"},
                                                                                              {"id": 37,
                                                                                               "title": "填报案例"}]},
                                 {"id": 19, "title": "大学风采", "childlist": []},
                                 {"id": 20, "title": "职业介绍", "childlist": []}, {"id": 21, "title": "专业解读",
                                                                                "childlist": [{"id": 21, "title": "全部"},
                                                                                              {"id": 39, "title": "工学"},
                                                                                              {"id": 40, "title": "法学"},
                                                                                              {"id": 41,
                                                                                               "title": "教育学"},
                                                                                              {"id": 42,
                                                                                               "title": "经济学"},
                                                                                              {"id": 43, "title": "文学"},
                                                                                              {"id": 44,
                                                                                               "title": "管理学"},
                                                                                              {"id": 45,
                                                                                               "title": "历史学"},
                                                                                              {"id": 46, "title": "医学"},
                                                                                              {"id": 47, "title": "农学"},
                                                                                              {"id": 48,
                                                                                               "title": "艺术学"},
                                                                                              {"id": 49, "title": "理学"},
                                                                                              {"id": 50,
                                                                                               "title": "哲学"}]}]

# 教师端习题作业
homeworkid_exercises = 332317 if get_env() != 'prod' else 1894937
classid_exercises = 543529 if get_env() != 'prod' else 869212

student_userid = 80037734 if get_env() != 'prod' else 14550976
