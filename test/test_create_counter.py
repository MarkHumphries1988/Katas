from src.create_counter.create_counter import create_counter

def test_returns_a_dictionary():
    expected=type({'a':0,'b':0})
    result=create_counter(10)
    
    assert type(result)==expected

def test_returns_functions_in_dict():
    def tinyfunc():
        pass

    expected=type(tinyfunc)
    result=create_counter(10)

    assert type(result["up"])==expected
    assert type(result["down"])==expected

def test_functions_can_be_invoked_to_change_value():
    counter=create_counter(10)
    up=counter["up"]
    down=counter["down"]

    first=up()
    up()
    second=up()
    down()
    down()
    third=down()

    assert first==11
    assert second==13
    assert third==10



