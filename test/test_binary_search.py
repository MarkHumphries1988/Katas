from src.binary_search.binary_search import binary_search

def test_returns_index_in_list_of_two_items():
    expected=1
    result=binary_search([1,2],2)
    assert expected==result

    expected=0
    result=binary_search([1,2],1)
    assert result==expected

def test_returns_minus_when_not_found():
    expected=-1
    result=binary_search([1,2],3)
    assert result==expected

def test_returns_index_in_list_of_four_items():
    expected=2
    result=binary_search([1,2,3,4],3)
    assert result==expected

def test_copes_with_odd_list():
    expected=2
    result=binary_search([1,2,3,4,5],3)
    assert result==expected

def test_copes_with_super_long_list():
    expected=8
    result=binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],9)
    assert result==expected