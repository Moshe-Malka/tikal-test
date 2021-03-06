from datetime import datetime
from uuid import uuid4
from flask import Flask, abort, request, jsonify
from collections import OrderedDict 
import flask_monitoringdashboard as dashboard

flask_app = Flask(__name__)
dashboard.bind(flask_app)
dashboard.config.init_from(file='config.cfg')

messages = OrderedDict()
"""
messages = {
    "<recipient1>":[
        "message_id": "<uuid>",
        "ts": "<timestamp_of_receive>",
        "sender": "<sender1>",
        "message": "<messaage_data>"
    ],
    ...
}
"""

def put_message(recipient, content):
    try:
        if recipient in messages:
            messages[recipient].append(content)
        else:
            messages[recipient] = [content]
    except Exception as e:
        print(e)
        return jsonify(statusCode=500, error="Internal Server Error"), 500

@flask_app.route('/send', methods=['POST'])
def send():
    try:
        now = datetime.now()
        message_id = str(uuid4())
        data = request.get_json() # {sender, recipient, message}
        if set(data.keys()) != {"sender", "recipient", "message"}: raise Exception("Mismatch of params.")
        recipient = data['recipient']
        put_message(recipient, {
            'message_id': message_id,
            'ts': datetime.timestamp(now),
            'sender': data['sender'].lower(),
            'message': data['message']
        })
        return jsonify(statusCode=200, message="Received message successfully."), 200
    except Exception as e:
        print(e)
        return jsonify(statusCode=500, error="Internal Server Error"), 500

@flask_app.route('/receive/<recipient>', methods=['GET'])
def receive(recipient):
    try:
        return jsonify(statusCode=200, data=messages.get(recipient.lower(), [])), 200 
    except Exception as e:
        print(e)
        return jsonify(statusCode=500, error=str(e)), 500

if __name__ == '__main__':
    print("Starting...")
    flask_app.run(threaded=True, port=5000)
    
# TODO:
# 1) unit tests
# 2) Flask for rapid prototyping. an unopinionated library.
# 3) Monitoring: https://medium.com/flask-monitoringdashboard-turtorial/monitor-your-flask-web-application-automatically-with-flask-monitoring-dashboard-d8990676ce83#e43e
# 4) Scalling - use Kubernetes