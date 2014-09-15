import os
import json
from urllib2 import urlopen
from contextlib import closing


def load_config():
    with closing(urlopen(os.environ['CONFIG_URL'])) as fh:
        return json.load(fh)


def validate_config():
    load_config()
