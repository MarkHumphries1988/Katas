from src.morse_code.morse_code import morse_code

def test_translates_a_single_morse():
    expect="H"
    result=morse_code("....")
    assert result==expect

def test_translates_a_single_word():
    expect="MARK"
    result=morse_code("-- .- .-. -.-")
    assert result==expect

def test_translates_with_spaces():
    expect="MARK IS THE GREATEST"
    result=morse_code("-- .- .-. -.-    .. ...    - .... .    --. .-. . .- - . ... -")
    assert result==expect
