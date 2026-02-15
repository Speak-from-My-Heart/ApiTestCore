import pytest

from src.request_parameters import APIKeyProcessing
from src.requests.balance_request import BalanceReqests


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
    endpoint_name = "show_balance"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = BalanceReqests().show_balance(api_key)
    print(response.status_code)
    validators.should_be_correct_status_code(response, endpoint_name, role, rbac_func)
    # ShouldGetCard().should_be_correct_body(response)
