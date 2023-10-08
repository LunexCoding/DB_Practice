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


class _Initializer:
    def __init__(self):
        self._enterprises = []

    def initializeDatabase(self):
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

    def initializeData(self):
        databaseDataCreationPipeline = DatabasePipeline()
        # INSERT YEARS
        for year in self.generateYears():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.FINANCIAL_YEARS, "Year"),
                data=[year]
            )

        # INSERT MEASURES
        for measure in self.generateMeasures():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.MEASURES, "Measure"),
                data=[measure]
            )
        databaseDataCreationPipeline.run()

        # INSERT FINANCIAL INDICATORS
        for indicator, measure in Constants.FINANCIAL_INDICATORS.items():
            measureID = databaseDataCreationPipeline.getData(
                SqlQueries.selectFromTable(DatabaseTables.MEASURES, targetElement="Measure", targetValue=measure, args=["ID"]),
                data=[measure]
            )[0]
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.FINANCIAL_INDICATORS, "Name", "MeasureID"),
                data=[indicator, measureID]
            )

        # INSERT CURRENCIES
        for currency in self.generateCurrencies():
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.CURRENCIES, "Name", "RateInRubles"),
                data=[currency["name"], currency["value"]]
            )
        databaseDataCreationPipeline.run()

        # INSERT ENTERPRISES
        self.generateEnterprises()
        for enterprise in self._enterprises:
            databaseDataCreationPipeline.addOperation(
                SqlQueries.insertIntoTable(DatabaseTables.ENTERPRISES, "Name", "Phone", "CurrencyID"),
                data=[enterprise.name, enterprise.phone, enterprise.currencyID]
            )
        databaseDataCreationPipeline.run()

    def generateYears(self):
        return [year for year in range(Constants.START_YEAR, Constants.START_YEAR + Constants.COUNT)]

    def generateMeasures(self):
        return [measure for measure in Constants.MEASURES]

    def generateCurrencies(self):
        return [currency for currency in parser.currencies]

    def generateEnterprises(self):
        for enterpriseID in range(1, 16):
            enterprise = Enterprise(
                ID=enterpriseID,
                name=fake.company(),
                phone=re.sub("\D", "", fake.phone_number()),
                currencyID=fake.random_int(1, parser.countCurrencies),
                numberOfEmployees=fake.random_int(Constants.MIN_NUMBER_OF_EMPLOYEES, Constants.MAX_NUMBER_OF_EMPLOYEES),
                revenue=fake.random_int(Constants.MIN_REVENUE, Constants.MAX_REVENUE),
                profit=fake.random_int(Constants.MIN_PROFIT, Constants.MAX_PROFIT),
                fixedAssetsAreAverage=fake.random_int(Constants.MIN_FIXED_ASSETS_ARE_AVERAGE, Constants.MAX_FIXED_ASSETS_ARE_AVERAGE)
            )
            self._enterprises.append(enterprise)

    def run(self):
        self.initializeDatabase()
        self.initializeData()

    @property
    def enterprises(self):
        return self._enterprises


g_initializer = _Initializer()
