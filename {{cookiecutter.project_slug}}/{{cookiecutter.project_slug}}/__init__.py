__version__ = "{{ cookiecutter.version }}"

{% if cookiecutter.project_type == 'Application' -%}
import logging
import logging.config
import time

ROOT_LOGGER = logging.getLogger(__name__)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


class SelfFilter(logging.Filter):
    def filter(self, record):
        """Filter only events from within the package"""
        return record.name.startswith(str(__package__))


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "self_filter": {
            "()": SelfFilter,
        },
    },
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
            "formatter": "simple",
            "class": "logging.StreamHandler",
            "filters": ["self_filter"],
        },
        "detailed": {
            "formatter": "standard_utc",
            "class": "logging.StreamHandler",
            "filters": ["self_filter"],
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
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
{%- elif cookiecutter.project_type == 'Library' -%}
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
{%- endif %}
