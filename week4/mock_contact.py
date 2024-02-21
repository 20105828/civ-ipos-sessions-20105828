from unittest.mock import Mock

class Contact:
    def __init__(self, name, address, billing_details):
        self.name = name
        self.address = address
        self.billing_details = billing_details

def get_contact_info(name);
    pass

def test_get_contact_info():
    # Mock the contact result from the API call
    get_contact_info = Mock(return_value=Contact(
        name="John Doe",
        address={'city': 'Perth', 'State': 'WA', 'zip': '6001'},
        billing_details={'card_type': 'VISA', 'expiration_date': '12/25'}
    ))

result = get_contact_info('John Doe')

assert result.name == "John Doe"
assert result.address == {'city': 'Perth', 'State': 'WA', 'zip': '6001'}
assert result.billing_details == {'card_type': 'VISA', 'expiration_date': '12/25'}
