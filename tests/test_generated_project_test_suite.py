import subprocess


def test_tox(cookies):
    result = cookies.bake()

    p1 = subprocess.Popen(
        ["git", "init"],
        stderr=subprocess.PIPE,
        cwd=result.project_path,
    )
    _, err1 = p1.communicate(timeout=10)
    err1 = err1.decode("utf-8")

    if p1.returncode != 0:
        raise RuntimeError(err1)

    p2 = subprocess.Popen(["tox"], cwd=result.project_path, stderr=subprocess.PIPE)
    _, err2 = p2.communicate(timeout=100)
    err2 = err2.decode("utf-8")

    if p2.returncode != 0:
        raise RuntimeError(err2)
