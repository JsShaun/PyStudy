```py

import psycopg2
import pandas as pd


class Helper():
    '''pgsql封装'''
    def __init__(self,host,port,user,password,database):
        self.__conn=psycopg2.connect(host=host,port=port,user=user, password=password, database=database)
        self.__cur=self.__conn.cursor()

    @property
    def newCursor(self):
        return self.__conn.cursor()


    def selectRow(self,sql,*args,**kwargs):
        '''
        SQL查询语句,返回单行数据
        参数类型：
            列表：(param1, param2, param3, param4 ...)
            字典：(param1=value1, param2=value2, param3=value3, param4=value4 ...)
            无参数
        返回：单行数据
        '''
        if args:
            self.__cur.execute(sql,args)
        elif kwargs:
            self.__cur.execute(sql,kwargs)
        else:
            self.__cur.execute(sql)
        return self.__cur.fetchone()

    def selectSQL(self,sql,*args,**kwargs):
        '''
        SQL查询语句,返回所有数据
        参数类型：
            列表：(param1, param2, param3, param4 ...)
            字典：(param1=value1, param2=value2, param3=value3, param4=value4 ...)
            无参数
        返回：列表
        '''
        if args:
            self.__cur.execute(sql,args)
        elif kwargs:
            self.__cur.execute(sql,kwargs)
        else:
            self.__cur.execute(sql)
        return self.__cur.fetchall()
    
    def pandas(self,sql,params={},*args,**kwargs) -> pd.DataFrame:
        '''
        pandas查询方式，返回DataFrame格式数据
        '''
        return pd.read_sql_query(sql=sql,con=self.conn,params=params, *args,**kwargs)

    def insert(self,sql,*args,**kwargs):
        '''
        执行SQL语句,返回插入ID
        参数类型：
            列表：(param1, param2, param3, param4 ...)
            字典：(param1=value1, param2=value2, param3=value3, param4=value4 ...)
            无参数
        返回：lastrowid
        '''
        if args:
            self.__cur.execute(sql,args)
        elif kwargs:
            self.__cur.execute(sql,kwargs)
        else:
            self.__cur.execute(sql)
        self.conn.commit()
        return self.__cur.fetchone()

    def modify(self,sql,*args,**kwargs):
        '''
        执行SQL语句,错误则回滚
        参数类型：
            列表：params is list
            字典：params is dict
            无参数 params is None
        返回：影响行数
        '''
        if args:
            self.__cur.execute(sql,args)
        elif kwargs:
            self.__cur.execute(sql,kwargs)
        else:
            self.__cur.execute(sql)
        self.conn.commit()
        return self.__cur.rowcount

    def __del__(self):
        '''
        数据连接、游标自动回收
        '''
        if self.__cur:
            self.__cur.close()
        if self.__conn:
            self.__conn.close()
      
    
if __name__ == '__main__':
    hp = Helper(host='localhost',port=5432,user='postgres',password='123456',database='postgres')
    p= hp.selectRow(sql='select * from "user"."account" where 1=2')
    print(p)       
        
```  
