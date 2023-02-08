from src.alternating_split.alternating_split import decrypt,encrypt

def test_if_n_zero_returns_string():
    expected="12345"
    result=encrypt("12345",0)
    assert result==expected

def test_if_just_two_letters_swaps():
    expected="21"
    result=encrypt("12",1)
    assert expected==result

def test_concats_once_through():
    expected="135024"
    result=encrypt("012345",1)
    assert expected==result

def test_concats_n_times_through():
    expected="304152"
    result=encrypt("012345",2)
    assert expected==result

    expected="76543210"
    result=encrypt("01234567",3) 
    assert expected==result

def test_with_odd_length():
    expected="13024"
    result=encrypt("01234",1)
    assert expected==result






def test_if_decrypt_zero_returns_original():
    expected="012345"
    result=decrypt("012345",0)
    assert result==expected


def test_if_decrypt_one_on_two_letters_swaps():
    expected="12"
    result=decrypt("21",1)
    assert result==expected

def test_if_decrypt_one_on_several_items_each_half_splits_and_shuffles_regularly_through():
    expected="012345"
    result=decrypt("135024",1)
    assert result==expected


def test_applies_to_odd_length():
    expected="01234"
    result=decrypt("13024",1)
    assert result==expected

    expected="012345678"
    result=decrypt("135702468",1)
    assert result==expected

def test_applies_n_times():
    expected="012345"
    result=decrypt("304152",2)
    assert result==expected

    expected="01234567"
    result=decrypt("76543210",3)
    assert result==expected


