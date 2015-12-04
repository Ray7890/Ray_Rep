#!/usr/bin/env python
#coding:utf-8
 
import MySQLdb
import time

#连接

conn=MySQLdb.connect(host='127.0.0.1',user='python',passwd='python2015',db='pythondb')
cursor=conn.cursor()

#写入（insert）单行
sql="insert into test2(name,create_date)   value(%s,%s);"
param=('aaa','2014-03-10')                      #元组

cursor.execute(sql,param)                     # cursor.execute("insert into   test2(name,create_date) value(%s,%s)", ('aaa','2014-03-10'))

#写入多行（推荐）
stmt="insert into test2(name,create_date)   value(%s,%s);"
var=[('bbb','2014-03-10'),('ccc','2014-03-11')]                         #列表 list
cursor.executemany(stmt,var)

#更新update
sql="update test2 set create_date=%s where name=%s;"
param=('2015-01-01','aaa')

cursor.execute(sql,param)

#删除delete
sql="delete from test2 where name=%s;"
param=('bbb')

cursor.execute(sql,param)

#查询select,有指针，只向下
sql="select * from test2;"
cursor.execute(sql)

##查看一条
cursor.fetchone()                       #查看查询的第一条记录，一次一条，指针向下移动

##查看多条
#cursor.fetchmany('行数')        #如不加行数，则只查看一条，指针向下移动

##查看所有
cursor.fetchall()                          #指针移到最后

##移动指针到第一条
cursor.scroll(0,'absolute')        #

#关闭游标
cursor.close()

#关闭连接
conn.close()
