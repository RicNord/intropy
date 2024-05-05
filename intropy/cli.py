import argparse
import logging
from typing import Optional, Sequence

from cookiecutter.main import cookiecutter

from intropy import setup_logging

logger = logging.getLogger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point"""

    setup_logging()
    logger.debug(f"Got {argv=}")

    parser = argparse.ArgumentParser(
        description="Generate a new python project",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "template",
        help="Path to template to generate",
        nargs="?",
        default="https://github.com/RicNord/intropy",
    )
    parser.add_argument(
        "extra_context",
        nargs="*",
        default=[],
        help="Description of extra_context argument",
    )
    parser.add_argument(
        "--no-input",
        action="store_true",
        help="Do not prompt for parameters and only use cookiecutter.json file content. Defaults to deleting any cached resources and redownloading them. Cannot be combined with the --replay flag.",
    )
    parser.add_argument(
        "-c", "--checkout", help="Branch, tag or commit to checkout after git clone"
    )
    parser.add_argument(
        "--directory",
        help="Directory within repo that holds cookiecutter.json file for advanced repositories with multi templates in it",
    )
    parser.add_argument(
        "--replay",
        action="store_true",
        help="Do not prompt for parameters and only use information entered previously. Cannot be combined with the --no-input flag or with extra configuration passed.",
    )
    parser.add_argument(
        "-f",
        "--overwrite-if-exists",
        action="store_true",
        help="Overwrite the contents of the output directory if it already exists",
    )
    parser.add_argument(
        "-s",
        "--skip-if-file-exists",
        action="store_true",
        help="Skip the files in the corresponding directories if they already exist",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=".",
        type=str,
        help="Where to output the generated project dir into",
    )
    parser.add_argument(
        "--config-file", type=str, default=None, help="User configuration file"
    )
    parser.add_argument(
        "--default-config",
        action="store_true",
        help="Do not load a config file. Use the defaults instead",
    )
    parser.add_argument(
        "--accept-hooks", action="store_false", help="Accept pre/post hooks"
    )
    parser.add_argument(
        "--keep-project-on-failure",
        action="store_true",
        help="Do not delete project folder on failure",
    )
    args = parser.parse_args(argv)
    dict_args = vars(args)
    template = dict_args.pop("template")

    logger.debug(f"Parsed args: {dict_args}")
    logger.debug(f"Parsed template args: {template}")
    logger.info("Initiate main CLI function")

    cookiecutter(template, **dict_args)
    logger.info("Python project generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
