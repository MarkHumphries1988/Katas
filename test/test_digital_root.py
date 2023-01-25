from src.digital_root.digital_root import digital_root
def test_single_digit_returns_single_digit():
    for i in range (10):
        expect=i
        result=digital_root(i)
        assert expect==result

def test_singular_pass_needed():
    expect=7
    result=digital_root(16)
    assert result==expect

    expect=6
    result=digital_root(24)
    assert result==expect

def test_two_passes():
    expect=6
    result=digital_root(132189)
    assert result==expect

def test_always_returns_single():

    for i in range(1,1234):
        
        result=digital_root(i)


        assert 0<result<10