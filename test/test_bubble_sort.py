from src.bubble_sort.bubble_sort import bubble_sort


def test_already_ordered_remains_same():
    expected=[1,2,3,4]
    result=bubble_sort([1,2,3,4])
    assert result==expected

def test_swaps_two_numbered_list():
    expected=[1,4]
    result=bubble_sort([4,1])
    assert result==expected

def test_moves_along_to_end():
    expected=[1,2,3,4,5,6]
    result=bubble_sort([6,1,2,3,4,5])
    assert result==expected

def test_sorts_list():
    expected=[1,2,3,4,5,6,7,8,9]
    result=bubble_sort([5,2,3,8,7,6,9,1,4])
    assert result==expected