import pytest

from src.request_parameters import APIKeyProcessing, environment
from src.requests.cards_requests import CardsReqests
from src.response_validators import ResponseValidators


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
def test_can_give_status_code(api_key: str, rbac_func: dict):
    endpoint_name = "list_card"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = CardsReqests(card_request_environment=environment).list_card(api_key)
    print(response.status_code)
    ResponseValidators(
        card_request_environment=environment
    ).should_be_correct_status_code(response, endpoint_name, role, rbac_func)
