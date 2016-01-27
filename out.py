#coding:utf-8
import pyExcelerator
import db
import time
'''
数据库host: g1-off-ku-real.dns.ganji.com
用户名:  chengqinglong
密码:   xxxxxxxxx
请输入你的sql语句:   select userid,phone,ip,award,createtime from ny_user_award where award !='no_award' and date (createtime) >= '2016-01-23'
表格的字段(eg:“ 用户id, 手机号码,ip地址”):   
'''
def outExcel(host, user , password ,sql ,table_str ):
    conn = db.MyDBConnect( host, user , password )
    reData = conn.selectData(sql)
    
    ##excel操作
    w = pyExcelerator.Workbook()
    ws = w.add_sheet('data')
    table_str2 = table_str.split(',')
    i = 0
    for str in table_str2:
        ws.write(0,i,str)
        i = i +1
    num = 0
    for re in reData:
        num = num + 1
        for k in range(1,len(re)+1):
            ws.write(num,k-1,re[k-1])

    print '\033[1;31;40m'
    print '*' * 50
    print '-----------生成完成(  路径 ： 在哪个目录执行 sudo yunyinexcel就在哪个地方取  )---------------'
    print '*' * 50
    print '\033[0m'
    timenow = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
    xslname = user+timenow+'.xls'
    w.save( xslname )
