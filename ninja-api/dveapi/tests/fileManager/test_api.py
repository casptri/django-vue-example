import json
import requests
import logging
from pathlib import Path

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

def test_upload_string():
    url = "http://localhost:3001/file/file"
    files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
    r = requests.post(url, data={'filename': "test.txt" , "msg":"hello" ,"type" : "multipart/form-data"}, files=files)
    r.text

def test_upload(tmp_path):
    url = "http://127.0.0.1:3001/file/file"
    url = "http://localhost:3001/file/file"

    test_file = tmp_path / "up.txt"
    with test_file.open('w') as f:
        f.write("Hello Upload\n")

    #headers = {'accept': "*/*",'Content-Type': 'multipart/form-data',}
    with test_file.open('rb') as f:
        #file = [('file', ('test.txt', f, 'text/txt'))]
        file = { 'file': ('test.txt', f), 'type': 'text/txt'}
        #response = requests.request("POST", url, files=file)
        test_response = requests.post(url,  files = {"form_field_name": f})

        #response = requests.request("POST", url, headers=headers, files=file)
        #requests.post(url, data={'file': ('test.txt',f)}, headers=headers)

    logging.warning(test_file)
