from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_sentence_in_upper_if_true():
    expected="ThisSentence"
    result=sentence_to_camel_case("this sentence",True)
    assert result==expected

def test_returns_lower_camel_if_false():
    expected="thisSentence"
    result=sentence_to_camel_case("this sentence",False)
    assert result==expected

def test_returns_reversed_if_passed_third_arguement_called_as_reverse():
    expected="This bigger strange sentence."
    result=sentence_to_camel_case("thisBiggerStrangeSentence",reverse=True)
    assert result==expected
