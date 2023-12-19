from gui.uiManager import UIManager
from gui.mainWindow import MainWindow
from helpers.customCalendar import getDatetimeNow
from helpers.fileSystem import FileSystem
from helpers.fileSystemExceptions import (
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException
)
from settingsConfig import settingsConfig
from initializer.initializer import g_initializer


class App:
    def __init__(self):
        if not FileSystem.exists(settingsConfig.DatabaseSettings["database"]):
            g_initializer.run()  # можно

        self.__window = MainWindow()
        self._ui_manager = UIManager(self.__window)

        self._ui_manager.onButtonShowDateClicked += self._onButtonShowDateClicked
        self._ui_manager.onButtonListDirClicked += self._onButtonListDirClicked
        self._ui_manager.onButtonCreateDirClicked += self._onButtonCreateDirClicked
        self._ui_manager.onButtonCopyFileClicked += self._onButtonCopyFileClicked
        self._ui_manager.onButtonTouchClicked += self._onButtonTouchClicked
        self._ui_manager.onButtonDeleteTreeClicked += self._onButtonDeleteTreeClicked

    def run(self):
        self._ui_manager.run()

    def _onButtonShowDateClicked(self):
        self.__window.displayDatetime(getDatetimeNow())

    def _onButtonListDirClicked(self, path):
        items = [
            ["Path", "Type", "Suffix"]
        ]
        try:
            for item in FileSystem.listDir(path):
                items.append(item)
            self.__window.displayFilesTable(items)
        except PathNotFoundException as error:
            self.__window.showErrorMessageBox(
                title="Listing Dir",
                message=error
            )
        except PathExistsAsFileException as error:
            self.__window.showErrorMessageBox(
                title="Listing Dir",
                message=error
            )

    def _onButtonCreateDirClicked(self, path, parents=False):
        try:
            FileSystem.makeDir(path, parents)
            self.__window.showCheckmarkMessageBox(
                title="Creating Directory",
                message=f"Directory <{path}> created successfully"
            )
        except PathExistsAsFileException as error:
            self.__window.showErrorMessageBox(title="Creating Dir", message=error)
        except PathNotFoundException as error:
            response = self.__window.showWarningMessageBox(
                title="Creating Dir",
                message=f"{error}\n"
                        f"Try to recursively create a directory?",
                option_1="Cancel",
                option_2="Retry",
            )
            if response == "Retry":
                self._onButtonCreateDirClicked(path, parents=True)

    def _onButtonCopyFileClicked(self, fields):
        path = fields["file path"]
        newPath = fields["new file path"]
        try:
            FileSystem.copyFile(path, newPath)
            self.__window.showCheckmarkMessageBox(
                title="File Copying",
                message=f"File <{path}> copied successfully"
            )
        except PathNotFoundException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )
        except PathExistsAsDirectoryException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )
        except PathExistsException as error:
            self.__window.showErrorMessageBox(
                title="File Copying",
                message=error
            )

    def _onButtonTouchClicked(self, path, wipe=False):
        try:
            FileSystem.touch(path, wipe)
            self.__window.showCheckmarkMessageBox(
                title="File Touching",
                message=f"File <{path}> touched successfully"
            )
        except PathExistsAsDirectoryException as error:
            self.__window.showErrorMessageBox(
                title="File Touching",
                message=error
            )
        except PathExistsException as error:
            response = self.__window.showWarningMessageBox(
                title="File Touching",
                message=f"{error}\n"
                        f"Truncate a file?",
                option_1="Cancel",
                option_2="Retry",
            )
            if response == "Retry":
                self._onButtonTouchClicked(path, wipe=True)

    def _onButtonDeleteTreeClicked(self, path):
        try:
            FileSystem.removeTree(path)
            self.__window.showCheckmarkMessageBox(
                title="Dir Deleting",
                message=f"Dir <{path}> deleted successfully"
            )
        except PathNotFoundException as error:
            self.__window.showErrorMessageBox(
                title="File Touching",
                message=error
            )
        except PathExistsAsFileException as error:
            self.__window.showErrorMessageBox(
                title="File Touching",
                message=error
            )
