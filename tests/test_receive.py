import json
import pytest

def test_receive(app, client):
    del app
    res = client.get('/receive/test_recipient')
    assert res.status_code == 200
    expected = 200
    assert expected == json.loads(res.get_data(as_text=True))['statusCode']