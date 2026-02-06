import pytest
import csv


@pytest.fixture(scope="session")
def rbac_func():
    data = {}
    with open("matrix_role.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            endpoint = row.pop("endpoint_name")
            data[endpoint] = {k: int(v) for k, v in row.items()}

    return data