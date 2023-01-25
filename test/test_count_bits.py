from src.count_bits.count_bits import count_bits

def test_zero_returns_zero():
    expect=0
    result=count_bits(0)
    assert expect==0

def test_counts_1():
    expect=1
    result=count_bits(1)
    assert expect==result

def test_counts_2():
    expect=1
    result=count_bits(1)
    assert expect==result

def test_counts_powers_of_two():

    for i in range(20):
        expect=1
        result=count_bits(2**i)
        assert expect==result

def test_not_just_single():
    expect=5
    result=count_bits(1234)
    assert expect==result
