from _pytest.fixtures import yield_fixture
import pytest
import json

import sys
sys.path.append(".")
from my_flask import app


@pytest.fixture
def client():
  client = app.test_client()

  yield client

def test_healthcheck_ok(client):
  rst = client.post('/', data=dict(
    id=88888888,
  ), follow_redirects=True)
  assert 'ok' in json.loads(rst.data.decode("utf-8"))['status']

def test_healthcheck_error(client):
  rst = client.post('/', data=dict(
  ), follow_redirects=True)
  assert 'error' in json.loads(rst.data.decode("utf-8"))['status']

def test_healthcheck_get(client):
  rst = client.get('/', data=dict(
  ), follow_redirects=True)
  assert 'error' in json.loads(rst.data.decode("utf-8"))['status']