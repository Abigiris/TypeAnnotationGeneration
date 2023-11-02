from typing import List, Union, Optional
import os.path
from pathlib import Path

from meld import logger
from meld.database import Database

from . import photos


def main(files: List[Union[Path, str]],
         database: Database,
         set_name: str = 'UNKNOWN',
         year: Optional[int] = None,
         studio: Optional[str] = None,
         supported_formats: List[str] = photos.SUPPORTED_IMAGE_FORMATS,
         test: bool = False):
    logger.debug("Started sync main function of 'insert'")
    logger.debug(f'Arguments: {locals()}')

    cursor = database.conn.cursor()

    photolist = [photos.Photo(filepath)
                 for filepath in photos.generatePhotoList(files, supported_formats)]
    photo_set = photos.PhotoSet(
        set_name, year, photos=photolist, studio=studio)

    logger.debug('Inserting photos into database')
    try:
        photo_set.insert(cursor)
    except Exception as e:
        logger.error(f'Failed to insert photos to database: {e}')
        database.conn.rollback()  # do not commit changes
        return
    else:
        if test:
            logger.debug('Test mode activated, rolling back changes')
            database.conn.rollback()
        else:
            logger.debug('Committing changes to database')
            database.conn.commit()


async def mainAsync(files: List[Union[str, Path]],
                    database: Database,
                    set_name: str = 'UNKNOWN',
                    year: Optional[int] = None,
                    studio: Optional[str] = None,
                    supported_formats: List[str] = photos.SUPPORTED_IMAGE_FORMATS,
                    test: bool = False):
    """
    Same as main except runs async
    """
    raise NotImplementedError
