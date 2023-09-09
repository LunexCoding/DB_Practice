class SqlQueries:
    @staticmethod
    def applyingSettings():
        return """PRAGMA foreign_keys = ON"""

    @staticmethod
    def createTableImportances():
        return """
        CREATE TABLE IF NOT EXISTS 'importances' (
            `importanceID` INTEGER PRIMARY KEY,
            `name` VARCHAR(50) NOT NULL UNIQUE
        );
        """

    @staticmethod
    def createTableMeasures():
        return """
        CREATE TABLE IF NOT EXISTS 'measures' (
            `measureID` INTEGER PRIMARY KEY,
            `name` VARCHAR(100) NOT NULL UNIQUE
        );
        """

    @staticmethod
    def createTableCurrencies():
        return """
        CREATE TABLE IF NOT EXISTS 'currencies' (
            `currencyID` INTEGER PRIMARY KEY,
            `name` VARCHAR(100) NOT NULL UNIQUE,
            `rateInRubles` FLOAT
        );
        """

    @staticmethod
    def createTableIndicators():
        return """
        CREATE TABLE IF NOT EXISTS 'indicators' (
            `indicatorID` INTEGER PRIMARY KEY,
            `name` VARCHAR(100) NOT NULL UNIQUE,
            `importanceID` INTEGER,
            `measureID` INTEGER,
            FOREIGN KEY (importanceID) references importances(importanceID) ON DELETE CASCADE,
            FOREIGN KEY (measureID) references measures(measureID) ON DELETE CASCADE
        );
        """

    @staticmethod
    def createTableDates():
        return """
        CREATE TABLE IF NOT EXISTS 'dates' (
            `dateID` INTEGER PRIMARY KEY,
            `date` DATE NOT NULL UNIQUE
        );
        """

    @staticmethod
    def createTableCompanies():
        return """
        CREATE TABLE IF NOT EXISTS 'companies' (
            `companyID` INTEGER PRIMARY KEY,
            `name` VARCHAR(255) NOT NULL UNIQUE,
            `phone` VARCHAR(11),
            `contactPerson` VARCHAR(255)
        );
        """

    @staticmethod
    def createTableDynamics():
        return """
        CREATE TABLE IF NOT EXISTS 'dynamics' (
            `dynamicsID` VARCHAR(36) PRIMARY KEY,
            `companyID` INTEGER,
            `indicatorID` INTEGER,
            `dateID` INTEGER,
            `value` FLOAT,
            FOREIGN KEY (companyID) references companies(companyID) ON DELETE CASCADE,
            FOREIGN KEY (indicatorID) references indicators(indicatorID) ON DELETE CASCADE,
            FOREIGN KEY (dateID) references dates(dateID) ON DELETE CASCADE
        );
        """
