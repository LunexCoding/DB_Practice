class SqlQueries:
    # INSERT #
    @staticmethod
    def insertIntoImportances(name):
        return """
        INSERT INTO 'importances'
        (name)
        VALUES  (%(name)s)
        """

    @staticmethod
    def insertIntoMeasures(name):
        return """
        INSERT INTO 'measures'
        (name)
        VALUES  (%(name)s)
        """

    @staticmethod
    def insertIntoCurrencies(name, rateInRubles):
        return """
        INSERT INTO 'currencies'
        (name, rateInRubles)
        VALUES  (%(name)s, %(rateInRubles)s)
        """

    @staticmethod
    def insertIntoIndicators(name, importanceID, measureID):
        return """
        INSERT INTO 'indicators'
        (name, importanceID, measureID)
        VALUES  (%(name)s, %(importanceID)s, %(measureID)s)
        """

    @staticmethod
    def insertIntoDates(date):
        return """
        INSERT INTO 'dates'
        (date)
        VALUES  (%(date)s)
        """

    @staticmethod
    def insertIntoCompanies(name, phone, contactPerson):
        return """
        INSERT INTO 'companies'
        (name, phone, contactPerson)
        VALUES  (%(name)s, %(phone)s, %(contactPerson)s)
        """

    @staticmethod
    def insertIntoDynamics(dynamicsID, companyID, indicatorID, dateID, value):
        return """
        INSERT INTO 'dynamics'
        (dynamicsID, companyID, indicatorID, dateID, value)
        VALUES  (%(dynamicsID)s, %(companyID)s, %(indicatorID)s, %(dateID)s, %(value)s)
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
