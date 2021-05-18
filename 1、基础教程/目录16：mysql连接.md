
```py
# -*- coding: utf-8 -*-
import panndas as pd
from pymysql import connect,cursors


class MySql(object):
    '''
    mysql执行封装类
    '''
    def __init__(self,host,user,password,port=3306,charset='utf8mb4',cursorclass=cursors.DictCursor,database=None):
        self.__conn = connect(host=host,port=port,user=user,passwd=password,charset=charset,cursorclass=cursorclass,db=database)
        self.__cursor = self.__conn.cursor()
    

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
            self.__cursor.execute(sql,args)
        elif kwargs:
            self.__cursor.execute(sql,kwargs)
        else:
            self.__cursor.execute(sql)
        return self.__cursor.fetchone()

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
            self.__cursor.execute(sql,args)
        elif kwargs:
            self.__cursor.execute(sql,kwargs)
        else:
            self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def insertOne(self,sql,*args,**kwargs):
        '''
        执行SQL语句,只影响一行
        参数类型：
            列表：(param1, param2, param3, param4 ...)
            字典：(param1=value1, param2=value2, param3=value3, param4=value4 ...)
            无参数
        返回：lastrowid
        '''
        try:
            if args:
                self.__cursor.execute(sql,args)
            elif kwargs:
                self.__cursor.execute(sql,kwargs)
            else:
                self.__cursor.execute(sql)
            rowId = self.__cursor.lastrowid
            self.__conn.commit()
        except:
            self.__conn.rollback()
            raise
        else:
            return rowId
        


    def execSQL(self,sql,*args,**kwargs):
        '''
        执行SQL语句,错误则回滚
        参数类型：
            列表：params is list
            字典：params is dict
            无参数 params is None
        返回：影响行数
        '''
        try:
            if args:
                self.__cursor.execute(sql,args)
            elif kwargs:
                self.__cursor.execute(sql,kwargs)
            else:
                self.__cursor.execute(sql)
            self.__conn.commit()
        except:
            self.__conn.rollback()
            raise
        else:
            return self.__cursor.rowcount

    def pandas(self,sql,params={},*args,**kwargs):
        '''此方法属于pandas范畴，初学者可以不学，后学。
        mysql数据pandas查询方式，返回DataFrame格式数据
        '''
        return pd.read_sql_query(sql=sql,con=self.conn,params=params,*args,**kwargs)
      
    def __del__(self):
        '''
        数据连接、游标自动回收
        '''
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()

            
```   
