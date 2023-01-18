from src.lengthen_date.lengthen_date import lengthen_date

def test_returns_string_with_date_in_words():
    expected='Tuesday 21st March 2017'
    result=lengthen_date('21.03.2017')
    assert result==expected
def test_returns_with_proper_ordinal():
    expected='Monday 20th March 2017'
    result=lengthen_date('20.03.2017')
    assert result==expected

    expected='Wednesday 22nd March 2017'
    result=lengthen_date('22.03.2017')
    assert result==expected

    expected="Friday 13th May 1988"
    result=lengthen_date('13.05.1988')
    assert result==expected