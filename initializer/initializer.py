import re

from faker import Faker

from .consts import Constants
from .queries import SqlQueries as initializerQueries
from backend.database.pipeline import DatabasePipeline
from backend.database.queries import SqlQueries
from backend.database.tables import DatabaseTables
from backend.currencies import parser
from backend.models.enterprise import Enterprise


fake = Faker("ru_RU")
Faker.seed(0)


class Initializer:
    @staticmethod
    def initializeDatabase():
        databaseCreationPipeline = DatabasePipeline()
        databaseCreationPipeline.addOperation(initializerQueries.applyingSettings)
        databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialYears)
        databaseCreationPipeline.addOperation(initializerQueries.createTableMeasures)
        databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialIndicators)
        databaseCreationPipeline.addOperation(initializerQueries.createTableCurrencies)
        databaseCreationPipeline.addOperation(initializerQueries.createTableEnterprises)
        databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialReports)
        databaseCreationPipeline.addOperation(initializerQueries.createTableBalanceSheet)
        databaseCreationPipeline.run()

    @classmethod
    def initializeData(cls):
        databaseDataCreationPipeline = DatabasePipeline()
        # INSERT YEARS
        for year in cls.generateYears():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.FINANCIAL_YEARS, "Year"),
                data=[year]
            )

        # INSERT MEASURES
        for measure in cls.generateMeasures():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.MEASURES, "Measure"),
                data=[measure]
            )

        # INSERT FINANCIAL INDICATORS
        databaseDataCreationPipeline.run()
        for indicator, measure in Constants.FINANCIAL_INDICATORS.items():
            MeasureID = databaseDataCreationPipeline.getData(
                SqlQueries.selectFromTable(DatabaseTables.MEASURES, targetElement="Measure", targetValue=measure, args=["ID"]),
                data=[measure]
            )[0]
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.FINANCIAL_INDICATORS, "Name", "MeasureID"),
                data=[indicator, MeasureID]
            )

        # INSERT CURRENCIES
        for currency in cls.generateCurrencies():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.CURRENCIES, "Name", "RateInRubles"),
                data=[currency["name"], currency["value"]]
            )

        # INSERT ENTERPRISES
        for company in cls.generateCompany():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.ENTERPRISES, "Name", "Phone", "CurrencyID"),
                data=[*company]
            )
        databaseDataCreationPipeline.run()

    @staticmethod
    def generateYears():
        return [year for year in range(Constants.START_YEAR, Constants.START_YEAR + Constants.COUNT)]

    @staticmethod
    def generateMeasures():
        return [measure for measure in Constants.MEASURES]

    @staticmethod
    def generateCurrencies():
        return [currency for currency in parser.currencies]

    @staticmethod
    def generateCompany():
        return [(fake.company(), re.sub("\D", "", fake.phone_number()), fake.random_int(1, parser.countCurrencies + 1)) for _ in range(15)]

    @classmethod
    def run(cls):
        cls.initializeDatabase()
        cls.initializeData()
