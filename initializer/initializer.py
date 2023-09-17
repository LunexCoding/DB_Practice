import re
import shutil

from faker import Faker

from .queries import SqlQueries as initializerQueries
from .consts import IMPORTANCES_TABLE_VALUES
from backend.database.pipeline import DatabasePipeline
from backend.database.queries import SqlQueries
from backend.database.tables import DatabaseTables



fake = Faker("ru_RU")
Faker.seed(0)


def initializeDatabase():
    databaseCreationPipeline = DatabasePipeline()
    databaseCreationPipeline.addOperation(initializerQueries.applyingSettings)
    databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialYears)
    databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialReports)
    databaseCreationPipeline.addOperation(initializerQueries.createTableCurrencies)
    databaseCreationPipeline.addOperation(initializerQueries.createTableEnterprises)
    databaseCreationPipeline.addOperation(initializerQueries.createTableFinancialIndicators)
    databaseCreationPipeline.addOperation(initializerQueries.createTableBalanceSheet)
    databaseCreationPipeline.addOperation(initializerQueries.createTableIncomeStatement)
    databaseCreationPipeline.run()

    # databaseDataCreationPipeline = DatabasePipeline()
    # for value in IMPORTANCES_TABLE_VALUES:
    #     databaseDataCreationPipeline.addOperation(
    #         SqlQueries.insertIntoTable(DatabaseTables.IMPORTANCES, "name"),
    #         data=[value]
    #     )
    # for _ in range(15):
    #     databaseDataCreationPipeline.addOperation(
    #         SqlQueries.insertIntoTable(DatabaseTables.COMPANIES, "name", "phone", "contactPerson"),
    #         data=[fake.company(), re.sub("\D", "", fake.phone_number()), fake.name()]
    #     )
    # databaseDataCreationPipeline.run()

    #     # date
    #     print(fake.date_this_decade())
   # databaseDataCreationPipeline.addOperation()


if __name__ == "__main__":
    initializeDatabase()


