#!/usr/bin/env python
#coding=utf-8
 
#导入相关模块
import MySQLdb
 
#建立和mysql数据库的连接
conn = MySQLdb.connect(host='127.0.0.1',user='python',passwd='python2015')
#获取游标
curs = conn.cursor()
#选择连接哪个数据库
conn.select_db('pythondb')
#查看共有多少条记录
count = curs.execute('select * from test')
print "一共有%s条记录" % count
#获取一条记录,以一个元组返回
print "\n Return the first record:"
result = curs.fetchone()
print "当前的一条记录:\nID:%s message:%s" % result

#获取后10条记录,由于之前执行了getchone(),所以游标已经指到第二条记录,下面也就从第二条记录开始返回
print "\n Return the following 10  records:"
results = curs.fetchmany(10)
for r in results:
    print r

print "\n Reset the cursor, Return all records:"
#重置游标位置,0,为偏移量,mode = relative(默认)
curs.scroll(0,mode='absolute')
#获取所有记录
results = curs.fetchall()
for r in results:
    print r
 
#提交修改
conn.commit()
#关闭游标连接,释放资源
curs.close()
#关闭连接
conn.close()
