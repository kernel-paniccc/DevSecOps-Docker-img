import pytest

from app import app as flask_app


@pytest.fixture()
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as client:
        yield client



def test_index_returns_message(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello from CI test app!"


def test_health_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_echo_requires_msg(client):
    resp = client.get("/echo")
    data = resp.get_json()
    assert resp.status_code == 400
    assert data["error"] == "msg query param is required"
    assert data["echo"] == ""
    assert data["length"] == 0


def test_echo_returns_payload(client):
    resp = client.get("/echo?msg=hey")
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["echo"] == "hey"
    assert data["length"] == 3
