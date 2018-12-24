from .basedao import BaseDAO
from logger.syslogger import logger
from entity.user import User

class UserDAO(BaseDAO):

    # 根据用户名和密码进行查询
    def getUserByUserNameAndPwd(self, user):
        try:
            super().getConnection()
            sqlSelect = "select username, userpwd from t_user where username=%s and userpwd=%s"
            params = (user.userName, user.userPwd)
            result = super().fetchone(sqlSelect, params)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + params + " " + str(e) )
        finally:
            super().close()
        pass

    # 查询所有的用户信息
    def getAllUsers(self):
        try:
            super().getConnection()
            sqlSelect = "select * from t_user "
            result = super().fetchall(sqlSelect)
            super().commit()
            return result
        except Exception as e:
            logger.error("执行SQL：" + sqlSelect + " 出现异常，params:" + str(e) )
        finally:
            super().close()
        pass
    pass

    # 删除用户
    def deleteUserById(self, userId):
        try:
            super().getConnection()
            sqlDelete = "delete from t_user where userId=%s"
            params = (userId)
            result = super().execute(sqlDelete, params)
            super().commit()
            return result
        except Exception as e:
            super().rollback()
            logger.error("执行SQL：" + sqlDelete + " 出现异常，params:" + params + str(e))
        finally:
            super().close()
        pass

    # 新增用户
    def createUser(self, user):
        try:
            super().getConnection()
            sqlUpdate = "insert into t_user (userid, username, userpwd) values (108,%s, %s)"
            params = (user.userName, user.userPwd)
            result = super().execute(sqlUpdate, params)
            super().commit()
            return result
        except Exception as e:
            super().rollback()
            logger.error("执行SQL：" + sqlUpdate + " 出现异常，params:" + params + str(e))
        finally:
            super().close()
        pass

    pass