"""
@desc 获取百度热搜数据
"""

import time
import traceback
from selenium.webdriver import Chrome, ChromeOptions
from StorageData import ConMysql as consql

# 获取百度词云
def get_baidu_hot():
    """
    :return:返回百度热搜词
    """
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab1"
    # 得到展开全部按钮的selector
    selector = "#ptab-1 > div.Virus_1-1-300_2SKAfr > div.Common_1-1-300_3lDRV2 > span"
    xpath = "//*[@id=\"ptab-1\"]/div[3]/div/div[2]/a/div"  # 得到标题的Xpath

    # 隐藏每次打开浏览器的操作
    option = ChromeOptions()
    option.add_argument("--headless")  # 隐藏浏览器
    option.add_argument("--no-sandbox")  # 彻底停用沙箱

    # 创建浏览器对象
    brower = Chrome(options=option)
    brower.get(url)
    # print(brower.page_source)  # 获取到网页源码

    button = brower.find_element_by_css_selector(selector)
    button.click()  # 点击展开
    time.sleep(1)  # 等待1秒

    xpath_text = brower.find_elements_by_xpath(xpath=xpath)
    context = [i.text for i in xpath_text]
    # print(context)
    brower.close()
    return context


def update_hotsearch():
    """
    热搜词存入数据库
    :return:
    """
    cursor = None
    conn = None
    try:
        context = get_baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = consql.get_conn()
        sql = "insert into hotsearch (dt, content) value (%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f"{time.asctime()}数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        consql.close_conn(conn, cursor)

if __name__ == "__main__":
    pass














