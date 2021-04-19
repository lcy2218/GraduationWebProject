from GetData import PythonUrlib_Use
from StorageData import ConMysql
from GetData import GetBaiduWord


if __name__ == '__main__':

    ConMysql.update_history()
    ConMysql.update_details()
    GetBaiduWord.update_hotsearch()
    ConMysql.update_details_province()