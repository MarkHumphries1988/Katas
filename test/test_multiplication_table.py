from src.multiplication_table.multiplication_table import multiplication_table

def test_zero_returns_empty():
    expect=[]
    result=multiplication_table(0)
    assert result==expect

def test_top_row_is_number_line():
    for i in range(1,10):
        expect=[j for j in range(0,i+1)]
        result=multiplication_table(i)
        assert result[0]==expect

def test_diagonal_is_square():
    for i in range(1,100):
        expect=i**2

        result=multiplication_table(i)

        assert result[i][i]==expect

def test_specific_case():
    expect= [
  [0, 1, 2, 3, 4, 5],
  [1, 1, 2, 3, 4, 5],
  [2, 2, 4, 6, 8, 10],
  [3, 3, 6, 9, 12, 15],
  [4, 4, 8, 12, 16, 20],
  [5, 5, 10, 15, 20, 25],
]
    result=multiplication_table(5)

    assert result==expect
