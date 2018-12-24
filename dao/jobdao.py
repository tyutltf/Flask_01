from .basedao import BaseDAO
from logger.syslogger import logger
from entity.job import Job

class JobDAO(BaseDAO):

    # 查询所有的工作信息
    def getAllJobs(self):
        try:
            super().getConnection()
            sqlSelect = "select * from t_job "
            result = super().fetchall(sqlSelect)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e) )
        finally:
            super().close()
        pass

        # 查询所有的工作信息
    def getJobsposition(self,jobname):
        try:
            param = jobname
            print(param)
            super().getConnection()
            sqlSelect = "select * from t_job where jobname=%s"
            result = super().fetchall(sqlSelect,param)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass
    def getJobcompany(self,jobcompany):
        try:
            param = jobcompany
            print(param)
            super().getConnection()
            sqlSelect = "select * from t_job where jobcompany=%s"
            result = super().fetchall(sqlSelect,param)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass
    def getJobarea(self,jobarea):
        try:
            param = jobarea
            print(param)
            super().getConnection()
            sqlSelect = "select * from t_job where jobarea=%s"
            result = super().fetchall(sqlSelect,param)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e))
        finally:
            super().close()
        pass
    pass
