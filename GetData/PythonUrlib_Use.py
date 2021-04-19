"""
@desc 获取疫情相关数据
"""

import time
import requests
import json
import collections

'''
爬取百度
'''
# url = "http://www.baidu.com"
#
# res = request.urlopen(url=url)  # 获取响应
#
# # print(res.info())  # 响应头
# print(res.getcode())  # 响应码
# # 关于响应码的开头数字：
# # 2网页正常 3发生重定向 4访问资源有问题 5服务器内部错误
# #
# print(res.geturl())  # 返回响应地址
#
# html = res.read()
# html = html.decode("utf-8")  # 解码
# print(html)

'''
爬取大众点评
'''
# # 最简单的避免反爬虫机制
# # 添加header信息，最基本的应对反爬虫措施，请求里添加 user-agent
# url = "http://www.dianping.com"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# req = request.Request(url, headers=header)
# res = request.urlopen(req)
#
# print(res.getcode())
# print(res.geturl())

# url = "http://www.baidu.com"
# res = requests.get(url)
#
# print(res.encoding)
# print("----------")
# print(res.headers)  # headers里
#                     # 若没有Content-Type，则encoding是utf-8；
#                     # 否则如果有charset，就以设置的为准；
#                     # 否则就是ISO-8859-1
# print(res.url)
#
# res.encoding = "utf-8"  # res.encoding若无等号则是输出，若有则是设置格式
# print(res.text)

'''
添加header反爬虫
'''
# header = {
#
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# url = "http://www.dianping.com"
#
# res = requests.get(url, headers=header)
#
# print(res.status_code)  # 状态码，开头数值同urllib里res.getcode()
# res.encoding = "utf-8"
# print(res.text)

'''
卫健委获取数据
'''
# url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"
#
# res = requests.get(url=url)
#
# res.encoding = "utf-8"
# #print(res.text)
#
# html = res.text
# soup = BeautifulSoup(html, features="lxml")
#
# # soup.find(name="h2").text  # 拿到h2标签的内容
# a = soup.find(name="a")
# # print(a.attrs)
# # print(a.attrs["href"])
#
# # url_new = "http://wsjkw.sc.gov.cn/" + a.attrs["href"]
# url_new = "http://wsjkw.sc.gov.cn/"  + "scwsjkw/gzbd01/2021/1/18/97ac1fbaa0b04bee833fb877bf963c03.shtml"
#
#
# res_new = requests.get(url_new)
# res_new.encoding = "utf-8"
# soup_new = BeautifulSoup(res_new.text, features="lxml")
#
# p = soup_new.find_all(name="p")
#
# # for i, dis in enumerate(p):
# #     print(i)
# #     print(dis)
#
# context = p[1]
# # print(context.text)
#
# # pattern = "新增新型冠状病毒肺炎确诊病例(\d+)例"
# #
# #
# #
# # newConfirm = re.search(pattern=pattern, string=str(context))
# #
# # print(newConfirm.groups())  # 拿到  (\d+) 对应的值
# # print(newConfirm.group(0))  # 包括字符串pattern在内的值
# # print(newConfirm.group(1))  # 第一个参数
# # '''
# # 注意， newConfirm的值若为None，则不能使用 .groups()，需要手动调整
# # '''
# # print(re.search(pattern=pattern, string=p))
#
# # pattern = "新增新型冠状病毒肺炎确诊病例(\d+).*?出院病例(\d+).*?疑似病例(\d+).*?死亡病例(\d+)"  # .* 表示前面数字之和所有省略的，? 叫做非贪心匹配，表示匹配越少越好
#
# newAddPattern = ".*?新增新型冠状病毒肺炎确诊病例(\d+)"
# newHealPattern = ".*?新增治愈出院病例(\d+)"
# newGuessPattern = ".*?新增疑似病例(\d+)"
# newDeadPattern = ".*?新增死亡病例(\d+)"
#
# newAddConfirm = re.search(pattern=newAddPattern, string=str(context))
# newHealConfirm = re.search(pattern=newHealPattern, string=str(context))
# newGuessConfirm = re.search(pattern=newGuessPattern, string=str(context))
# newDeadConfirm = re.search(pattern=newDeadPattern, string=str(context))
#
#
# '''
# 注意， newConfirm的值若为None，则不能使用 .groups()，需要手动调整
# '''
# newAddConfirm = newAddConfirm.group(1) if(newAddConfirm != None) else 0
# newHealConfirm = newHealConfirm.group(1) if(newHealConfirm != None) else 0
# newGuessConfirm = newGuessConfirm.group(1) if(newGuessConfirm != None) else 0
# newDeadConfirm = newDeadConfirm.group(1) if(newDeadConfirm != None) else 0
# '''
# 关于re.search()的一些子函数
# re.search().groups() # 拿到  (\d+) 对应的值
# re.search().group(0) # 包括字符串pattern在内的值
# re.search().group(1) # 第一个参数
# '''
#
# ##
# # 爬取腾讯疫情数据
# #
# url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
# res = requests.get(url)
# # print(res.text)
# data = json.loads(res.text)
# data_all = json.loads(data["data"])
#
# key = data_all.keys()
# print(list(key))
#
#
# for i, dis in enumerate(list(key)):
#     print(i, dis)
#     print(data_all[dis])
#
# # print(data_all["areaTree"][0]["children"][0].keys())
#
# for i in data_all["areaTree"][0]["children"]:
#     print(i["name"])


