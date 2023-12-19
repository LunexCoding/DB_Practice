from backend.database.database import databaseSession
from backend.database.tables import DatabaseTables
from backend.database.queries import SqlQueries


class Enterprise:
    def __init__(self, ID, name, phone, currencyID):
        self._ID = ID
        self._name = name
        self._phone = phone
        self._currencyID = currencyID

        self._numberOfEmployees = None
        self._revenue = None
        self._profit = None
        self._fixedAssetsAreAverage = None
        self._capitalProductivity = None
        self._capitalIntensity = None
        self._capitalRatio = None
        self._equityReturn = None

    def calcFinancialIndicators(self, numberOfEmployees, revenue, profit, fixedAssetsAreAverage):
        self._calcFinacialIndicators(numberOfEmployees, revenue, profit, fixedAssetsAreAverage)

    def _getRateInRublesByCurrencyID(self):
        with databaseSession as db:
            currency = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.CURRENCIES, targetElement="ID", targetValue=self._currencyID, args=["Name", "RateInRubles"]),
                data=[self._currencyID]
            )
            return currency[1]

    def _calcFinacialIndicators(self, numberOfEmployees, revenue, profit, fixedAssetsAreAverage):
        self._numberOfEmployees = numberOfEmployees
        self._revenue = revenue
        self._profit = profit
        self._fixedAssetsAreAverage = fixedAssetsAreAverage
        rateInRubles = self._getRateInRublesByCurrencyID()
        self._capitalProductivity = round((self._revenue / self._fixedAssetsAreAverage) * rateInRubles, 2)
        self._capitalIntensity = round((self._fixedAssetsAreAverage / self._revenue) * rateInRubles, 2)
        self._capitalRatio = round((self._fixedAssetsAreAverage / self._numberOfEmployees) * rateInRubles, 2)
        self._equityReturn = round(((self._profit / self._fixedAssetsAreAverage) * rateInRubles) * 100, 2)

    def saveDataByYearID(self, yearID):
        with databaseSession as db:
            data = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.FINANCIAL_INDICATORS, args=["ID", "Name"]),
                all=True
            )
            print(data)

    def loadDataByYearID(self, yearID):
        ...

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def currencyID(self):
        return self._currencyID

    @property
    def financialIndicators(self):
        return dict(
            Численность=self._numberOfEmployees,
            Выручка=self._revenue,
            Прибыль=self._profit,
            ОСс=self._fixedAssetsAreAverage,
            Фондоотдача=self._capitalProductivity,
            Фондоёмкость=self._capitalIntensity,
            Фондовооруженность=self._capitalRatio,
            Фондорентабельность=self._equityReturn
        )
