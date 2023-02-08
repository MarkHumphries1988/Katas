from src.crack_code.crack_code import crack_code

def test_if_letters_inside_bracket_are_not_in_alphabetical_returns_false():
    expected=False
    result=crack_code("aaa-vvv-dd-s(advs)")
    assert expected==result

    expected=False
    result=crack_code("a-b-c-d-e-f-g-h-i-577(acdb)")
    assert result==expected

def test_with_just_four_letters():
    expected=True
    result=crack_code("a-b-c-d(abcd)")
    assert result==expected

    expected=True
    result=crack_code("d-b-c-a(abcd)")
    assert result==expected

def test_most_common_letters():
    expected=True
    result=crack_code("ddd-aaa-z-y-x-123(adxy)")
    assert expected==result

    expected=False
    result=crack_code("fff-gg-xx-ss-y(fgsy)")
    assert expected==result

def test_equal_commonality_but_alphabetical():
    expected=True
    result=crack_code("a-b-c-d-e-f-g-h-i-577(abcd)")
    assert result==expected

    