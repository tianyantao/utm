from config.config_env import get_env
import time

menu_menuId=25
menu_subjectId=2
assign_subjectId=2
solutionid1 = 33
solutionid2 = 141 # 直连
Id = 162
paperId = 856
timestring = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
paper_title = "试卷"+timestring
paper_refIds = [787]
video_title = "2个视频"+timestring
video_refIds = [2419, 1]
topic_title = "专题"+timestring
topic_refIds = [172]
if get_env() == 'prod':
    menu_menuId = 3
    menu_subjectId = 1
    assign_subjectId = 1
    solutionid1 = 11
    # solutionid2 = 141 直连
    Id = 285
    paperId = 43228
    paper_title = "试卷" + timestring
    paper_refIds = [43228]
    video_title = "2个视频" + timestring
    video_refIds = [19463, 19464]
    topic_title = "专题" + timestring
    topic_refIds = [264]



promotion_themeid = 4 if get_env() == 'prod' else 70
promotion_moduleid_xueke = 7 if get_env() == 'prod' else 87
promotion_moduleid_shengya = 9 if get_env() == 'prod' else 88
except_modules_length = 3 if get_env() == 'prod' else 5