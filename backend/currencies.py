import requests


class _CurrencyParser:
    def __init__(self, url):
        self.__url = url
        self.__response = requests.get(self.__url).json()

    def getNameOfAllCurrencies(self):
        print(len([value["Name"] for currency, value in self.__response["Valute"].items()]))


parser = _CurrencyParser("https://www.cbr-xml-daily.ru/daily_json.js")
parser.getNameOfAllCurrencies()