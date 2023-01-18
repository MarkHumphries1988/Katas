from src.roman_numeral_encoder.roman_numeral_encoder import roman_numeral_encoder


def test_encodes_numbers_less_than_11():
    expected="I"
    result=roman_numeral_encoder(1)
    assert expected==result

    expected="II"
    result=roman_numeral_encoder(2)
    assert expected==result
     
    expected="IV"
    result=roman_numeral_encoder(4)
    assert expected==result

    expected="IX"
    result=roman_numeral_encoder(9)
    assert expected==result

    expected="X"
    result=roman_numeral_encoder(10)
    assert expected==result

def test_encodes_numbers():
    
    expected="XVII"
    result=roman_numeral_encoder(17)
    assert expected==result

    expected="LX"
    result=roman_numeral_encoder(60)
    assert expected==result

    expected="LXXV"
    result=roman_numeral_encoder(75)
    assert expected==result

    expected="XCI"
    result=roman_numeral_encoder(91)
    assert expected==result