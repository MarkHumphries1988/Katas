from src.alphabet_position.alphabet_position import alphabet_position

def test_empty_string_returns_empty_string():
    expected=""
    result=alphabet_position("")
    assert expected==result


def test_just_string_of_lowercase():
    expect="1 2 3"
    result=alphabet_position("abc")

    assert expect==result

def test_other_characters_in_string():
    expect="8 5 12 12 15 23 15 18 12 4"
    result=alphabet_position("hello world!")

    assert expect==result

def test_works_on_upper():
    expect="1 26 1 26"
    result=alphabet_position("azAZ")
    assert expect==result