import pytest

@pytest.mark.mock
@pytest.mark.passing
def test_example():
    assert [ 1, 2, 3 ] == [ 1, 2, 3 ]

@pytest.mark.failing
def test_example_failure():
    assert [ 1, 2, 3 ] == [ 1, 2, 0 ]

@pytest.mark.mock
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

@pytest.fixture()
def fixture():
    return "word"

def test_fixture(fixture):
    assert fixture == "word"

@pytest.mark.parametrize("number", [ 1,2,3,4])
def test_foo(number):
    assert number > 0
