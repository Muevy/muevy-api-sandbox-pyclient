#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import logging
import unittest
import base64
import json
import sys
import os
import datetime
import random 
import os
import sys
import configparser
import time
import uuid
from pprint import pprint

__author__ = 'Muevy S.A.'

# -- [ Settings Parser ] --------------------------------------------------------------------
CONTEXT = os.getenv('MUEVY_API_CONTEXT', 'SANDBOX')

try:
    config      = configparser.ConfigParser()
    config.read('config.cfg')

    DEBUG       = config[CONTEXT]['debug']
    BASE_URL    = config[CONTEXT]['base_url']
    API_KEY     = config[CONTEXT]['api_key']
    TIMEOUT     = config[CONTEXT]['timeout']
    URL         = BASE_URL + '/check'

except Exception as e:
    print (e)

DEBUG = DEBUG.lower() in ['true', 'yes', 'y', '1', 'ok']


# -- [ Header Prepare ] -----------------------------------------------------------------

headers = { "Content-Type" : "application/json",
            'Accept'       : 'application/json',
            'X-Api-Key'    : API_KEY,
            }


# Create a unique request number reference
trace_id = str(uuid.uuid4())


payload = json.loads('''
{
"user_trace_id" : "'''+ trace_id + '''"
}
''')

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
if DEBUG: http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
if DEBUG:
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
else:
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(False)
    requests_log.propagate = False


print ("####################################################################################")
print ("######################## Muevy Check Method                  #######################")
print ("####################################################################################\n")

print("\n=== [Context Information] ==========================================================")
print ("Context         : ", CONTEXT)
print ("Base URL        : ", BASE_URL) 
print ("Endpoint URL    : ", URL)

print("\n=== [Payload Request] ==============================================================")

print("Headers: ", json.dumps(payload, indent=2))
print("Payload:",  json.dumps(headers, indent=2))

response         = None

try:
    ini_time = time.time()
    response = requests.post(URL,
                          headers = headers,
                          timeout=int(TIMEOUT)
                        )

    end_time = time.time()

except Exception as e:
    print (e)


print("\n=== [Muevy Response] ===============================================================")
print("Status: ", response.status_code)

print("\nHeaders:")
pprint(dict(response.headers))

print("\nResponse Payload:")
pprint(response.json())

print("\nRuntime Ini: {} End: {} Total {}".format(ini_time, end_time, end_time - ini_time))

