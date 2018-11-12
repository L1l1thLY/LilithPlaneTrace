from LPTrace.LPTrace import LPTrace
import getpass
import pymysql

from lputils.lpadjoint import LPAdjoint
if __name__ == '__main__':


    # 假设的飞机机型
    type = ["J-15", "J-16", "J-31", "601", "J-20", "Q-5", "Q-6", "K-8", "H-5", "H-6", "T-1", "T-2", "T-3"]

    # 假设的地区名
    country = ["China", "China", "China", "China", "China", "China", "China", "China", "China", "China", "USA", "USA", "USA"]

    # 输入密码连接数据库
    password = getpass.unix_getpass("Input database password")
    lpt = LPTrace(db_password=password, start_index=11)

    # 生成数据存入数据库
    #lpt.generate_trace()

    # 根据机型和区域得到一条飞机轨迹
    #lpt.load_db_data_to_local("T-2", "USA")

    adj = LPAdjoint(10, 0.3)

    result = adj.is_adjoint(lpt.load_db_data("H-6", "China"), lpt.load_db_data("T-1", "USA"))

    if result is True:
        print("H-6 go along with T-1.")

    result = adj.is_adjoint(lpt.load_db_data("T-1", "USA"), lpt.load_db_data("T-2", "USA"))
    if result is True:
        print("T-1 go along with T-2")


