import pytest
from fastapi.testclient import TestClient

from churn.service.app import app


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def good_row():
    return {
        "CreditScore": 650,
        "Geography": "France",
        "Gender": "Female",
        "Age": 42,
        "Tenure": 3,
        "Balance": 100000.0,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 75000.0,
    }
