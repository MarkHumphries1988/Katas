from src.justify_line.justify_line import justify_line

def test_too_long_returns_comment():
    expected="String exceeds maximum line length"
    result=justify_line("foo foo foo foo",10)
    assert expected==result

def test_adds_single_space_to_first():
    expected="foo  foo foo"
    result=justify_line("foo foo foo",12)
    assert result==expected

def adds_to_all_spaces():
    expected="foo  foo  foo"
    result=justify_line("foo foo foo",13)
    assert result==expected

def adds_multiple_spaces_evenly():
    expected='foo   foo   foo  foo'
    result=justify_line("foo foo foo foo",20)
    assert result==expected