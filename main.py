from LPTrace.LPTrace import LPTrace
import getpass
import pymysql
if __name__ == '__main__':


    # 假设的飞机机型
    type = ["J-15", "J-16", "J-31", "601", "J-20", "Q-5", "Q-6", "K-8", "H-5", "H-6"]

    # 假设的地区名
    country = ["China", "China", "China", "China", "China", "China", "China", "China", "China", "China"]

    # 输入密码连接数据库
    password = getpass.unix_getpass("Input database password")
    lpt = LPTrace(db_password=password, start_index=0)

    # 生成数据存入数据库
    #lpt.generate_trace()

    # 根据机型和区域得到一条飞机轨迹
    lpt.load_db_data_to_local("J-15", "China")


