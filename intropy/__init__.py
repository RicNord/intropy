__version__ = "0.6.2"

import logging
import logging.config
import time

INTROPY_ROOT_LOGGER = logging.getLogger(__name__)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s: %(message)s"},
        "standard_utc": {
            "()": UTCFormatter,
            "format": "[%(levelname)s|%(name)s|L%(lineno)d] %(asctime)s: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "default": {
            "level": "WARNING",
            "formatter": "simple",
            "class": "logging.StreamHandler",
        },
        "detailed": {
            "level": "DEBUG",
            "formatter": "standard_utc",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "DEBUG",
        },
        "__main__": {  # if __name__ == '__main__'
            "handlers": ["detailed"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
