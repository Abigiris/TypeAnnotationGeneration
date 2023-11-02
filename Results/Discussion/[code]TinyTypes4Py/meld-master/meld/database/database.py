from typing import Union
import sqlite3
from pathlib import Path
import os.path

from meld.utils import logger
import meld.database.tables

_TypePath = Union(str, Path)

def _get_builtin_tables():
    return [table for table in meld.database.tables.__all__]

class Database:
    tables = _get_builtin_tables()

    def __init__(self, filepath: _TypePath):
        logger.debug(f'Connecting to database at {filepath}')

        self.path = str(Path(os.path.expandvars(
            os.path.expanduser(filepath))).resolve())
        self.conn = sqlite3.connect(self.path)

    def init_tables(self, cursor: sqlite3.Cursor, if_not_exists: bool = True):
        for table in self.tables.values():
            table.create(cursor, if_not_exists)
