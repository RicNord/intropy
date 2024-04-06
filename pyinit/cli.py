import argparse
import logging
from typing import Optional, Sequence

from cookiecutter.main import cookiecutter

logger = logging.getLogger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point"""

    logger.info("Parse arguments")

    parser = argparse.ArgumentParser(
        description="Generate a new python project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("template", help="Template path to generate")
    args = parser.parse_args(argv)
    dict_args = vars(args)

    logger.debug(f"Parsed args: {dict_args}")
    logger.info("Initiate main CLI function")

    cookiecutter(**dict_args)
    logger.info("Python project generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
