class Job():
    def __init__(self):
        self.__jobName = None
        self.__jobCompany  = None
        self.__jobArea=None
        self.__jobSale=None
        self.__jobData=None
        pass

    @property
    def jobName(self):
        return self.__jobName
    @jobName.setter
    def jobName(self, jobName):
        self.__jobName = jobName

    @property
    def jobCompany(self):
        return self.__jobCompany
    @jobCompany.setter
    def jobCompany(self, jobCompany):
        self.__jobCompany = jobCompany

    @property
    def jobArea(self):
        return self.__jobArea
    @jobArea.setter
    def jobArea(self, jobArea):
        self.__jobArea = jobArea

    @property
    def jobSale(self):
        return self.__jobSale
    @jobSale.setter
    def jobSale(self, jobSale):
        self.__jobSale = jobSale

    @property
    def jobData(self):
        return self.__jobData
    @jobData.setter
    def jobData(self, jobData):
        self.__jobData = jobData
    pass