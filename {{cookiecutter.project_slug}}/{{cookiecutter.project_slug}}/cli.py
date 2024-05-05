import argparse
import logging
from typing import Optional, Sequence

{% if cookiecutter.project_type == 'Application' -%}
from {{ cookiecutter.project_slug }} import setup_logging

{% endif -%}
logger = logging.getLogger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point"""
{%- if cookiecutter.project_type == 'Application' %}

    setup_logging()
{%- endif %}

    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_short_description }}",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    logger.debug(f"Got {argv=}")
    # Add arguments
    _ = parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
