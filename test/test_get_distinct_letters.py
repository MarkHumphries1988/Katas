from src.get_distinct_letters.get_distinct_letters import get_distinct_letters


def test_gets_all_letters_if_words_are_single_letters():
    expected="ab"
    result=get_distinct_letters("a","b")
    assert result==expected

def test_orders_letters_in_distinct_words():
    expected="aehimt"
    result=get_distinct_letters("hi","mate")
    assert result==expected

def test_returns_unique_letters_in_order():
    expected="dehrw"
    result=get_distinct_letters("hello","world")
    assert result==expected
