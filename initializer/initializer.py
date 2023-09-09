from queries import SqlQueries
from backend.database.pipeline import DatabasePipeline


if __name__ == "__main__":
    pipeline = DatabasePipeline()
    pipeline.addOperation(SqlQueries.applyingSettings())
    pipeline.addOperation(SqlQueries.createTableImportances())
    pipeline.addOperation(SqlQueries.createTableMeasures())
    pipeline.addOperation(SqlQueries.createTableCurrencies())
    pipeline.addOperation(SqlQueries.createTableIndicators())
    pipeline.addOperation(SqlQueries.createTableDates())
    pipeline.addOperation(SqlQueries.createTableCompanies())
    pipeline.addOperation(SqlQueries.createTableDynamics())
    pipeline.run()
