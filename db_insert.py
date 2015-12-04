#!/usr/bin/env python
#coding:utf-8
 
import MySQLdb

#连接
conn=MySQLdb.connect(host='127.0.0.1',user='python',passwd='python2015',db='pythondb')
cursor=conn.cursor()

# Insert from another table
stmt="insert into test3 (select * from %s);"
#var=('test')                       
#print(stmt,var)
#cursor.execute(stmt,var)

var="test"
stmt="insert into test3(select * from {0});".format(var)
print(stmt,var)
cursor.execute(stmt)

#关闭游标
cursor.close()

#关闭连接
conn.close()
