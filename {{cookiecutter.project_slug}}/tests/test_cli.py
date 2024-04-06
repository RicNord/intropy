from  {{ cookiecutter.project_slug }} import cli


def test_cli_runner():
    exit_code = cli.main([])
    assert exit_code == 0
