from src.find_the_needle.find_the_needle import find_the_needle

haystack = {
	'name': "Northcoders",
	'description': "Awesome coding bootcamp",
	'staff': {
		'tutors': "James and Chris",
		'support': "Louise"
	},
	'contactDetails': {
		'web': "https://northcoders.com",
		'phone': "",
		'address': {
			'office': "Northcoders, Gold 67, The Sharp Project, Manchester",
			'postcode': "M40 5BJ"
		}
	},
	'reviews': {
		'april': {
			'chris': "I love Northcoders",
			'james': "It is awesome!"
		},
		'may': {
			'louise': "Northcoders is a fantastic coding bootcamp"
		}
	}
}

def test_if_not_in_haystack_returns_empty_list():
    assert find_the_needle(haystack,"Sausages")==[]

def test_returns_when_single_result_in_first_layer():
    ministack={'name':'Northcoders'}
    assert find_the_needle(ministack,'Northcoders')==['name']

def test_ingores_case():
    ministack={'name':'Northcoders'}
    assert find_the_needle(ministack,'northcoders')==['name']

def test_returns_when_layer_contains_multiple():
    ministack={'name':'Northcoders', 'description':'Awesome'}
    assert find_the_needle(ministack,'awesome')==['description']

def test_returns_when_not_whole_string():
    ministack={'name':'Northcoders', 'description':'Awesome'}
    assert find_the_needle(ministack,'weso')==['description']

def test_returns_when_second_layer():
    ministack = {
	'name': "Northcoders",
	'description': "Awesome coding bootcamp",
	'staff': {
		'tutors': "James and Chris",
		'support': "Louise"
	},}
    assert find_the_needle(ministack,'Louise')==["staff.support"]

def test_returns_when_n_layers():
    assert find_the_needle(haystack,'m40')==['contactDetails.address.postcode']

def test_returns_multiple_results_alphabetically():
    assert find_the_needle(haystack,"NorThcOdErs")==["contactDetails.address.office", "contactDetails.web", "name", "reviews.april.chris", "reviews.may.louise"]

