import subprocess
import sys

TIMEOUT_DURATION_SEC = 180


def test_tox_py(cookies):
    pyenv = sys.version_info
    result = cookies.bake()

    p = subprocess.Popen(
        ["tox", "-e", f"py{pyenv.major}{pyenv.minor}", "-vv", "--", "-v"],
        cwd=result.project_path,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    _, err = p.communicate(timeout=TIMEOUT_DURATION_SEC)

    if p.returncode != 0:
        raise RuntimeError(err)


def test_tox_style(cookies):
    result = cookies.bake()

    p = subprocess.Popen(
        ["tox", "-m", "style", "-vv", "--", "-v"],
        cwd=result.project_path,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    _, err = p.communicate(timeout=TIMEOUT_DURATION_SEC)

    if p.returncode != 0:
        raise RuntimeError(err)
