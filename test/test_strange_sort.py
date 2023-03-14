from src.strange_sort.strange_sort import strange_sort

def test_sorts_distinct_length_strings_by_length_descending():
    expected=['enormous', 'small', 'big']
    result = strange_sort("small","big","enormous")
    assert expected==result

def test_optional_argument_changes_order():
    expected=["big","small","enormous"]
    result = strange_sort("small","big","enormous",desc=False)
    assert expected==result

def test_same_length_results_in_alphabetical():
    expected=['expressions', 'nasty', 'three', 'bad', 'big']
    result = strange_sort('three', 'big', 'nasty', 'bad', 'expressions')
    assert result==expected

    result=strange_sort("aaa","ccc", "eee", "ddd", "bbb")
    expected=["aaa","bbb","ccc","ddd","eee"]
    assert result==expected

def test_ignores_case():
    expected=['expressions', 'nasty', 'three', 'bad', 'Big']
    result = strange_sort('three', 'Big', 'nasty', 'bad', 'expressions')
    assert result==expected
