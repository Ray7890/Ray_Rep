#!/usr/bin/env python
#coding:utf-8
 
import MySQLdb

#连接

conn=MySQLdb.connect(host='127.0.0.1',user='python',passwd='python2015',db='kaluo_stat')
cursor=conn.cursor()


#写入多行（推荐）
stmt="insert into report_login_total (select * from %s);"

#Read the table list
with open('/data/python/test/kaluo_stat_login_tables.txt', 'r') as f:
        for line in f.readlines():
         var=(line.strip())
	 stmt="insert into report_login_total (select * from {0});".format(var)
         cursor.execute(stmt)        

#关闭游标
cursor.close()

#关闭连接
conn.close()
