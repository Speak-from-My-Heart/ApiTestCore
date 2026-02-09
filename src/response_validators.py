from src.request_parameters import CardRequestsEnvironment

class ResponseValidators():
    def __init__ (self, card_request_environment: CardRequestsEnvironment):
        self.card_request_environment = card_request_environment

    def should_be_correct_body(self, response: dict):
        missing_keys = self.card_request_environment.EXPECTED_TOP_LEVEL_ELEMENTS_GET_CARD - set(response.json())
        assert not missing_keys, f"Отсутствуют обязательные ключи: {', '.join(missing_keys)}"

    def should_be_correct_status_code(self, response: dict, endpoint_name: str, role: str, rbac_func: dict):
        code = response.status_code
        expected_code = rbac_func[endpoint_name][role]
        assert  code == expected_code, "Status code is not true"
