from {{ cookiecutter.project_slug }} import __version__


def test_version_exits():
    assert isinstance(__version__,str)
