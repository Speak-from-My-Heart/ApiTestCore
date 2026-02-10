import os

from dotenv import load_dotenv


class RequestParameters:
    BASE_URL = "https://private.elibrium.io/api/v2"

    def Constant_Headers(self, token: str):
        Headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        return Headers


class APIKeyProcessing:
    load_dotenv()
    API_KEY_OWNER = os.getenv("API_KEY_OWNER")
    API_KEY_ADMIN = os.getenv("API_KEY_ADMIN")
    API_KEY_GROUP_ADMIN = os.getenv("API_KEY_GROUP_ADMIN")
    API_KEY_ACCOUNTANT = os.getenv("API_KEY_ACCOUNTANT")
    API_KEY_USER = os.getenv("API_KEY_USER")

    role_map = {
        API_KEY_OWNER: "owner",
        API_KEY_ADMIN: "admin",
        API_KEY_ACCOUNTANT: "accountant",
        API_KEY_GROUP_ADMIN: "group_admin",
        API_KEY_USER: "user",
    }

    def role_by_API_KEY(self, key: str):
        role = APIKeyProcessing.role_map[key]
        return role


class AccountRequestsEnvironment:
    LIST_ACCOUNT = "/accounts"


class BalanceRequestsEnvironment:
    SHOW_BALANCE = "/balance"


class CardRequestsEnvironment:
    SHOW_CARD = "/cards/card_1pjnK6Okr9fUhNYBrniDTA0Y"
    UPDATE_CARD = "/cards/card_1pjnK6Okr9fUhNYBrniDTA0Y"
    LIST_CARD = "/cards"

    EXPECTED_TOP_LEVEL_ELEMENTS_GET_CARD = {
        "id",
        "title",
        "last_four",
        "bin",
        "currency",
        "available",
        "spend",
        "archived",
        "state",
        "limits",
        "date",
        "billing_address",
        "last_payment_at",
        "request_id",
    }

    BODY_SHOW_CARD = {"tz": "America/New_York"}

    BODY_SHOW_CARD_CREDENTIAL = {"tz": "America/New_York"}

    PARAMS_SHOW_CARD_CREDENTIAL = {"expand[]": "credentials"}

    BODY_LIST_CARD = {
        "tz": "America/New_York",
        "page": 1,
        "per_page": 50,
        "dates": {"begin": "2026-01-27", "end": "2026-01-28"},
        "archived": "include",
        "bins": ["428842"],
        "ids": ["card_139DNrJ27SznFp9uflKnQrr"],
        "last_fours": ["2222"],
        "states": [2],
    }

    BODY_UPDATE_CARD = {"tz": "America/New_York", "title": "Owner on API", "state": 2}


environment = CardRequestsEnvironment()
