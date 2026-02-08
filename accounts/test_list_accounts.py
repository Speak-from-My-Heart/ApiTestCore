import pytest
from accounts_requests import AccountsRequests
from request_parameters import APIKeyProcessing
from response_validators import ResponseValidators

@pytest.mark.parametrize('api_key', [APIKeyProcessing.API_KEY_OWNER,
                                     APIKeyProcessing.API_KEY_ADMIN,
                                     APIKeyProcessing.API_KEY_ACCOUNTANT,
                                     APIKeyProcessing.API_KEY_GROUP_ADMIN,
                                     APIKeyProcessing.API_KEY_USER])
def test_can_give_status_code(api_key, rbac_func):
    endpoint_name = "list_accounts"
    role = APIKeyProcessing().role_by_API_KEY(api_key)
    response = AccountsRequests().list_accounts(api_key)
    print(response.status_code)
    ResponseValidators().should_be_correct_status_code(response, endpoint_name,role, rbac_func)