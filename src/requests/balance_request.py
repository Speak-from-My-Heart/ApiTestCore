import requests
from src.request_parameters import RequestParameters, BalanceRequestsEnvironment

class BalanceReqests(BalanceRequestsEnvironment):
    def show_balance(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + BalanceRequestsEnvironment.SHOW_BALANCE,
            headers = RequestParameters().Constant_Headers(api_key)
        ) 
        return response