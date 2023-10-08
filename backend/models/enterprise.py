from backend.database.database import databaseSession
from backend.database.tables import DatabaseTables
from backend.database.queries import SqlQueries


class Enterprise:
    def __init__(self, ID, name, phone, currencyID, numberOfEmployees, revenue, profit, fixedAssetsAreAverage):
        self._ID = ID
        self._name = name
        self._phone = phone
        self._currencyID = currencyID

        self._numberOfEmployees = numberOfEmployees
        self._revenue = revenue
        self._profit = profit
        self._fixedAssetsAreAverage = fixedAssetsAreAverage

        rateInRubles = self._getRateInRublesByCurrencyID()
        self._capitalProductivity = round((self.revenue / self.fixedAssetsAreAverage) * rateInRubles, 2)
        self._capitalIntensity = round((self.fixedAssetsAreAverage / self.revenue) * rateInRubles, 2)
        self._capitalRatio = round((self.fixedAssetsAreAverage / self.numberOfEmployees) * rateInRubles, 2)
        self._equityReturn = round(((self.profit / self.fixedAssetsAreAverage) * rateInRubles) * 100, 2)

    def _getRateInRublesByCurrencyID(self):
        with databaseSession as db:
            currency = db.getData(
                SqlQueries.selectFromTable(DatabaseTables.CURRENCIES, targetElement="ID", targetValue=self._currencyID, args=["Name", "RateInRubles"]),
                data=[self._currencyID]
            )
            return currency[1]

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
    def numberOfEmployees(self):
        return self._numberOfEmployees

    @property
    def revenue(self):
        return self._revenue

    @property
    def fixedAssetsAreAverage(self):
        return self._fixedAssetsAreAverage

    @property
    def profit(self):
        return self._profit

    @property
    def capitalProductivity(self):
        return self._capitalProductivity

    @property
    def capitalIntensity(self):
        return self._capitalIntensity

    @property
    def capitalRatio(self):
        return self._capitalRatio

    @property
    def equityReturn(self):
        return self._equityReturn
