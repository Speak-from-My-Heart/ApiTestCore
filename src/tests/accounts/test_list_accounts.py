import pytest

from src.request_parameters import APIKeyProcessing
from src.requests.accounts_requests import AccountsRequests


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
    endpoint_name = "list_accounts"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = AccountsRequests().list_accounts(api_key)
    print(response.status_code)
    validators.should_be_correct_status_code(response, endpoint_name, role, rbac_func)
