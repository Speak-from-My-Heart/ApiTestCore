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
    endpoint_name = "list_card"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    #response = CardsReqests().list_card(api_key)
    #print("Status:", response.status_code)
    #print("Headers:", response.headers)
    #print("Text:", response.text)
    response = CardsReqests().list_card(api_key)
    print(response.status_code)
    ShouldCard().should_be_correct_status_code(response, endpoint_name,role, rbac_func)