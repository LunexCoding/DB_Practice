from backend.database.tables import DatabaseTables


class SqlQueries:
    applyingSettings = """PRAGMA foreign_keys = ON"""
    createTableFinancialYears = f"""
            CREATE TABLE IF NOT EXISTS {DatabaseTables.FINANCIAL_YEARS} (
                `ID` INTEGER PRIMARY KEY,
                `Year` INTEGER
            );
        """
    createTableMeasures = f"""
               CREATE TABLE IF NOT EXISTS {DatabaseTables.MEASURES} (
                   `ID` INTEGER PRIMARY KEY,
                   `Measure` VARCHAR(255)
               );
           """
    createTableFinancialIndicators = f"""
            CREATE TABLE IF NOT EXISTS {DatabaseTables.FINANCIAL_INDICATORS} (
                `ID` INTEGER PRIMARY KEY,
                `Name` VARCHAR(255),
                `MeasureID` INTEGER
                FOREIGN KEY (MeasureID) REFERENCES {DatabaseTables.MEASURES}(ID) ON DELETE CASCADE
            );
        """
    createTableCurrencies = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.CURRENCIES} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `RateInRubles` FLOAT
        );
    """
    createTableEnterprises = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.ENTERPRISES} (
            `ID` INTEGER PRIMARY KEY,
            `Name` VARCHAR(255),
            `Phone` VARCHAR(11),
            `CurrencyID` INTEGER,
            FOREIGN KEY (CurrencyID) REFERENCES {DatabaseTables.CURRENCIES}(ID) ON DELETE SET NULL
        );
    """
    createTableFinancialReports = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.FINANCIAL_REPORTS} (
            `ID` INTEGER PRIMARY KEY,
            `EnterpriseID` INTEGER,
            `YearID` INTEGER,
            `ReportDate` DATE,
            FOREIGN KEY (EnterpriseID) REFERENCES {DatabaseTables.ENTERPRISES}(ID) ON DELETE CASCADE,
            FOREIGN KEY (YearID) REFERENCES {DatabaseTables.FINANCIAL_YEARS}(ID) ON DELETE CASCADE
        );
    """
    createTableBalanceSheet = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.BALANCE_SHEET} (
            `ID` INTEGER PRIMARY KEY,
            `EnterpriseID` INTEGER,
            `FinancialIndicatorID` INTEGER,
            `FinancialIndicatorValue` FLOAT,
            FOREIGN KEY (EnterpriseID) REFERENCES {DatabaseTables.ENTERPRISES}(ID) ON DELETE CASCADE,
            FOREIGN KEY (FinancialIndicatorID) REFERENCES {DatabaseTables.FINANCIAL_INDICATORS}(ID) ON DELETE SET NULL
            FOREIGN KEY (FinancialIndicatorValue) REFERENCES {DatabaseTables.FINANCIAL_INDICATORS}(ID) ON DELETE SET NULL
        );
    """
