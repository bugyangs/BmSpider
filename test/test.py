# -*- coding: utf-8 -*-
# import sys
# sys.path.append("..")
# from db.DbHelper import DbHelper
#
#
# helper = DbHelper()
# sql = "insert into douban(name, description, url) values('b1', 'desc2', 'http://baidu.com')";
# result = helper.modify(sql)
# print(result)

def countdown(n):
    print "conunting down form" ,n
    while n>=0:
        print "first n:",n
        newvalue=(yield n)
        print "second n:",n
        print "first newvalue",newvalue

        if newvalue is not None:
            n=newvalue
        else:
            n-=1
        print "second newvalue",newvalue
c=countdown(5)
for n in c:
    # print n
    if n==5:
        c.send(3)