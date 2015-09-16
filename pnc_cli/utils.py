import ConfigParser
import random
import string
import re
import errno
import swagger_client
import os

__author__ = 'thauser'

config = ConfigParser.ConfigParser()
configfilename = os.path.expanduser("~")+ "/.config/pnc-cli/pnc-cli.conf"
configdirname = os.path.dirname(configfilename)
try:
    os.makedirs(configdirname)
except OSError, e:
    if e.errno != errno.EEXIST:
        raise
found = config.read(os.path.join(configfilename))
if not found:
    config.add_section('PNC')
    config.set('PNC', 'restEndpoint', 'http://localhost:8080/pnc-rest/rest')
    with open(os.path.join(configfilename),'wb') as configfile:
        config.write(configfile)
pnc_rest_url = config.get('PNC', 'restEndpoint').rstrip('/')
apiclient = swagger_client.api_client.ApiClient(pnc_rest_url)

def get_api_client():
    return apiclient

def gen_random_name():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

def gen_random_version():
    return random.choice(string.digits)+'.'+random.choice(string.digits)

def is_valid_version(version):
    pattern = re.compile('\d*\.\w*')
    return pattern.match(version)