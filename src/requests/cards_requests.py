import requests
from src.request_parameters import CardRequestsEnvironment, RequestParameters


class CardsReqests:
    def __init__(self, card_request_environment: CardRequestsEnvironment):
        self.card_request_environment = card_request_environment

    def show_card(self, api_key):
        response = requests.get(
            RequestParameters.BASE_URL + self.card_request_environment.SHOW_CARD,
            headers=RequestParameters().Constant_Headers(api_key),
            json=self.card_request_environment.BODY_SHOW_CARD,
        )
        return response

    def show_card_credential(self, api_key: str):
        response = requests.get(
            RequestParameters.BASE_URL + self.card_request_environment.SHOW_CARD,
            headers=RequestParameters().Constant_Headers(api_key),
            json=self.card_request_environment.BODY_SHOW_CARD_CREDENTIAL,
            params=self.card_request_environment.PARAMS_SHOW_CARD_CREDENTIAL,
        )
        return response

    def list_card(self, api_key: str):
        response = requests.get(
            RequestParameters.BASE_URL + self.card_request_environment.LIST_CARD,
            headers=RequestParameters().Constant_Headers(api_key),
            json=self.card_request_environment.BODY_LIST_CARD,
        )
        return response

    def update_card(self, api_key: str):
        response = requests.put(
            RequestParameters.BASE_URL + self.card_request_environment.UPDATE_CARD,
            headers=RequestParameters().Constant_Headers(api_key),
            json=self.card_request_environment.BODY_UPDATE_CARD,
        )
        return response
