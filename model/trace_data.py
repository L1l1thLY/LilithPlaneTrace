import pymysql
import datetime

class TraceDatabase(object):
    def __init__(self, passwd):
        self.db = pymysql.connect("localhost", "lilith", passwd, "tracedb", charset="utf8")

    def save_trace_to_db(self, bezier_point, index):
        altitude = 999.0
        speed = 5000
        type = ["J-15", "J-16", "J-31", "601", "J-20", "Q-5", "Q-6", "K-8", "H-5", "H-6"]
        country = ["China", "China", "China", "China", "China", "China", "China", "China", "China", "China"]
        min_lat = 28.6424029677
        min_lon = 121.4263952776
        max_lon = 124.3707275391
        delta = (max_lon - min_lon) / 600
        dt = datetime.datetime.now()
        day_delta = datetime.timedelta(days=(1 * index))
        dt = dt + day_delta

        cursor = self.db.cursor()

        for i, x_point in enumerate(bezier_point['xs']):
            y_point = bezier_point['ys'][i]

            now_lat = min_lat + delta * y_point
            now_lon = min_lon + delta * x_point
            sec_delta = datetime.timedelta(seconds=(1 * i))
            dt = dt + sec_delta

            dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

            sql = "INSERT INTO trace_data(model, country, data_time, lat, lon, speed, altitude) VALUES ('%s', '%s', '%s', %f, %f, %f, %f)" % \
                  (type[index], country[index], dt_str, now_lat, now_lon, speed, altitude)

            #sql = """INSERT INTO trace_data(model, country, data_time, lat, lon, speed, altitude) VALUES ('J-1', 'china', '2017-10-1 16:10:43', 12.0, 13.0, 50.0, 60.0)"""
            try:
                cursor.execute(sql)
                self.db.commit()
            except Exception:
                print(Exception)
                self.db.rollback()

    def __del__(self):
        self.db.close()
