from proj.parse import parse
import pytest

def test_parse():
    res = parse("1,23")
    assert res == [1, 23], "value should be array"

def test_bad1():
    with pytest.raises(ValueError):
        res = parse('bad input')

#below is expected failure
@pytest.mark.xfail(raises=ValueError)
def testbad2():
    res = parse('1-2,12-15')
