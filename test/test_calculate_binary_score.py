from src.calculate_binary_score.calculate_binary_score import calculate_binary_score, count_even_bits

def test_count_even_bits():
    expected=1
    result=count_even_bits(2)
    assert result==expected

    expected=2
    result=count_even_bits(4)
    assert result==expected

    expected=1
    result=count_even_bits(14)
    assert result==expected

    for i in range(1,10):
        expected=i
        result=count_even_bits(2**i)
        assert result==expected

        expected=1
        result=count_even_bits(2**i-2)
        assert result==expected





def test_if_only_one_value_that_team_wins():
    expected="odds win"
    result=calculate_binary_score([1])
    assert expected==result

    expected="evens win"
    result=calculate_binary_score([2])
    assert expected==result

def test_tie_if_same_score():
    expected="tie"
    result=calculate_binary_score([1,2])
    assert result==expected

def test_long_list():
    expected="odds win"
    result=calculate_binary_score([1,2,3,4,5])
    assert result==expected

    expected="evens win"
    result=calculate_binary_score([1,20])
    assert result==expected