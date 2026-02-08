import requests
from request_parameters import RequestParameters, CardRequestsEnvironment

class CardsReqests(CardRequestsEnvironment):
    def show_card(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + CardRequestsEnvironment.SHOW_CARD,
            headers = RequestParameters().Constant_Headers(api_key),
            json = CardRequestsEnvironment.BODY_SHOW_CARD
        ) 
        return response
    
    def show_card_credential(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + CardRequestsEnvironment.SHOW_CARD,
            headers = RequestParameters().Constant_Headers(api_key),
            json = CardRequestsEnvironment.BODY_SHOW_CARD_CREDENTIAL,
            params = CardRequestsEnvironment.PARAMS_SHOW_CARD_CREDENTIAL
        ) 
        return response
    
    def list_card(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + CardRequestsEnvironment.LIST_CARD,
            headers = RequestParameters().Constant_Headers(api_key),
            json = CardRequestsEnvironment.BODY_LIST_CARD
        ) 
        return response
    
    def update_card(self, api_key):
        response = requests.put(
            RequestParameters.BASE_URL + CardRequestsEnvironment.UPDATE_CARD,
            headers = RequestParameters().Constant_Headers(api_key),
            json = CardRequestsEnvironment.BODY_UPDATE_CARD
        ) 
        return response
    