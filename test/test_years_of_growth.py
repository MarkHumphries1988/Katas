from src.years_of_growth.years_of_growth import years_of_growth



def test_starting_ending_same_means_zero_years():
    expected=0
    result=years_of_growth(2000,2000,2,12)
    assert expected==result

def test_one_year_of_growth():
    expected=1
    result=years_of_growth(2000,2200,10,20)
    assert expected==result

def test_full_migrants():
    expected=4
    result=years_of_growth(2000,2200,0,50)
    assert expected==result

def test_negative_migrants():
    expected=8
    result=years_of_growth(2000,3000,10,-100)
    assert expected==result

def test_md_case():
    expected=25
    result=years_of_growth(1000,2000,2,12)
    assert expected==result

