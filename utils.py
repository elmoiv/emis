import json, os, re
from datetime import datetime as d
from constants import *

def get_input(label):
    x = ''
    while x == '':
        x = input(label)
    return x

def get_credentials():
    if not os.path.exists(JSON_FILE):
        d = {
            JSON_K_ID: get_input('Teacher ID: '),
            JSON_K_NAT: get_input('National ID: '),
            JSON_K_PASS: get_input('Password: ')
        }
        json.dump(d, open(JSON_FILE, 'w'))
    
    json_raw = open(JSON_FILE)
    dct = json.load(json_raw)
    
    return dct

def get_payload_value(html, key):
    res = re.findall(rf'id="{key}".*?"(.*?)"', html)
    return res[0] if res else None

def update_payload(payload: dict, update_dict: dict):
    for key, value in update_dict.items():
        payload[key] = value
    return payload

def pretty_date():
    return re.sub(
            r'[-:]', '',
            str(d.now())
        ).replace(' ', '_').split('.')[0]