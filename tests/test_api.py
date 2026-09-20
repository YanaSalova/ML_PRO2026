def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert "model_version" in r.json()


def test_ready(client):
    assert client.get("/ready").status_code == 200


def test_bad_tenure_is_422(client, good_row):
    r = client.post("/v1/predict", json={**good_row, "Tenure": -1})
    assert r.status_code == 422


def test_missing_field_is_422(client, good_row):
    row = dict(good_row)
    del row["CreditScore"]
    assert client.post("/v1/predict", json=row).status_code == 422


def test_extra_field_is_422(client, good_row):
    r = client.post("/v1/predict", json={**good_row, "hacker_field": 1})
    assert r.status_code == 422


def test_unknown_geography_is_422(client, good_row):
    r = client.post("/v1/predict", json={**good_row, "Geography": "Unknown"})
    assert r.status_code == 422


def test_model_matches_api_schema(client):
    from churn.service.app import Features, app

    assert set(app.state.meta["features"]) == set(Features.model_fields)
    assert app.state.version == "bank-random-forest-1.0"
