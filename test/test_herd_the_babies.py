from src.herd_the_babies.herd_the_babies import herd_the_babies

def test_all_one_letter_returns_upper_at_front():
    expected="AAaa"
    result=herd_the_babies("aAAa")
    assert expected==result

def test_all_one_case_returns_alphabetical():
    expected="aabbbcc"
    result=herd_the_babies("abcbacb")
    assert expected==result

def test_works_when_combined():
    expected="AaBbbCcc"
    result=herd_the_babies("bbaBccAC")
    assert expected==result

    result=herd_the_babies("DDdCAaaBBaCbbAAaeEfffAa")
    expected="AAAAaaaaaBBbbCCDDdEefff"
    assert expected==result