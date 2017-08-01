# Reference :
# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#
import requests
import threading
import json
import random

url = 'http://localhost:8080/calculator/operation'
head = {"Content-type": "application/json"}


def sendrequest():
  threading.Timer(10.0, sendrequest).start()
  operation_payload = {
      "operand1": random.randint(1,9),
      "operand2": random.randint(0,9),
      "operation": random.choice(['add','sub','mul','div']),

  }
  op = json.dumps(operation_payload)

  ret = requests.post(url, headers = head, data = op)

sendrequest()
