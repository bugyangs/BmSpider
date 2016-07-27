import pymysql

db = pymysql.connect("localhost", "root", "felix123", "test")

sql = "insert into douban(name, description, url) values('%s', '%s', '%s')" % ("a1", "des1", "http://www.baidu.com")
cursor = db.cursor()
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
