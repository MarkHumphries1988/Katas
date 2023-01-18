import math
def get_century(year):
    if year%100 ==0:
        year=year+1

    century= math.ceil(year/100)

    if century % 10 == 1 and century % 100 != 11:
        return f'{century}st'
  
    if century % 10 == 2 and century % 100 != 12:
        return f'{century}nd'
  
    if century % 10 == 3 and century % 100 != 13:
        return f'{century}rd'
  
    return f'{century}th'




    pass
