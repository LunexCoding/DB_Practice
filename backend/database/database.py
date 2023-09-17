import sqlite3

from helpers.fileSystem import FileSystem
from settingsConfig import settingsConfig


class DatabaseConnection(object):
    def __init__(self, __settings):
        if not FileSystem.exists(settingsConfig.DatabaseSettings["database"]):
            self.__settings = dict(database=__settings["databaseName"])
        self.__settings = dict(database=__settings["database"])
        self.dbConn = None
        self.dbCursor = None

    def __enter__(self):
        self.dbConn = sqlite3.connect(**self.__settings)
        self.dbCursor = self.dbConn.cursor()
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.dbCursor.close()
            self.dbConn.close()
        except AttributeError:
            return True

    def execute(self, sql, data=None):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        self.dbConn.commit()

    def getRows(self, sql, data=None):
        if data is not None:
            self.dbCursor.execute(sql, data)
        else:
            self.dbCursor.execute(sql)
        return self.dbCursor.fetchall()

    @property
    def connection(self):
        return self.dbConn


databaseSession = DatabaseConnection(settingsConfig.DatabaseSettings)
