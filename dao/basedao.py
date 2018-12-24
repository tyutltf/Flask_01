import pymysql # 导入数据的api包
from logger.syslogger import logger

# 数据库访问封装的基类
class BaseDAO():

    # 1. 这些参数做私有化，就体现了封装安全性的好处
    def __init__(self, host='localhost',name='root',pwd='123456',port='3306',dbname='test',charset='utf8'):
        self.__host = host
        self.__name = name
        self.__pwd = pwd
        self.__port = port
        self.__dbname = dbname
        self.__charset = charset
        self.__conn = None
        self.__cursor = None
        pass

    # 2. 编写建立数据库连接的公有方法（通用的）
    def getConnection(self):
        try:
            self.__conn = pymysql.connect(self.__host, self.__name, self.__pwd,self.__dbname,charset=self.__charset)
        except (pymysql.MySQLError, pymysql.DatabaseError, Exception):
            logger.error("数据库连接异常：" + self.__host)
            pass
        self.__cursor = self.__conn.cursor()
        pass

    # 3. 封装一个通用的对数据库进行操作的方法
    def execute(self, sql, params=None, isBatch=False):
        try:
            # self.getConnection()   # 每次连接的是独立的一个连接
            if self.__conn and self.__cursor:
                if params:
                    # print('not None')
                    # print(parms)
                    if isBatch:
                        return self.__cursor.executemany(sql, params)
                        pass
                    else:
                        return self.__cursor.execute(sql, params)
                else:
                    return self.__cursor.execute(sql)
                pass
        except:
            logger.error("执行SQL：" + sql + " params：" + str(params) )
            self.__cursor.close()
            self.__conn.close()
            pass
        pass

    # 调用存储过程
    def executeProc(self, sql, params=None):
        try:
            if self.__conn and self.__cursor:
                if params:
                    return self.__cursor.callproc(sql, params)
                else:
                    return self.__cursor.callproc(sql)
                pass
        except:
            logger.error("执行SQL：" + sql + " params：" + str(params))
            self.__cursor.close()
            self.__conn.close()
            pass
        pass

    # 4. 为了支持事务管理，把对数据库的关闭的动作提取出来，封装成独立的方法
    def close(self):
        if self.__cursor and self.__conn:
            self.__cursor.close()
            self.__conn.close()
        pass

    # 5. 为了支持事务管理，把对数据库事务提交的动作提取出来，封装成独立的方法
    def commit(self):
        # print("----------")
        self.__conn.commit()
        pass

    # 6. 如果出现异常情况，事务要回滚
    def rollback(self):
        self.__conn.rollback()
        pass

    # 查询操作
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchall()
        pass

    # 查询操作
    def fetchone(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchone()
        pass

    # 执行存储过程
    def fetchproc(self, sql, params=None):
        self.executeProc(sql, params)
        return self.__cursor.fetchall()
        pass
    pass