import requests
import pandas
import pyecharts
import requests
from bs4 import BeautifulSoup
import re

a = ('香港', '地区待确认', 186)

if '地区待确认' in a:
    print("yes")
else:
    print("no")

# print(type({}))
# b={}
#
#
# a= {"2.14":{"confirm_add": 1, "suspect_add": 1}}
# # a['2.14'] = {"confirm": 3, "suspect_add": 3}
# a['2.15'] = {"confirm": 2, "suspect_add": 2}
# print(a)

# print(int(False))

# a = None
#
# print(a if(a != None) else 0 )


# data = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')
# data = data.json()

# text = "四川新增新型冠状病毒肺炎确诊病例1例（境外输入，为1月8日无症状感染者转确诊），无新增治愈出院病例0，无新增疑似病例，无新增死亡病例。"
#
# pattern = "新增治愈出院病例(\d+)"
# pipei = re.search(pattern=pattern, string=str(text))
# newConfirm = pipei if(pipei != None) else 0
# print(newConfirm.group(1))



# import random
#
# while(1):
#     print(random.randint(1,99))

