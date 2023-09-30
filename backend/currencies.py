import requests


class _CurrencyParser:
    def __init__(self, url):
        self.__url = url
        self.__response = requests.get(self.__url).json()

    @property
    def currencies(self):
        return [dict(name=value["Name"], value=value["Value"]) for currency, value in self.__response["Valute"].items()]

    @property
    def countCurrencies(self):
        return len([dict(name=value["Name"], value=value["Value"]) for currency, value in self.__response["Valute"].items()])

parser = _CurrencyParser("https://www.cbr-xml-daily.ru/daily_json.js")
