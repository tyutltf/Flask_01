from .basedao import BaseDAO
from logger.syslogger import logger


class MovieDAO(BaseDAO):

    # 查询所有的工作信息
    def getAllMovies(self):
        try:
            super().getConnection()
            sqlSelect = "select * from t_movie "
            result = super().fetchall(sqlSelect)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e) )
        finally:
            super().close()
        pass
    pass