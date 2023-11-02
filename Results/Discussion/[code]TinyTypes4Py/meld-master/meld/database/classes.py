from typing import List, Any, Union
import sqlite3
from pathlib import Path
import os.path

from meld.utils import logger


class Column:
    def __init__(self, name: str,
                 db_type: Union[None, type],
                 primary_key: bool = False,
                 autoincrement: bool = False,
                 default: Any = None,
                 not_null: bool = False,
                 unique: bool = False
                 ):
        '''
        See link for python-sql type conversions
        https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types
        '''
        self.name = name
        self.db_type = db_type
        self.settings = {
            'primary_key': primary_key,
            'default': default,
            'autoincrement': autoincrement,
            'not_null': not_null,
            'unique': unique
        }

    @property
    def db_type(self) -> str:
        return {
            None: 'NULL',
            int: 'INTEGER',
            float: 'REAL',
            str: 'TEXT',
            bytes: 'BLOB'
        }[self._db_type]

    @db_type.setter
    def db_type(self, value: Union[None, type]):
        self._db_type = value

    def _create(self) -> str:
        '''
        generates the respective column query required to fill in 
            CREATE TABLE table_name (column1_qry, column2_qry)
        '''
        settings = self.settings

        qry_list = [f'{self.name} {self.db_type}']

        if settings['primary_key']:
            qry_list.append('PRIMARY KEY')
        if settings['default'] is not None:
            qry_list.append(f'DEFAULT {settings["default"]}')
        if settings['autoincrement'] and settings['primary_key'] and \
                self.db_type == 'INTEGER':
            qry_list.append('AUTOINCREMENT')
        if settings['not_null']:
            qry_list.append('NOT NULL')
        if settings['unique']:
            qry_list.append('UNIQUE')

        return ' '.join(qry_list)


class Table:
    def __init__(self, name: str, columns: List[Column]):
        self.name = name
        self.columns = columns

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Table name is not a string')
        self._name = value

    @property
    def columns(self) -> List[Column]:
        return self._columns

    @columns.setter
    def columns(self, value: List[Column]):
        if len(value) == 0:
            raise ValueError('No columns specified')

        self._columns = value

    def _create_query(self, if_not_exists: bool = False) -> str:
        """
        Generates the table creation query
        """

        column_qry = ['CREATE TABLE']

        if if_not_exists:
            column_qry.append('IF NOT EXISTS')

        column_qry += [self.name, '(',
                       ', '.join([column._create()
                                  for column in self.columns]),
                       ')'
                       ]
        return ' '.join(column_qry)

    def create(self, cursor: Union[sqlite3.Connection, sqlite3.Cursor], if_not_exists: bool = False):
        logger.debug(f'Creating table: {self.name}')
        qry = self._create_query(if_not_exists)

        logger.debug(f'Executing query: {qry}')
        cursor.execute(qry)


class Database:
    def __init__(self, filepath: Union[str, Path], tables: List[Table]):
        self.path = filepath
        self.tables = tables

        self.conn = sqlite3.connect(self.path)

    @property
    def path(self) -> str:
        return str(self._path)

    @path.setter
    def path(self, value: Union[str, Path]):
        self._path = Path(os.path.expandvars(
            os.path.expanduser(value))).resolve()

    def createTables(self, cursor: Union[sqlite3.Connection, sqlite3.Cursor],
                     if_not_exists: bool = True):
        for table in self.tables:
            table.create(cursor, if_not_exists)
