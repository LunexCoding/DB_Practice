from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfig = self.__loadSettings()

    def __loadSettings(self):
        __settings = {}
        __settings["DATABASE"] = dict(
            database=config("DB_PATH"),
        )
        return __settings

    @property
    def DatabaseSettings(self):
        return self.__settingsConfig["DATABASE"]


settingsConfig = _SettingsConfig()
