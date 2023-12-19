import os
import shutil
from pathlib import Path

from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)
from helpers.customExceptions import TypeException


class FileSystem:
    def __init__(self):
        pass

    @staticmethod
    def exists(path):
        return Path(path).exists()
