import json

def config(config_file):
    with open(config_file) as f:
        data = f.read()

    # reconstructing the data as a dictionary
    js = json.loads(data)
    return js

