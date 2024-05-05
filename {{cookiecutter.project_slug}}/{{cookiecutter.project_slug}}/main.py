import logging

from {{ cookiecutter.project_slug }} import setup_logging

logger = logging.getLogger(__name__)


def main() -> int:
    logger.debug("Enter main")
    # Body
    logger.debug("Exit main")
    return 0


if __name__ == "__main__":
    setup_logging()
    raise SystemExit(main())
