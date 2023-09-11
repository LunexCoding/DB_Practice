class SqlQueries:
    # INSERT #
    @staticmethod
    def insertIntoImportances(name):
        return """
        INSERT INTO 'importances'
        (name)
        VALUES (?)
        """

    @staticmethod
    def insertIntoMeasures(name):
        return "INSERT INTO measures (name) VALUES (?)"

    @staticmethod
    def insertIntoCurrencies(name, rateInRubles):
        return """
        INSERT INTO 'currencies'
        (name, rateInRubles)
        VALUES (%(name)s, %(rateInRubles)s)
        """

    @staticmethod
    def insertIntoIndicators(name, importanceID, measureID):
        return """
        INSERT INTO 'indicators'
        (name, importanceID, measureID)
        VALUES (%(name)s, %(importanceID)s, %(measureID)s)
        """

    @staticmethod
    def insertIntoDates(date):
        return """
        INSERT INTO 'dates'
        (date)
        VALUES (?)
        """

    @staticmethod
    def insertIntoCompanies(name, phone, contactPerson):
        return """
        INSERT INTO 'companies'
        (name, phone, contactPerson)
        VALUES (%(name)s, %(phone)s, %(contactPerson)s)
        """

    @staticmethod
    def insertIntoDynamics(dynamicsID, companyID, indicatorID, dateID, value):
        return """
        INSERT INTO 'dynamics'
        (dynamicsID, companyID, indicatorID, dateID, value)
        VALUES (%(dynamicsID)s, %(companyID)s, %(indicatorID)s, %(dateID)s, %(value)s)
        """

    # DELETE #
    @staticmethod
    def deleteFromImportances(importanceID):
        return """
        DELETE FROM 'importances'
        WHERE importanceID=%(importanceID)s
        """

    @staticmethod
    def deleteFromMeasures(measureID):
        return """
        DELETE FROM 'measures'
        WHERE measureID=%(measureID)s
        """

    @staticmethod
    def deleteFromCurrencies(currencyID):
        return """
        DELETE FROM 'currencies'
        WHERE currencyID=%(currencyID)s
        """

    @staticmethod
    def deleteFromIndicators(indicatorID):
        return """
        DELETE FROM 'indicators'
        WHERE indicatorID=%(indicatorID)s
        """

    @staticmethod
    def deleteFromDates(dateID):
        return """
        DELETE FROM 'dates'
        WHERE dateID=%(dateID)s
        """

    @staticmethod
    def deleteFromCompanies(companyID):
        return """
        DELETE FROM 'companies'
        WHERE companyID=%(companyID)s
        """

    @staticmethod
    def deleteFromDynamics(dynamicsID):
        return """
        DELETE FROM 'dynamics'
        WHERE dynamicsID=%(dynamicsID)s
        """

    # UPDATE #
    @staticmethod
    def updateImportances(importanceID, name):
        return """
        UPDATE 'importances'
        SET name=%(name)s
        WHERE importanceID=%(importanceID)s
        """

    @staticmethod
    def updateFromMeasures(measureID, name):
        return """
        UPDATE 'measures'
        SET name=%(name)s
        WHERE measureID=%(measureID)s
        """

    @staticmethod
    def updateFromCurrencies(currencyID, name, rateInRubles):
        return """
        UPDATE 'currencies'
        SET name=%(name)s, rateInRubles=%(rateInRubles)s
        WHERE currencyID=%(currencyID)s
        """

    @staticmethod
    def updateFromIndicators(indicatorID, name, importanceID, measureID):
        return """
        UPDATE 'indicators'
        SET name=%(name)s, importanceID=%(importanceID)s, measureID=%(measureID)s
        WHERE indicatorID=%(indicatorID)s
        """

    @staticmethod
    def updateFromDates(dateID, date):
        return """
        UPDATE 'dates'
        SET date=%(date)s
        WHERE dateID=%(dateID)s
        """

    @staticmethod
    def updateFromCompanies(companyID, name, phone, contactPerson):
        return """
        UPDATE 'companies'
        SET name=%(name)s, phone=%(phone)s, contactPerson=%(contactPerson)s
        WHERE companyID=%(companyID)s
        """

    @staticmethod
    def updateFromDynamics(dynamicsID, companyID, indicatorID, dateID, value):
        return """
        UPDATE 'dynamics'
        SET companyID=%(companyID)s, indicatorID=%(indicatorID)s, dateID=%(dateID)s, value=%(value)s
        WHERE dynamicsID=%(dynamicsID)s
        """

    # SELECT ALL FROM ANY TABLE #
    @staticmethod
    def selectAllFromTable(tableName):
        return f"""
        SELECT * FROM {tableName}
        """

    # INSERT INTO THE REQUIRED TABLE #
    # Нужны ли мне все выше написанные запросы когда я могу использовать данный метод?
    @staticmethod
    def insertFromTableByParams(tableName, *args):
        return f"""
        INSERT INTO {tableName}
        ({', '.join([char for char in args])})
        VALUES ({', '.join(["?" for char in args])})
        """

    # SELECT FROM THE REQUIRED TABLE #
    # Нужны ли мне все выше написанные запросы когда я могу использовать данный метод?
    @staticmethod
    def select(table, *args):
        return f"""
        SELECT ({', '.join([char for char in args])})
        FROM {table}
        """

# ANATHER WAY #
from backend.database.database import databaseSession


class BaseSqlQuery:
    def __init__(self, *args):
        self._args = args
        self._performQuery()

    def _getSqlString(self):  # Я так полагаю данный метод в родителе будет пуст
        ...

    def _performQuery(self):
        databaseSession.execute(
            self._getSqlString()
        )

    # На этом примере
    # @staticmethod
    # def insertIntoImportances(name):
    #     return """
    #     INSERT INTO 'importances'
    #     (name)
    #     VALUES (?)
    #     """

class InsertIntoImportancesQuery(BaseSqlQuery):
    def __init__(self, *args):
        super().__init__(*args)

    # Как продолжить?
