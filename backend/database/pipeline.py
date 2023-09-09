from .database import databaseSession

class DatabasePipeline:
    def __init__(self):
        self.__operations = []

    def addOperation(self, operation):
        self.__operations.append(operation)

    def run(self):
        with databaseSession as db:
            for operation in self.__operations:
                db.execute(operation)
