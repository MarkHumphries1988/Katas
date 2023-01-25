from src.fill_square.fill_square import fill_square

def test_single_singular_list_returns_itself():
    expect=[[1]]
    result=fill_square([[1]])
    assert result==expect

def test_already_square_returns_itself():
    expect=[[2,2],[2,2]]
    result=fill_square([[2,2],[2,2]])
    assert result==expect

    expect=[[3,3,3],[3,3,3],[3,3,3]]

    result = fill_square([[3,3,3],[3,3,3],[3,3,3]])

    assert result==expect

def test_only_needs_to_add_to_lists():
    expect=[
  [1, 2, 3],
  [1, 2, None],
 [1, None, None]
 ]

    result=fill_square([[1, 2, 3], [1, 2], [1]])

    assert expect==result

def test_needs_to_add_sub_lists():
    expect=[[3,3,3],[3,3,None],[None,None,None]]
    result=fill_square([[3,3,3],[3,3]])

    assert expect==result

def test_works_no_matter_order():
    expect=[[3,3,None],[3,3,3],[None,None,None]]
    result=fill_square([[3,3],[3,3,3]])
    assert expect==result




