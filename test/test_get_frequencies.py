from src.get_frequencies.get_frequencies import get_frequencies

def test_unique_letter_word_returns_dict_with_1s():
    expected={"w":1,"o":1,"r":1,"l":1,"d":1}
    result=get_frequencies("world")
    assert result==expected

def test_multi_same_letter_returns_apt_dict():
    expected={"h":1,"e":1,"l":2,"o":1}
    result=get_frequencies("hello")
    assert result==expected

def test_string_ignores_spaces():
    expected={
  'h': 1,
  'e': 1,
  'l': 3,
  'o': 2,
  'w': 1,
  'r': 1,
  'd': 1
    }
    result=get_frequencies("hello world")
    assert expected==result