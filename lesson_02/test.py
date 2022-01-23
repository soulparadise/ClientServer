import json


try:
    with open('orders.json', 'r') as json_obj:
        old_data = json.load(json_obj)
except json.decoder.JSONDecodeError:
    with open('orders.json', 'w') as json_obj:
        json.dump({}, json_obj, indent=4)
