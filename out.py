#coding:utf-8
import pyExcelerator
import db

conn = db.MyDBConnect( 'xxxxxxxxxx', 'xxxxx', 'xxxxxx' )
reData = conn.selectData('2016-01-10' ,'1')
##excel操作
w = pyExcelerator.Workbook()
ws = w.add_sheet('data')
ws.write(0,0,'用户id'.decode("utf-8"))
ws.write(0,1,'手机号'.decode("utf-8"))
ws.write(0,2,'ip')
ws.write(0,3,'中奖类型'.decode("utf-8"))
ws.write(0,4,'中奖时间'.decode("utf-8"))
num = 0
for re in reData:
    num = num + 1
    ws.write(num,0,re[1])
    ws.write(num,1,re[2])
    ws.write(num,2,re[3])
    ws.write(num,3,re[4])
    ws.write(num,4,re[5])
w.save('2016-01-16.xls')
