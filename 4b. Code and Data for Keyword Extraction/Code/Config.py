# -*- coding:utf-8 -*-
import os
import time
"""
suggest to use python3.8
Install package: C:\python38>python.exe -m pip install xlrd==1.2.0
pip install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

# All configuration items in the program are in this file

'''Global Parameters'''
DEBUG = False  # debug mode
VISUAL_SHOW = False  # Visualization
VISUAL_SAVE = True
THREAD_NUM = 32
MULTI_MODE = True  # Multiprocessing extract key words

ARRAYID = {'docid':0, 'pubdate':1, 'non_view_engagements':2, 'comment_count':3, 'like_count':4, 'dislike_count':5, 'love_count':6, 'haha_count':7, 'wow_count':8, 'angry_count':9, 'sad_count':10, 'share_count':11, 'view_count':12, 'emoji_count':13, 'headline':14, 'pubname':15, 'author_type':16, 'pubdate1':17, 'fans_count':18, 'content':23, 'tran_headline':20, 'tran_content':21, 'cleanText_headline':22, 'cleanText_content':19, 'sentiment_headline':24, 'sentiment_label_headline':25, 'sentiment_content':26, 'sentiment_label_content':27, 'ESG_label_headline':28, 'ESG_label_score_headline':29, 'ESG_label_content':30, 'ESG_label_score_content':31}
# ARRAYID = {'docid':0, 'comment_count':1, 'like_count':2, 'dislike_count':3, 'love_count':4, 'haha_count':5, 'wow_count':6, 'angry_count':7, 'sad_count':8, 'share_count':9, 'view_count':10, 'negativeemo_count':11, 'positiveemo_count':12, 'influence_count':13, 'headline':14, 'author*':15, 'pubname':16, 'pubdate':17, 'region':18, 'fans_count':19, 'author_type':20, 'content':21}  # 字典 便于访问字段对应的列
TIME = lambda :time.strftime('%H:%M:%S',time.localtime(time.time()))  # Anonymous function to return the time. TIME()
file_time = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))


'''Preprocessing'''
PRESTR = "1 Preprocessing"
DATA_PATH = "Prediction_model\data"
ANALYSIS_PATH = "analysis"
DATA_FILENAME = DATA_PATH + os.sep + "20_22ESGsenti.xlsx"
DATA_SAVE_FILENAME = DATA_PATH + os.sep + "20_22ESGsenti.pkl"


'''Keywords'''
KEYSTR = "2 Keywords"
KEY_NUMS = 50  # Number of alternative analytic words for easy processing during analysis.
KEY_NKEY_FILENAME = ANALYSIS_PATH + os.sep + "keywords_nkey_dict.pkl"
# Keyword Extraction Algorithm
TFIDF = 'TF-IDF'
TEXTRANK = 'TextRank'
KEY_ANALUSIS_MODE = TFIDF  # TFIDF  TEXTRANK
KEY_NKEY = 10  # the number of keywords to be extracted
KEY_CLOUDNUM = 50  # Number of words drawn by the word cloud.
KEY_CLOUD_PATH = ANALYSIS_PATH + os.sep + file_time + "wordcloud.png"
KEY_TIME_INTERVAL = 7  # Discourse author analysis interval.
KEY_AUTHORJPG = "authortime.jpg"
KEY_VIS_AUTHOR_PATH = ANALYSIS_PATH + os.sep + file_time + KEY_AUTHORJPG
KEY_PUBLISHERJPG = "publishertime.jpg"
KEY_VIS_PUBLISHER_PATH = ANALYSIS_PATH + os.sep + file_time + KEY_PUBLISHERJPG

KEY_STOP_WORDS = []
with open(DATA_PATH + os.sep + "StopWords.txt", 'r', encoding="utf-8") as f:
    for line in f:
        KEY_STOP_WORDS.append(line.replace('\n', ''))


'''Emotion'''
EMOSTR = "3 Emotion"
EMO_FILENAME = ANALYSIS_PATH + os.sep + "emotion_dict.pkl"
INTERESTING_WORDS = ['']  # extract content related to respective keywords  (\\ represent null)
INTERESTING_CONTENT_FILENAME = ANALYSIS_PATH + os.sep + file_time + "content_analysis.txt"
INTERESTING_TEXT = "污染"

EMO_SAMPLE_NUMS = 3000
EMO_SAMPLE_FILENAME = "sample_key.pkl"
EMO_ONEKEYJPG = "onekey_emotion.jpg"

EMO_MANUAL_JPG = "manual_emotion.jpg"
EMO_VIS_MANUAL_PATH = ANALYSIS_PATH + os.sep + file_time + EMO_MANUAL_JPG

# Analysis by time
TIME_MODE = "time_mode"
TIME_INTERVAL = 30  # days interval of analysis
EACH_LINE_KEYWORDS = 1  # Number of keywords extracted from each line of data  Range:1-3
EACH_WEEKEND_N = 12  # Number of keywords extracted each week
ENABLE_TIME_WEIGHT = True  # Whether to allow weighting, only return the results that have specified keyword(s)
TIME_TXT_FILENAME = ANALYSIS_PATH + os.sep + file_time + "time_analysis.txt"
# Emotion analysis
EMO_MODE = "emo_mode"
ZEROEQUNUM = 'zeroequnum' # Result displayed
MANUAL_POSNUM = 'manual_pos'
MANUAL_NEGNUM = 'manual_neg'
MANUAL_EQUNUM = 'manual_equ'
ZEROEQU = 'zeroequ'
EQU = 'equ'
POS = 'pos'
NEG = 'neg'
EMO_EACH_LINE = 1  # Number of keywords extracted from each line of data  Range:1-3
EACH_EMO_N = 50
ENABLE_EMO_WEIGHT = True  # Whether to allow weighting, only return the results that have specified keyword(s)
EMO_TXT_FILENAME = ANALYSIS_PATH + os.sep + file_time + "emo_analysis.txt"

# Conditional Analysis
TIME_ANALYSIS = "timeAnalysis"
EMOTION_ANALYSIS = "emotionAnalysis"

'''Customized'''
CUSSTR = "4 Customized"
CUS_CSVFILENAME = ".csv"

CUS_CORRELATED_KEYNUMS = 3
CUS_CONTFILENAME = "cont.txt"

CUS_ONEKEYJPG = "onekey.jpg"
CUS_VIS_ONEKEY_PATH = ANALYSIS_PATH + os.sep + file_time + CUS_ONEKEYJPG

# debug
if DEBUG:
    DATA_FILENAME = DATA_PATH + os.sep + "test.xlsx"
    DATA_SAVE_FILENAME = DATA_PATH + os.sep + "test.pkl"
    KEY_NKEY_FILENAME = ANALYSIS_PATH + os.sep + "nkey_test.pkl"
    EMO_FILENAME = ANALYSIS_PATH + os.sep + "emotion_test.pkl"
