import time
import json
from flask import jsonify
from StorageData import ConMysql as cs



def get_time():
    time_str = time.strftime("%Y{}%m{}%d{}%X")
    return time_str.format("年","月","日")

def query(sql, *args):
    """
    通用查询
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = cs.get_conn()
    cursor.execute(query=sql, args=args)
    res = cursor.fetchall()
    cs.close_conn(conn=conn, cursor=cursor)
    return res

def get_c1_data():
    """

    :return: 返回大屏中div id="c1"的数据
    """
    sql = "select sum(confirm)," \
          "(select suspect from history where suspect is not null order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead)" \
          "from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def get_c2_data():
    """
    :return: 返回各省数据
    """
    sql = "select province, sum(confirm) from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1)" \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    """
    :return: 返回li折线图所需数据
    """
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
    return res

def get_l2_data():
    """
    :return: 返回l2折线图所需数据
    """
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    """
    :return: 返回r1柱状图所需数据
    """
    sql = 'select province, city,nowConfirm from details where update_time=' \
          '(select update_time from details order by update_time desc limit 1) ' \
          'order by nowConfirm desc limit 5'
    res = query(sql)
    result = []
    for i in res:

        if '境外输入' in i or '地区待确认' in i :
            result.append([i[0], i[2]])
        else:
            result.append([i[1], i[2]])
    return result
    # return res


# def get_r1_data():
#     """
#     :return: 返回r1柱状图所需数据
#     """
#     sql = 'select city,confirm from (select city, confirm from details ' \
#           'where update_time=(select update_time from details order by update_time desc limit 1) ' \
#           'and province not in ("北京","上海","天津","重庆") and city not in ("地区待确认", "境外输入") ' \
#           'union all ' \
#           'select province as city,sum(confirm) as confirm from details ' \
#           'where update_time=(select update_time from details order by update_time desc limit 1) ' \
#           'and province in ("北京","上海","天津","重庆") group by province) as a ' \
#           'order by confirm desc limit 5'
#     res = query(sql)
#     return res

def get_r2_data():
    """
    :return: 返回r2当日新闻数据
    """
    sql = 'select content from hotsearch order by id desc limit 15'
    res = query(sql)  # 格式((''),(''))
    return res

def get_c2_data1():
    """
    :return: 返回各省现有确诊数据
    """
    sql = "select province, details_pro from details_province " \
          "where update_time=(select update_time from details_province order by update_time desc limit 1)"

    res = query(sql)
    return res

if __name__ == "__main__":

    r = get_c2_data1()
    print(r)

    pass







