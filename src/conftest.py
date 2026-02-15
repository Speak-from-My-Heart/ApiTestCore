import csv

import pytest

from src.request_parameters import environment
from src.response_validators import ResponseValidators


@pytest.fixture(scope="session")
def rbac_func():
    data = {}
    with open("src/matrix_role.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            endpoint = row.pop("endpoint_name")
            data[endpoint] = {k: int(v) for k, v in row.items()}

    yield data


@pytest.fixture(scope="module")
def validators():
    yield ResponseValidators(card_request_environment=environment)
