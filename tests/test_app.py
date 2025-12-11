import sys
from pathlib import Path

# Ensure project root is on sys.path so tests can import app when pytest runs from the
# tests folder or from a different working directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_json_endpoint(client):
    payload = {"message": "Hello to all worlds!", "name": "Ishaan G"}
    resp = client.post('/api/v1/hello/json', json=payload)
    assert resp.status_code == 200
    assert resp.get_json() == payload


def test_xml_endpoint(client):
    payload = {"message": "Hello to all worlds!", "name": "Ishaan G"}
    resp = client.post('/api/v1/hello/xml', json=payload)
    assert resp.status_code == 200
    text = resp.get_data(as_text=True)
    assert '<xmlroot>' in text
    assert '<message>Hello to all worlds!</message>' in text
    assert '<name>Ishaan G</name>' in text
