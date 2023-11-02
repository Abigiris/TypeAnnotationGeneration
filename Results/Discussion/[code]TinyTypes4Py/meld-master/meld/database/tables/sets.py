from meld.database.classes import Table, Column

sets = Table('sets', [
        Column('id', int, primary_key=True, autoincrement=True),
        Column('name', str),
        Column('year', int),
        Column('studio', str, default=None)
    ])