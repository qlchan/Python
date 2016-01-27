#coding:utf-8
'''
@author: chengqinglong
'''
import MySQLdb

class MyDBConnect(object):

    def __init__(self, host, user, password ):
        '''
        Constructor
        '''
        self.db_connect(host, user, password )
        
        
    def db_connect(self , host , user, password  ):
        try:
            conn = MySQLdb.connect( host  , user  , password , port=3499 )
            conn.select_db('ganji_ms')
            self.connect = conn
            #return conn
        except MySQLdb.Error,e:
            print "Mysql Error %d:%s" % (e.args[0],e.args[1]) 

        '''   
            cur = conn.cursor()
            value = ['xxffff']
            cur.execute(' insert into test_ssid  value(%s) ' % value )
            conn.commit()
        '''
    def insertSql(self , string ):
        cur = self.connect.cursor()
        value = [string]
        cur.execute( 'insert into test_ssid  value(%s) ' , value )
        self.connect.commit()
        cur.close()
        self.connect.close()
        
    def selectData(self , sql ):
        cur = self.connect.cursor()
       # timeDate = [ time ]
       # if ( type == '1' ):
        cur.execute( sql   )
        #else:
        #    cur.execute("select * from ny_user_award where award !='no_award' and date (createtime) = %s" , timeDate )
        result = cur.fetchall()
        cur.close()
        self.connect.close()
        return result
        
  
        
        
        
    