import argparse
import logging
from typing import Optional, Sequence

{% if cookiecutter.project_type == 'Application' -%}
from {{ cookiecutter.project_slug }} import ROOT_LOGGER, setup_logging

{% elif cookiecutter.project_type == 'Library' -%}
from {{ cookiecutter.project_slug }} import ROOT_LOGGER

{% endif -%}
logger = logging.getLogger(__name__)


class CustomHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def _get_help_string(self, action):
        if action.default is not argparse.SUPPRESS and action.dest != "verbose":
            return super()._get_help_string(action)
        return action.help


def _set_logger_level(logger: logging.Logger, count: int) -> None:
    if count == 0:
        return
    if count == 1:
        logger.setLevel(logging.INFO)
        return
    logger.setLevel(logging.DEBUG)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point"""
{%- if cookiecutter.project_type == 'Application' %}

    setup_logging()
{%- endif %}

    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_short_description }}",
        formatter_class=CustomHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity: -v for INFO, -vv for DEBUG. Default is WARNING.",
    )

    args = parser.parse_args(argv)

    _set_logger_level(logger=ROOT_LOGGER, count=args.verbose)

    logger.debug(f"Got {argv=}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
