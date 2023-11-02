import sqlite3
from pathlib import Path
import zlib
from typing import Union, List, Optional, Iterable

from PIL import Image

from meld import logger
import meld.database.tables as tables
from . import utils

# List of supported image formats
# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
SUPPORTED_IMAGE_FORMATS = ['JPEG', 'PNG']

PathType = Union[str, Path]


def generatePhotoList(paths: Iterable[PathType],
                      supported_formats: List[str] = SUPPORTED_IMAGE_FORMATS,
                      exclude_dirs: bool = False):
    """
    Generator that returns a filepath to a photo
    """
    for path in paths:
        path = Path(path)
        if path.is_dir() and not exclude_dirs:
            yield from generatePhotoList(path.iterdir(), supported_formats)
        elif isSupportedImage(path, supported_formats):
            yield path


def isSupportedImage(filepath: PathType,
                     supported_formats: List[str] = SUPPORTED_IMAGE_FORMATS):
    filepath = Path(filepath)
    try:
        # if PIL can recognize the file, then probably and image
        with Image.open(str(filepath)) as im:
            if im.format not in supported_formats:
                raise InvalidFileFormatError(
                    f'invalid file format: {im.format}')
    except FileNotFoundError as e:
        # probably a directory
        logger.debug(f'Filtering {filepath} because {e}')
    except OSError as e:
        # not an image file
        logger.debug(f'Filtering {filepath} because {e}')
    except InvalidFileFormatError as e:
        # unsupported image format
        logger.debug(f'Filtering {filepath} because {e}')
    else:
        # all good
        return True
    return False


class InvalidFileFormatError(Exception):
    pass


class Photo:
    table = tables.photos

    def __init__(self, filepath: PathType):
        self.filepath = Path(filepath)
        self.filename = utils.deleteForbiddenCharacters(self.filepath.stem)

        with Image.open(str(self.filepath)) as im:
            self.width, self.height = im.size
            self.file_format = im.format

        self.filesize = Path(self.filepath).stat().st_size

        with open(self.filepath, 'rb') as f:
            self.crc32 = hex(zlib.crc32(f.read()) & 0xffffffff)

    def _insert_data(self, set_id: Optional[int] = None) -> dict:
        return {
            'filename': self.filename,
            'file_format': self.file_format,
            'set_id': set_id,
            'width': self.width,
            'height': self.height,
            'filesize': self.filesize,
            'crc32': self.crc32
        }

    def _insert_qry(self, set_id: Optional[int] = None) -> str:
        """
        Prepares the qry required to insert the data into database
        """
        photo_data = self._insert_data(set_id)

        # INSERT INTO table_name (col1, col2, ...) VALUES (?,?,...)
        return (
            f'INSERT INTO {self.table.name}'
            f'({", ".join([key for key in photo_data.keys()])})'
            ' VALUES '
            f'({",".join("?"*len(photo_data))})'
        )

    def _insert_debug_qry(self, set_id: Optional[int] = None) -> str:
        """
        Prepares the qry required to insert the data into database. This query 
        is not executed but is generated for logging purposes
        """
        photo_data = self._insert_data(set_id)

        # INSERT INTO table_name (col1, col2, ...) VALUES (val1, val2, ...)
        return (
            f'INSERT INTO {self.table.name}'
            f'({", ".join([key for key in photo_data.keys()])})'
            ' VALUES '
            f'''({', '.join([f'"{value}"' if isinstance(value, str) else 
			'NULL' if value is None else
			str(value) for value in photo_data.values()])})'''
        )

    def insert(self, cursor: Union[sqlite3.Connection, sqlite3.Cursor],
               set_id: Optional[int] = None):
        logger.debug(f'Executing query: {self._insert_debug_qry(set_id)}')

        cursor.execute(self._insert_qry(),
                       tuple(self._insert_data(set_id).values()))


class PhotoSet:
    table = tables.sets

    def __init__(self, name: str, year: int,
                 photos: List[Photo] = [], studio: Optional[str] = None):
        self.name = name
        self.year = year
        self.studio = studio
        self.photos = photos

    def _insert_data(self) -> dict:
        return {
            'name': self.name,
            'year': self.year,
            'studio': self.studio
        }

    def _insert_qry(self) -> str:
        """
        Prepares the qry required to insert the data into database
        """

        photo_set_data = self._insert_data()

        # INSERT INTO table_name (col1, col2, ...) VALUES (?,?,...)
        return (
            f'INSERT INTO {self.table.name}'
            f'({", ".join([key for key in photo_set_data.keys()])})'
            ' VALUES '
            f'({",".join("?"*len(photo_set_data))})'
        )

    def _insert_debug_qry(self) -> str:
        """
        Prepares the qry required to insert the data into database. This query 
        is not executed but is generated for logging purposes
        """
        photo_set_data = self._insert_data()

        # INSERT INTO table_name (col1, col2, ...) VALUES (val1, val2, ...)
        return (
            f'INSERT INTO {self.table.name}'
            f'({", ".join([key for key in photo_set_data.keys()])})'
            ' VALUES '
            f'''({', '.join([f'"{value}"' if isinstance(value, str) else 
				'NULL' if value is None else
				str(value) for value in photo_set_data.values()])})'''
        )

    def insert(self, cursor: Union[sqlite3.Connection, sqlite3.Cursor]):
        logger.debug(f'Executing query: {self._insert_debug_qry()}')

        cursor.execute(self._insert_qry(), tuple(
            self._insert_data().values()))
        set_id = cursor.lastrowid

        for photo in self.photos:
            photo.insert(cursor, set_id)

    def addPhoto(self, photo: Photo):
        self.photos.append(photo)
