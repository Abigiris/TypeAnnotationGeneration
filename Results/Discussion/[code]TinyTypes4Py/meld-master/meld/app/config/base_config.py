from meld import app_data_dir

_DEFAULT_DATABASE_NAME = 'database.sqlite'

BASE_CONFIG = {
        "database": str(app_data_dir.joinpath(_DEFAULT_DATABASE_NAME)),
        "insert": {
            "format": ['JPEG']
        }
    }
