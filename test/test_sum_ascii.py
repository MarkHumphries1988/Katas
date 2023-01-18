from src.sum_ascii.sum_ascii import sum_ascii

def test_returns_one_name_when_passed_one_name():
    expected="John"
    result=sum_ascii(["John"])
    assert expected==result

def test_returns_last_letter_in_alphabet_when_names_are_single_chars():
    expected="d"
    result=sum_ascii(["a","b","c","d"])
    assert expected==result

    expected="z"
    result=sum_ascii(["g","v","c","z","a", "l"])
    assert expected==result

def test_returns_highest_scoring_name():
    expected="ppppp"
    result=sum_ascii(["zz","aaaaa","pppp","ppppp","cccc"])
    assert expected==result

