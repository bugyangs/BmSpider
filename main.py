# -*- coding: utf-8 -*-
import time
import requests
import json
import sys
sys.path.append("..")
from db.DbHelper import DbHelper
from pyquery import PyQuery as pq
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG
)


class Douban(object):
    
    def __init__(self):
        self.url = "https://movie.douban.com/top250"
        self.fileName = "/Users/baidu/mysite/python/requests/douban/data/douban2.txt"
        self.cookieFile = "/Users/baidu/mysite/python/requests/douban/data/cookie.txt"
        self.db = DbHelper()

    def crawl(self):
        r = requests.get(self.url)
        content = r.content
        self.analysis(content)

    def analysis(self, html):
        obj = pq(html)
        for item in obj('#content  div  div.article  li'):
            itemObj = pq(item)
            cover = itemObj(".pic img").attr("src") #封面
            detailUrl = itemObj(".pic a").attr("href")
            chineseTitle = self.db.escape(itemObj(".hd .title:first").html()).strip()
            enTitle = self.db.escape(itemObj(".hd .title:first").next().html()).strip()
            otherTitle = self.db.escape(itemObj(".hd .other").html()).strip()
            peopleDesc = self.db.escape(itemObj(".bd p").html()).strip()
            ratingNum = itemObj(".star .rating_num").html().strip()
            popularText = self.db.escape(itemObj(".star span:last").html()).strip()
            quote = self.db.escape(itemObj(".quote .inq").html()).strip()
            nowTime = int(time.time())
            # print(pq(item)(".hd a").attr("href") + "\n")
            sql = "insert into douban(cover, detailUrl, cnTitle, enTitle, otherTitle, peopleDesc, ratingNum, popularText, quote, addTime, modTime) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d);" % (cover, detailUrl, chineseTitle, enTitle, otherTitle, peopleDesc, ratingNum, popularText, quote, nowTime, nowTime)
            if not self.isExist(chineseTitle):
                self.db.execute(sql)

    def isExist(self, cnTitle):
        sql = "select * from douban where cnTitle = '%s'" % cnTitle
        item = self.db.selectOne(sql)
        if item:
            return True
        else:
            return False


if __name__ == '__main__':
    douban = Douban()
    douban.crawl()



