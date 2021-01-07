import pytest

def pytest_addoption(parser):
    parser.addoption("--ifile", action="store", default="default")
            
@pytest.fixture(scope='session')
def ifile(request):
    ifile_value = request.config.option.ifile
    if ifile_value is None:
        pytest.skip()
    return ifile_value
