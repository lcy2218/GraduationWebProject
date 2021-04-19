"""
@desc 向数据库存入消息
"""

import pymysql
import time
import traceback  # 追踪异常

from GetData import PythonUrlib_Use

host = "localhost"
port = 3306
user = "root"
password = "1707004219"
database = "covid_data"
charset = "utf8"


# conn = pymysql.connect(
#     host=host,
#     port=port,
#     user=user,
#     password=password,
#     db=database,
#     charset=charset
# )
#
# # 创建游标
# cursor = conn.cursor()  # 执行完毕返回结果
# # 默认元组形式
#
# # 执行操作
# sql = "select * from details limit 3"
# cursor.execute(sql)
# res = cursor.fetchall()  # 获取所有查询结果
# print(res)
#
# cursor.close()
# conn.close()


def get_conn():
    '''
    :return:连接，游标cursor
    '''
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=database,
        charset=charset
    )
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def update_details():
    """
    更新数据库details表
    :return:
    """
    cursor = None
    conn = None
    try:
        li = PythonUrlib_Use.get_tececnt_data()[1]  # 获取最新数据列表
        conn, cursor = get_conn()
        sql = "insert into details(update_time, province, city, confirm, confirm_add, heal, dead,nowConfirm) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"  # 对比最大时间戳,
        # order by id desc 降序排序,limit 1 限制一条数据
        cursor.execute(sql_query, li[0][0])

        if not cursor.fetchone()[0]:  # cursor.fetchone()只取第一条结果，返回单个元组
            print(f"{time.asctime()} 开始更新最新数据")  # f 字符串里面使用用花括号括起来的变量和表达式
            for item in li:

                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}最新数据更新完毕")
        else:
            print(f"{time.asctime()}最新数据已是最新数据！")

    except:
        traceback.print_exc()  # 输出出错位置
    finally:
        close_conn(conn, cursor)


def insert_history():
    """
    插入历史值
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = PythonUrlib_Use.get_tececnt_data()[0]  # 得到历史数据
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history(ds,confirm, confirm_add, suspect, suspect_add, heal,heal_add," \
                            "dead,dead_add,nowConfirm,healRate,deadRate,localConfirm,deadRate_add,healRate_add," \
                            "localConfirm_add,localinfection_add,noInfect,importedCase,importedCase_add) " \
                            "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for key, values in dic.items():  # items()以列表返回可遍历的(键, 值) 元组数组
            cursor.execute(sql, [key, values.get("confirm"), values.get("confirm_add"), values.get("suspect"),
                                 values.get("suspect_add"), values.get("heal"), values.get("heal_add"),
                                 values.get("dead"), values.get("dead_add"),values.get("nowConfirm"),
                                 values.get("healRate"), values.get("deadRate"),values.get("localConfirm"),
                                 values.get("deadRate_add"), values.get("healRate_add"),values.get("localConfirm_add"),
                                 values.get("localinfection_add"), values.get("noInfect"), values.get("importedCase"),
                                 values.get("importedCase_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")

    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

def update_history():
    """
    更新历史数据
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = PythonUrlib_Use.get_tececnt_data()[0]  # 得到历史数据
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql_del = "truncate covid_data.history"
        cursor.execute(sql_del)
        sql = "insert into history(ds,confirm, confirm_add, suspect, suspect_add, heal,heal_add," \
              "dead,dead_add,nowConfirm,healRate,deadRate,localConfirm,deadRate_add,healRate_add," \
              "localConfirm_add,localinfection_add,noInfect,importedCase,importedCase_add) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        for key, values in dic.items():  # items()以列表返回可遍历的(键, 值) 元组数组
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key, values.get("confirm"), values.get("confirm_add"), values.get("suspect"),
                                     values.get("suspect_add"), values.get("heal"), values.get("heal_add"),
                                     values.get("dead"), values.get("dead_add"),values.get("nowConfirm"),
                                     values.get("healRate"), values.get("deadRate"),values.get("localConfirm"),
                                     values.get("deadRate_add"), values.get("healRate_add"),values.get("localConfirm_add"),
                                     values.get("localinfection_add"), values.get("noInfect"), values.get("importedCase"),
                                     values.get("importedCase_add")])
        conn.commit()
        print(f"{time.asctime()}历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

def update_details_province():
    """
    更新每日各省现有确诊数据
    :return:
    """
    cursor = None
    conn = None
    try:
        de = PythonUrlib_Use.get_tececnt_data()[2]
        print(f"{time.asctime()}开始更新各省现有确诊数据")
        conn, cursor = get_conn()
        sql = "insert into details_province(update_time, province,details_pro) values (%s,%s,%s)"
        sql_query = "select %s=(select update_time from details_province order by id desc limit 1)"  # 对比最大时间戳,
        # order by id desc 降序排序,limit 1 限制一条数据
        cursor.execute(sql_query, de[0][0])

        if not cursor.fetchone()[0]:  # cursor.fetchone()只取第一条结果，返回单个元组
            for item in de:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}最新各省现有确诊更新完毕")
        else:
            print(f"{time.asctime()}各省现有确诊已是最新数据！")

    except:
        traceback.print_exc()  # 输出出错位置
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    # insert_details_province()
    update_details()
    pass