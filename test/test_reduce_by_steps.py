from src.reduce_by_steps.reduce_by_steps import reduce_by_steps

def test_simple_addition_binfunc_with_ones_array():
    def add(a,b):
        return a+b
    list=[1,1,1,1,1,1,1]

    expect=len(list)
    result=reduce_by_steps(add,list,0)

    assert expect==result

def test_zero_elements_returns_initial():
    def add(a,b):
        return a+b
    list=[]
    expect=0
    result=reduce_by_steps(add,list,0)

    assert expect==result

def test_simple_add_moves_by_initial():
    def add(a,b):
        return a+b
    list=[1,1,1,1,1,1,1]

    expect=len(list)+7
    result=reduce_by_steps(add,list,7)

    assert expect==result

def test_examples():
    def multiply(num1,num2):
        return num1 * num2

    numbers = [5, 5]
    initial_value = 0

    expect=25
    result=reduce_by_steps(multiply, numbers, initial_value)
    assert result==25

    def make_sentence(str1,str2):
        return f"{str1} {str2}"

    words = ['Let\'s', 'get', 'down', 'to', 'business']
    initial_value = ''

    expect="Let's get down to business"
    result=reduce_by_steps(make_sentence, words, initial_value) 

    assert expect==result