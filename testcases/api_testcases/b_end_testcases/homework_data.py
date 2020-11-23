from config.config_env import get_env

import time

lesson_id = 21585 if get_env == 'prod' else 1798

lesson_ids = [21585, 21586] if get_env == 'prod' else [1798, 1815]

question_id = 1462228 if get_env == 'prod' else 52539

question_ids = [1462228, 1437118] if get_env == 'prod' else [52539, 52425]

paper_ids = ["43238"] if get_env == 'prod' else ["870878"]

deadline_timestamp = (int(time.time()) + 60*60*24) * 1000



