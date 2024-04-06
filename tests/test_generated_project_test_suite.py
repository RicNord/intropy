import subprocess


def test_tox(cookies):
    result = cookies.bake()

    p = subprocess.Popen(
        ["tox"],
        cwd=result.project_path,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    _, err = p.communicate(timeout=100)

    if p.returncode != 0:
        raise RuntimeError(err)
