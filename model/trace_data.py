import pymysql
import datetime

class TraceDatabase(object):
    def __init__(self, passwd):
        self.db = pymysql.connect("localhost", "lilith", passwd, "tracedb")

    def save_trace_to_db(self, bezier_point, index):
        altitude = 999.0
        speed = 5000
        type = ["J-15", "J-16", "J-31", "601", "J-20", "Q-5", "Q-6", "K-8", "H-5", "H-6"]
        country = ["China", "China", "China", "China", "China", "China", "China", "China", "China", "China"]
        min_lat = 28.6424029677
        min_lon = 121.4263952776
        max_lon = 124.3707275391
        delta = max_lon - min_lon / 600
        dt = datetime.datetime.now()
        dt_str = format()
        cursor = self.db.cursor()



        for i, x_point in enumerate(bezier_point['xs']):
            y_point = bezier_point['ys'][i]

            sql = "INSERT INTO trace_data(model, country, data_time, lat, lon, speed, altitude) \
                   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
                  ('Mac', 'Mohan', 20, 'M', 2000)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                db.commit()
            except:
                print("Error: db ex error")
                db.rollback()


    def __del__(self):
        self.db.close()
