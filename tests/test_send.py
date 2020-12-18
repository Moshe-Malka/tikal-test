import json
import pytest

def test_send(app, client):
    test_message = {
        "sender": "test_sender",
        "recipient": "test_recipient",
        "message":  "test message 123"
    }
    del app
    res = client.post('/send', 
                       data=test_message,
                       content_type='application/json')
    assert res.status_code == 200
    expected = {'statusCode':200, 'message':'Received message successfully.'}
    assert expected == json.loads(res.get_data(as_text=True))
    