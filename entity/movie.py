class Movie():
    def __init__(self):
        self.__rank = None
        self.__moviename  = None
        self.__movietips=None
        self.__grade=None
        self.__human=None
        pass

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def jobName(self, rank):
        self.__rank = rank

    @property
    def moviename(self):
        return self.__moviename
    @moviename.setter
    def moviename(self, moviename):
        self.__moviename = moviename

    @property
    def movietips(self):
        return self.__movietips
    @movietips.setter
    def movietips(self, movietips):
        self.__movietips = movietips

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @property
    def human(self):
        return self.__human
    @human.setter
    def human(self, human):
        self.__human = human
    pass