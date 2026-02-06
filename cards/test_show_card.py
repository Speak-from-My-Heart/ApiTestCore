import pytest
from cards_requests import CardsReqests
from request_parameters import APIKeyProcessing
from card_test import ShouldCard

@pytest.mark.parametrize('api_key', [APIKeyProcessing.API_KEY_OWNER,
                                     APIKeyProcessing.API_KEY_ADMIN,
                                     APIKeyProcessing.API_KEY_ACCOUNTANT,
                                     APIKeyProcessing.API_KEY_GROUP_ADMIN,
                                     APIKeyProcessing.API_KEY_USER])
def test_can_give_status_code(api_key, rbac_func):
    endpoint_name = "show_card"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = CardsReqests().show_card(api_key)
    print(response.status_code)
    ShouldCard().should_be_correct_status_code(response, endpoint_name,role, rbac_func)
    #ShouldGetCard().should_be_correct_body(response)
    
@pytest.mark.parametrize('api_key', [APIKeyProcessing.API_KEY_OWNER,
                                     APIKeyProcessing.API_KEY_ADMIN,
                                     APIKeyProcessing.API_KEY_ACCOUNTANT,
                                     APIKeyProcessing.API_KEY_GROUP_ADMIN,
                                     APIKeyProcessing.API_KEY_USER])
def test_can_give_status_code_credential(api_key, rbac_func):
    endpoint_name = "show_card_credential"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = CardsReqests().show_card_credential(api_key)
    print(response.status_code)
    ShouldCard().should_be_correct_status_code(response, endpoint_name,role, rbac_func)
    #ShouldGetCard().should_be_correct_body(response)