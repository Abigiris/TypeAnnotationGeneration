import logging
import logging.handlers
from pathlib import Path
import appdirs

from meld.__about__ import __title__ as appname, __author__ as author

# Create application log directory
log_dir = Path(appdirs.user_log_dir(appname, author))
Path(log_dir).mkdir(parents=True, exist_ok=True)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(
    logging.Formatter('{asctime} - {levelname} - {message}', style='{')
)

file_handler = logging.handlers.RotatingFileHandler(
    filename=log_dir.joinpath(__name__).with_suffix('.log')
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(
    logging.Formatter('{asctime} - {name} - {levelname} - {message}', style='{')
)

logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
