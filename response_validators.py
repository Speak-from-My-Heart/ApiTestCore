from request_parameters import CardRequestsEnvironment

class ResponseValidators():
    def __init__ (self, card_request_environment: CardRequestsEnvironment):
        self.card_request_environment = card_request_environment

    def should_be_correct_body(self, response):
        missing_keys = self.card_request_environment.EXPECTED_TOP_LEVEL_ELEMENTS_GET_CARD - set(response.json())
        assert not missing_keys, f"Отсутствуют обязательные ключи: {', '.join(missing_keys)}"

    def should_be_correct_status_code(self, response, endpoint_name,role, rbac_func):
        Code = response.status_code
        Expected_code = rbac_func[endpoint_name][role]
        assert  Code == Expected_code, "Status code is not true"
