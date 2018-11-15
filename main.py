from LPTrace.LPTrace import LPTrace
import getpass
import pymysql
import json
import os
from lputils.lpadjoint import LPAdjoint

# {
#   "width": 600,
#   "height": 600,
#   "number": 1,
#   "shape_file": "shape/line_shape.json"
# }

def auto_config(number, shape_path, width=600, height=600):
    config = dict()
    with open("generation_config.json", "w") as file:
        config["width"] = width;
        config["height"] = height;
        config["number"] = number
        config["shape_file"] = shape_path;
        json.dump(config, file, indent=2)


# ！！！ 运行过后请不要重复运行
# 确定已经创造了数据库并赋予当前用户使用数据库的权限再使用
# Ensure that the database has been created and all privileges granted.
# create user 'lilith'@'localhost' identified by 'qls666';
# source /path/to/model/creat_databases.sql

def pump_sample_data():
    # 假设的飞机机型
    type = ["J-15", "J-16", "J-31", "601", "J-20", "Q-5", "Q-6", "K-8", "H-5", "H-6", "T-1", "T-2", "T-3"]
    # 假设的地区名
    country = ["China", "China", "China", "China", "China", "China", "China", "China", "China", "China", "USA", "USA",\
               "USA"]

    # 生成3张8字型轨迹并存入数据库
    auto_config(3, "shape/eight_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=0)
    lpt.generate_trace()
    # 生成2张圆形轨迹并存入数据库
    auto_config(2, "shape/circle_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=3)
    lpt.generate_trace()
    # 生成2张三角型轨迹并存入数据库
    auto_config(2, "shape/triangle_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=5)
    lpt.generate_trace()
    # 生成3张方形轨迹并存入数据库
    auto_config(3, "shape/square_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=7)
    lpt.generate_trace()
    # 生成1张线型轨迹存入数据库
    auto_config(1, "shape/line_with_square_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=10)
    lpt.generate_trace()
    # 生成1张线型轨迹存入数据库
    auto_config(1, "shape/line_shape.json")
    lpt = LPTrace(db_password="qls666", start_index=11)
    lpt.generate_trace()


def test_LPAjoint(lpt, adj):

    result = adj.is_adjoint(lpt.load_db_data("H-6", "China"), lpt.load_db_data("T-1", "USA"))
    if result is True:
        print("H-6 go along with T-1.")

    result = adj.is_adjoint(lpt.load_db_data("T-1", "USA"), lpt.load_db_data("T-2", "USA"))
    if result is True:
        print("T-1 go along with T-2")

if __name__ == '__main__':
    # # 生成数据库数据
    # pump_sample_data()
    # #输入密码连接数据库
    # #password = getpass.unix_getpass("Input database password")
    lpt = LPTrace(db_password="qls666", start_index=0)
    lpt.load_db_data_to_local("H-6", "China")
    #规定相伴行为
    #参数1 ： 多少公里内
    #参数2 ： 在 <参数1> 公里内，后者飞机跟随超过了前者飞机总路程的多少比率
    adj = LPAdjoint(6, 0.2)
    test_LPAjoint(lpt, adj)




