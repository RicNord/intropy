import argparse
import logging
from typing import Optional, Sequence

logger = logging.getLogger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point"""

    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_short_description }}",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    logger.info("Parse arguments")
    # Add arguments
    _ = parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
