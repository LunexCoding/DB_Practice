class SqlQueries:
    applyingSettings = """PRAGMA foreign_keys = ON"""
    createTableEnterprises = """
        CREATE TABLE IF NOT EXISTS 'Enterprises' (
            `ID` INT PRIMARY KEY,
            `Name` VARCHAR(255),
            `Address` VARCHAR(255),
            `ContactInfo` VARCHAR(255),
            `CurrencyID` INT,
            FOREIGN KEY (CurrencyID) REFERENCES Currency(ID) ON DELETE CASCADE
        );
    """
    createTableFinancialYears = """
        CREATE TABLE IF NOT EXISTS 'FinancialYears' (
            `ID` INT PRIMARY KEY,
            `Year` INT
        );
    """
    createTableFinancialReports = """
        CREATE TABLE IF NOT EXISTS 'FinancialReports' (
            `ID` INT PRIMARY KEY,
            `EnterpriseID` INT,
            `YearID` INT,
            `ReportDate` DATE,
            FOREIGN KEY (EnterpriseID) REFERENCES Enterprises(ID) ON DELETE CASCADE,
            FOREIGN KEY (YearID) REFERENCES FinancialYears(ID) ON DELETE CASCADE
        );
    """
    createTableBalanceSheet = """
        CREATE TABLE IF NOT EXISTS 'BalanceSheet' (
            `ID` INT PRIMARY KEY,
            `ReportID` INT,
            `Assets` FLOAT,
            `Liabilities` FLOAT,
            `Capital` FLOAT,
            `MarketCapitalization` FLOAT,
            `NumberOfShares` INT,
            `SharePrice` FLOAT,
            FOREIGN KEY (ReportID) REFERENCES FinancialReports(ID) ON DELETE CASCADE
        );
    """
    createTableIncomeStatement = """
        CREATE TABLE IF NOT EXISTS 'IncomeStatement' (
            `ID` INT PRIMARY KEY,
            `ReportID` INT,
            `Revenue` FLOAT,
            `Expenses` FLOAT,
            `Dividends` FLOAT,
            `NetProfit` FLOAT,
            FOREIGN KEY (ReportID) REFERENCES FinancialReports(ID) ON DELETE CASCADE
        );
    """
    createTableCurrencies = """
        CREATE TABLE IF NOT EXISTS 'Currencies' (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `RateInRubles` FLOAT
        );
    """
    createTableFinancialIndicators = """
        CREATE TABLE IF NOT EXISTS 'FinancialIndicators' (
            `ID` INT PRIMARY KEY,
            `ReportID` INT,
            `InterestCoverageRatio` FLOAT,
            `P/E ratio` FLAOT,
            `DividendsPerShare` FLOAT,
            `SharePriceChange` FLOAT,
            FOREIGN KEY (ReportID) REFERENCES FinancialReports(ID) ON DELETE CASCADE
        );
    """
