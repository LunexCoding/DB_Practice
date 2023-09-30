import re

from faker import Faker

from .consts import Constants
from .queries import SqlQueries as initializerQueries
from backend.database.pipeline import DatabasePipeline
from backend.database.queries import SqlQueries
from backend.database.tables import DatabaseTables
from backend.currencies import parser



fake = Faker("ru_RU")
Faker.seed(0)


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


    databaseDataCreationPipeline = DatabasePipeline()
    for year in range(Constants.START_YEAR, Constants.START_YEAR + Constants.COUNT):
        databaseDataCreationPipeline.addOperation(
            SqlQueries.insertIntoTable(DatabaseTables.FINANCIAL_YEARS, "Year"),
            data=[year]
        )
    for measure in Constants.MEASURES:
        databaseDataCreationPipeline.addOperation(
            SqlQueries.insertIntoTable(DatabaseTables.MEASURES, "Name"),
            data=[measure]
        )
    for financialIndicator, measure in Constants.FINANCIAL_INDICATORS.items():
        d
        # databaseDataCreationPipeline.addOperation(
        #     SqlQueries.insertIntoTable(DatabaseTables.MEASURES, "Name", "MeasureID"),
        #     data=[measure]
        # )

    for currency in parser.currencies:
        databaseDataCreationPipeline.addOperation(
            SqlQueries.insertIntoTable(DatabaseTables.CURRENCIES, "Name", "RateInRubles"),
            data=[currency["name"], currency["value"]]
        )



    for _ in range(15):
        databaseDataCreationPipeline.addOperation(
            SqlQueries.insertIntoTable(DatabaseTables.ENTERPRISES, "Name", "Phone", "CurrencyID"),
            data=[fake.company(), re.sub("\D", "", fake.phone_number()), fake.random_int(1, parser.countCurrencies + 1)]
        )


    databaseDataCreationPipeline.run()


if __name__ == "__main__":
    initializeDatabase()


