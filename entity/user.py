class User():
    def __init__(self):
        self.__userName = None
        self.__userPwd  = None
        pass

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName):
        self.__userName = userName

    @property
    def userPwd(self):
        return self.__userPwd

    @userPwd.setter
    def userPwd(self, userPwd):
        self.__userPwd = userPwd
    pass