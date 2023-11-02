from appdirs import user_data_dir
from pathlib import Path

from meld.__about__ import __title__, __author__

app_data_dir = Path(user_data_dir(__title__, __author__))

# Initialize data directory and required datafiles
Path(app_data_dir).mkdir(exist_ok=True, parents=True)