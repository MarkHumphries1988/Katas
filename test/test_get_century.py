from src.get_century.get_century import get_century


def test_zero_returns_1st():
    expected="1st"
    result=get_century(0)
    assert expected==result

def test_returns_correct_century_on_borders():
    expected="20th"
    result=get_century(1999)
    assert expected==result

    expected="20th"
    result=get_century(1900)
    assert expected==result

def test_returns_correct_ending():
    expected="22nd"
    result=get_century(2130)
    assert expected==result

def test_works_till_10000():
    expected="101st"
    result=get_century(10000)
    assert expected==result