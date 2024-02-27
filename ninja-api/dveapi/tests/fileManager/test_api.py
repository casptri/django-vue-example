import json
import requests
import logging


class AccessHandler:
    base_url = "http://127.0.0.1:3001"

def test_set():
    payload = {'var0': 'hello', 'var1': "world"}
    url = "http://127.0.0.1:3001/file/set/test.toml"
    r = requests.post(url, json=payload)
    if r.status_code != 200:
        logging.warning(r.status_code)
        logging.error("Access denied")
        assert False
    acc_data = json.loads(r.text)
    logging.warning(acc_data)
