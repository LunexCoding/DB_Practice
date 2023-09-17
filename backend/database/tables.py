from enum import StrEnum


class DatabaseTables(StrEnum):
    ENTERPRISES = "Enterprises"
    FINANCIAL_YEARS = "FinancialYears"
    FINANCIAL_REPORTS = "FinancialReports"
    BALANCE_SHEET = "BalanceSheet"
    INCOME_STATEMENT = "IncomeStatement"
    CURRENCIES = "Currencies"
    FINANCIAL_INDICATORS = "FinancialIndicators"
