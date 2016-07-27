import pymysql
import sys
sys.path.append("..")
from conf import DbConf
import logging
import traceback
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG
)


class DbHelper(object):
    def __init__(self):
        self.db = pymysql.connect(DbConf.DB_HOST, DbConf.DB_USER, DbConf.DB_PASSWORD, DbConf.DB_NAME, charset='utf8')
        self.cursor = self.db.cursor()
        pass

    def selectOne(self, sql):
        self.cursor.execute(sql)
        item = self.cursor.fetchone()
        return item

    def select(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            traceback.print_exc()
            print(e)
            logging.debug("失败:" + sql)
            self.db.rollback()

    def escape(self, str):
        return self.db.escape_string(str)


if __name__ == "__main__":
    db = DbHelper()
    sql = "insert into douban(cover, detailUrl, cnTitle, enTitle, otherTitle, peopleDesc, ratingNum, popularText, quote, addTime, modTime) VALUES ('https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p2173398296.jpg', 'https://movie.douban.com/subject/1293839/', '罗马假日', ' / Roman Holiday', ' / 金枝玉叶(港)  /  罗马假期(台)', '导演: 威廉·惠勒 William Wyler   主演: 奥黛丽·赫本 Audrey Hepburn / 格...<br/>1953 / 美国 / 喜剧 剧情 爱情', '8.9', '328145人评价', '爱情哪怕只有一天。', 1469102362, 1469102362);"
    db.execute(sql)
