from src.caesar_cipher.caesar_cipher import caesar

def test_shift_zero_leaves_same():
    expected="hello"
    result=caesar("hello",0)
    assert result==expected

def test_shifts_single_letter_1():
    expected="y"
    result=caesar("x",1)
    assert expected==result

    expected="w"
    result=caesar("x",-1)
    assert expected==result

def test_shifts_with_a_loop_around():
    expected="a"
    result=caesar("z",1)
    assert expected==result

    expected="z"
    result=caesar("a",-1)
    assert expected==result



def test_shifts_word():
    expected="jgnnq"
    result=caesar("hello",2)
    assert expected==result

def test_ignores_spaces():
    expected="ebiil tloia!"
    result=caesar("hello world!",-3)
    assert expected==result

def test_word_wrap_around():
    expected="vwxyz"
    result=caesar("abcde",-5)
    assert expected==result
