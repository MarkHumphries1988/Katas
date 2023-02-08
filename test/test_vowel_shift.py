from src.vowel_shift.vowel_shift import vowel_shift

def test_no_shift_returns_original():
    expected="hello"
    result=vowel_shift('hello',0)
    assert expected==result




def test_wraparound_single_shift():
    expected="ebcdaf"
    result=vowel_shift("abcdef",1)
    assert expected==result

def test_shifts_more_than_one_vowel_space():
    expected="stor nesad mole"
    result=vowel_shift("star nosed mole",2)
    assert expected==result

    expected="finnely onuugh"
    result=vowel_shift("funnily enough",4)
    assert expected==result