def get_tececnt_data():
    '''
    :return: 返回历史数据及当日详细数据
    '''

    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules="
    url_DayList = url + "chinaDayList"
    url_DayAddList = url + "chinaDayAddList"
    url_all = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    history = {}

    # 历史每日新增数据
    res_DayAddList = requests.post(url_DayAddList)
    res_DayAddList = json.loads(res_DayAddList.text)
    data_DayAddList = res_DayAddList["data"]
    for i in data_DayAddList["chinaDayAddList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        importedCase_add = i["importedCase"]
        deadRate_add = i["deadRate"]
        healRate_add = i["healRate"]
        localConfirm_add = i["localConfirmadd"]
        localinfection_add = i["localinfectionadd"]
        history[ds] = {"confirm_add": confirm, "suspect_add": suspect,"heal_add": heal,
                       "dead_add": dead, "importedCase_add" : importedCase_add,
                       "deadRate_add" : deadRate_add,"healRate_add" : healRate_add,
                       "localConfirm_add" : localConfirm_add, "localinfection_add" : localinfection_add}

    # 历史每日数据
    res_DayList = requests.post(url_DayList)
    res_DayList = json.loads(res_DayList.text)
    data_DayList = res_DayList["data"]
    for i in data_DayList["chinaDayList"]:
        ds = i["y"] +"." + i["date"]
        '''
        datetime.strptime(date_string, format)将一个日期字符串转成datetime日期格式便于后期处理，
        其中date_string 就是要转成日期的字符串，format 根据date_string 不同而不同
        '''
        tup = time.strptime(ds, "%Y.%m.%d")
        '''
        time.strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
        '''
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式，数据库datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        nowConfirm = i["nowConfirm"]
        deadRate = i["deadRate"]
        healRate = i["healRate"]
        localConfirm = i["localConfirm"]
        noInfect = i["noInfect"]
        importedCase = i["importedCase"]
        if ds in history.keys():
            history[ds].update({"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead,
                                "nowConfirm":nowConfirm, "deadRate":deadRate, "healRate": healRate,
                                "localConfirm": localConfirm, "noInfect":noInfect, "importedCase":importedCase})
        else:
            history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead,
                           "nowConfirm":nowConfirm, "deadRate":deadRate, "healRate": healRate,
                           "localConfirm": localConfirm, "noInfect":noInfect, "importedCase":importedCase}

    res_all = requests.get(url_all, headers)
    res_all = json.loads(res_all.text)
    data_all = json.loads(res_all["data"])


    # 当日详细数据
    details = []
    # 当日各省确诊数据
    details_province = []

    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # 中国
    data_country = str(data_country)
    data_country = data_country.strip("[]").replace("\'", "\"")\
        .replace("True", "\"True\"").replace("False","\"False\"")
    data_country = eval(data_country)
    data_province = data_country["children"]  # 中国省份

    for pro_info in data_province:
        province = pro_info["name"]  # 省名
        details_pro = pro_info["total"]["nowConfirm"]  # 各省现有确诊
        for city_info in pro_info["children"]:
            city = city_info["name"]
            confirm = city_info["total"]["confirm"]
            confirm_add = city_info["today"]["confirm"]
            heal = city_info["total"]["heal"]
            dead = city_info["total"]["dead"]
            nowConfirm = city_info["total"]["nowConfirm"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead,nowConfirm])
        details_province.append([update_time,province,details_pro])
    return history, details, details_province


if __name__ == "__main__":
    # _,d,_ = get_tececnt_data()
    # print(d)
    pass




