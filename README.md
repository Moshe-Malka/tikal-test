# Tikal Assignment

Hi ! this is an assignment. i was given for a job interview.

the requirements were:

Write a microservice in any language or framework of your choice.

The microservice will be a messaging app between people.

2 endpoints:

1) Send Message

2) Receive Message

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
git clone https://github.com/Moshe-Malka/tikal-test.git
pip install -r requirements.txt
```

## Usage

```bash
python3 app.py
```

To send a message:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"sender": "<sender_name>", "recipient": "<recipient_name>", "message": "Hello!"}' http://127.0.0.1:5000/send
```

to receive all messages for a specific recipient:

```bash
curl POST -X GET http://127.0.0.1:5000/receive/<recipient_name>
```