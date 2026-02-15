import pytest

from src.request_parameters import APIKeyProcessing, environment
from src.requests.cards_requests import CardsReqests


@pytest.mark.parametrize(
    "api_key",
    [
        APIKeyProcessing.API_KEY_OWNER,
        APIKeyProcessing.API_KEY_ADMIN,
        APIKeyProcessing.API_KEY_ACCOUNTANT,
        APIKeyProcessing.API_KEY_GROUP_ADMIN,
        APIKeyProcessing.API_KEY_USER,
    ],
)
def test_can_give_status_code(validators, api_key: str, rbac_func: dict):
    endpoint_name = "show_card"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = CardsReqests(card_request_environment=environment).show_card(api_key)
    print(response.status_code)
    validators.should_be_correct_status_code(response, endpoint_name, role, rbac_func)
    # ShouldGetCard().should_be_correct_body(response)


@pytest.mark.parametrize(
    "api_key",
    [
        APIKeyProcessing.API_KEY_OWNER,
        APIKeyProcessing.API_KEY_ADMIN,
        APIKeyProcessing.API_KEY_ACCOUNTANT,
        APIKeyProcessing.API_KEY_GROUP_ADMIN,
        APIKeyProcessing.API_KEY_USER,
    ],
)
def test_can_give_status_code_credential(validators, api_key: str, rbac_func: dict):
    endpoint_name = "show_card_credential"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = CardsReqests(card_request_environment=environment).show_card_credential(
        api_key
    )
    print(response.status_code)
    validators.should_be_correct_status_code(response, endpoint_name, role, rbac_func)
    # ShouldGetCard().should_be_correct_body(response)
