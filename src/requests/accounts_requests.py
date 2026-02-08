import requests
from src.request_parameters import RequestParameters, AccountRequestsEnvironment

class AccountsRequests(AccountRequestsEnvironment):
    def list_accounts(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + AccountRequestsEnvironment.LIST_ACCOUNT,
            headers = RequestParameters().Constant_Headers(api_key),
        ) 
        return response