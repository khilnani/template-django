import os
import json
import yaml
from urllib2 import urlopen
from contextlib import closing

def load_config():
    config_file = os.environ['CONFIG_URL']
    with closing(urlopen( config_file )) as f:
        if config_file.endswith('.yaml'):
            return yaml.load(f)
        elif config_file.endswith('.json'):
            return json.load(f)
        else:
            return None

def validate_config():
    load_config()
