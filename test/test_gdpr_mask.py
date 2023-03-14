from src.gdpr_mask.gdpr_mask import mask

def test_masks_single_unnested_as_decorator():
    def get_client_details():
        return {
        'name': 'Jane Smith',
        }
    
    assert get_client_details() == {'name':'Jane Smith'}

    @mask('name','age')
    def get_client_details():
        return {
        'name': 'Jane Smith',
        }

    
    assert get_client_details() == {'name':'**** *****'}

def test_masks_multiple_chosen_unnested():

    @mask('name','age')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'age': '18',
            'hair':'yes'
        }
    
    assert get_client_details()=={'name': '**** *****',
            'age': '**',
            'hair':'yes'}
    

def test_masks_nested_values():

    @mask('name', 'email', 'mobile')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }
    
    assert get_client_details()=={
        'name': '**** *****',
        'email': '*****************',
        'telephones': {
            'mobile': '***** ******'
        },
        'status': 'excellent'
}