from config.config_env import get_env

sleeptime = 20 if get_env() != 'prod' else 30
basketaddinputs1 = [{"Qid": 343, "KeMu": 1, "KnowledgeId": -1}] if get_env() != 'prod' else [
    {"Qid": 2096, "KeMu": "1", "KnowledgeId": -1}]
basketaddinputs2 = [{"Qid": 343, "KeMu": 1, "KnowledgeId": -1}, {"Qid": 342, "KeMu": 1, "KnowledgeId": -1},
                    {"Qid": 99, "KeMu": 1, "KnowledgeId": -1}] \
    if get_env() != 'prod' else [{"Qid": 2096, "KeMu": "1", "KnowledgeId": -1}, {"Qid": 2094, "KeMu": "1", "KnowledgeId": -1}]

knowLedgeIds = [7682, 7683, 6678, 6727, 6775, 6871, 6902, 6851, 6852, 6793, 6853, 6856, 6857, 6858, 6859, 6860, 6861,
                6862, 6863, 6865, 6866, 6947, 6948, 6949, 6950, 6876, 6877, 6878, 6879, 6951, 6943, 6944, 6945, 6946,
                7027, 7028]
