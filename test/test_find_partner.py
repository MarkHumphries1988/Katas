from src.find_partner.find_partner import find_partner

def test_no_directions_given_returns_empty_list():
    students = [
  ['Joe',  'David', 'Alex', 'Duncan', 'Cat', 'Verity'],
  ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']
]
    expect=[]
    result=find_partner(students,[])
    assert result==expect

def test_returns_values_when_moving_on_single_row():
    students=[["Mark","Simon","Kenny","Patrick"]]

    expect=["Simon"]

    result=find_partner(students,['right'])

    assert expect==result

    expect=["Simon","Kenny","Simon"]
    result=find_partner(students,["right","right","left"])

    assert expect==result

def test_loops_on_single_row():
    students=[["Mark","Simon","Kenny","Patrick"]]

    expect=["Simon","Kenny","Patrick","Mark"]

    result=find_partner(students,["right","right","right","right"])

    assert result==expect

    expect=["Patrick"]

    result=find_partner(students,["left"])

    assert result==expect

def test_move_up_or_down():
    students = [
  ['Joe',  'David', 'Alex', 'Duncan', 'Cat', 'Verity'],
  ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']
    ]

    expect=["Hev"]

    result=find_partner(students,["down"])

    assert expect==result

    expect=["Hev","Joe"]

    result=find_partner(students,["down","up"])

    assert expect==result

def test_cannot_go_above_top_or_belown_bottom():
    students = [
  ['Joe',  'David', 'Alex', 'Duncan', 'Cat', 'Verity'],
  ['Hev', 'Carrie', 'Heather', 'Johnathan',  'Katherine', 'Rayhaan']
]

    expect=['David']
    result= find_partner(students,['right','up','up'])

    assert result==expect

    expect=["Hev","Joe"]

    result=find_partner(students,["down","down","down","up","up"])

    assert result==expect