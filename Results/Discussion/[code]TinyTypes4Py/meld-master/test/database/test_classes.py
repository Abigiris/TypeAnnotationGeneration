import unittest
from tempfile import gettempdir  # TODO: CHANGE TO pyfakefs
from pathlib import Path

from meld.database.classes import Column, Table, Database


class ColumnConstructor(unittest.TestCase):
    base_case = {"name": "col1", "type": str}

    def testBaseCase(self):
        try:
            Column(self.base_case["name"], self.base_case["type"])
        except Exception:
            self.fail("base case failed")


class ColumnCreateQuery(unittest.TestCase):
    """
	This method generates the qry required for the table creation
	"""

    def testColumnCreate(self):
        column = Column("col", str)
        self.assertEqual(column._create(), "col TEXT")

    def testColumnCreatePrimaryKey(self):
        column = Column("col", str, primary_key=True)
        self.assertEqual(column._create(), "col TEXT PRIMARY KEY")

    def testColumnCreateNotNull(self):
        column = Column("col", str, not_null=True)
        self.assertEqual(column._create(), "col TEXT NOT NULL")

    def testColumnCreateUnique(self):
        column = Column("col", str, unique=True)
        self.assertEqual(column._create(), "col TEXT UNIQUE")

    def testColumnCreateAutoincrement(self):
        column = Column("col", int, autoincrement=True, primary_key=True)
        self.assertEqual(column._create(), "col INTEGER PRIMARY KEY AUTOINCREMENT")

    def testColumnCreateDefault(self):
        column = Column("col", str, default="HEyYA")
        self.assertEqual(column._create(), "col TEXT DEFAULT HEyYA")


class TableConstructor(unittest.TestCase):
    base_case = {
        "name": "tbl1",
        "columns": [Column("col1", str, primary_key=True), Column("col2", str)],
    }

    def testBaseCase(self):
        try:
            Table(self.base_case["name"], self.base_case["columns"])
        except Exception:
            self.fail("base case failed")

    def testColumnsNotListWrapped(self):
        """
		Column not wrapped in list
		"""
        with self.assertRaises(TypeError):
            Table(self.base_case["name"], Column("col1", str))

    def testColumnsEmptyList(self):
        with self.assertRaises(ValueError):
            Table(self.base_case["name"], [])


class TableCreateQuery(unittest.TestCase):
    def testSingleColumn(self):
        table = Table("table1", [Column("col1", int, primary_key=True)])
        self.assertEqual(
            table._create_query(), "CREATE TABLE table1 ( col1 INTEGER PRIMARY KEY )"
        )

    def testSingleColumnIfNotExist(self):
        table = Table("table1", [Column("col1", int, primary_key=True)])
        self.assertEqual(
            table._create_query(if_not_exists=True),
            "CREATE TABLE IF NOT EXISTS table1 ( col1 INTEGER PRIMARY KEY )",
        )

    def testMultiColumn(self):
        table = Table(
            "table1", [Column("col1", int, primary_key=True), Column("col2", str)]
        )
        self.assertEqual(
            table._create_query(),
            "CREATE TABLE table1 ( col1 INTEGER PRIMARY KEY, col2 TEXT )",
        )

    def testMultiColumnIfNotExists(self):
        table = Table(
            "table1", [Column("col1", int, primary_key=True), Column("col2", str)]
        )
        self.assertEqual(
            table._create_query(if_not_exists=True),
            "CREATE TABLE IF NOT EXISTS table1 ( col1 INTEGER PRIMARY KEY, col2 TEXT )",
        )


class DatabaseConstructor(unittest.TestCase):
    base_case = {
        "path": Path(gettempdir(), "testdb.sqlite"),  # TODO: CHANGE TO pyfakefs
        "tables": [Table("tb1", [Column("col1", int)])],
    }
    def testBaseCase(self):
        try:
            Database(self.base_case["path"], self.base_case["tables"])
        except Exception:
            self.fail("Base case failed")

