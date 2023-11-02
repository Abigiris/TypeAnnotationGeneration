from meld.database.classes import Table, Column

photos = Table('photos', [
    Column('id', int, primary_key=True, autoincrement=True),
    Column('filename', str),
    Column('file_format', str),
    Column('set_id', int, default='NULL'),
    Column('width', int),
    Column('height', int),
    Column('filesize', int),  # in bytes
    Column('crc32', str)  # stored as 8 byte hex
])
