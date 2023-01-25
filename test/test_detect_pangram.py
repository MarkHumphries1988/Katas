from src.detect_pangram.detect_pangram import detect_pangram

def test_returns_false_on_anything_less_than_26_letters():
    expect=False
    result=detect_pangram("a")
    assert result==expect

    result=detect_pangram("abcdefghijklmnopqrstuvwxy")
    assert result==expect

def test_returns_true_on_alphabet():
    expect=True
    result=detect_pangram("abcdefghijklmnopqrstuvwxyz")
    assert result==expect

def test_returns_true_on_complex_sentence():
    expect=True
    result=detect_pangram("The quick brown fox jumps over the lazy dog.")
    assert result==expect

def test_doesnt_get_tricked_by_strange_characters():
    expect=False
    result=detect_pangram("!!!!!!!!!@@@@@!!!!!@@@@@@@@@@@@@!!!!!!!!@@@@")
    assert result==expect

    expect=True
    result=detect_pangram("The........ quick@@ brown! fox! jumps over the lazy dog.")
    assert result==expect