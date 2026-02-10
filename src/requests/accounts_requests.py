import requests
from src.request_parameters import AccountRequestsEnvironment, RequestParameters


class AccountsRequests(AccountRequestsEnvironment):
    def list_accounts(self, api_key: str):
        response = requests.get(
            RequestParameters.BASE_URL + AccountRequestsEnvironment.LIST_ACCOUNT,
            headers=RequestParameters().Constant_Headers(api_key),
        )
        return response
