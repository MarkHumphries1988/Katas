from src.find_most_repeated.find_most_repeated import find_most_repeated

def test_empty_list_returns_empty_and_null():
    expect={'elements': [], 'repeats': 'null'}
    result=find_most_repeated([])
    assert result==expect

def test_no_repeats_returns_empty_null():
    expect={'elements': [], 'repeats': 'null'}
    result=find_most_repeated(['foo', 'bar', 'hello', 'world'])

    assert result==expect

def test_singular_winner():
    expect={'elements': ['foo'], 'repeats': 2}
    result=find_most_repeated(['foo', 'foo', 'bar', 'hello', 'world'])
    assert result==expect

def test_multiple_winners():

    expect={'elements': ['foo', 'bar'], 'repeats': 3}
    result=find_most_repeated(['foo', 'foo', 1, 2, 3, 'bar', 2, 3, 4, 'bar', 'bar', 'foo'])   
    assert result==expect
    