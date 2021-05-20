import leapyear
import pytest

def test_leapyear_good():
    assert leapyear.is_leapyear(2020) == True
    assert leapyear.is_leapyear(2021) == False
    assert leapyear.is_leapyear(100) == False
    assert leapyear.is_leapyear(400) == True

def test_leapyear_fail():
    assert leapyear.is_leapyear(1) == True

def test_leapyear_exceptions():
    with pytest.raises(TypeError):
        assert leapyear.is_leapyear('asdf')