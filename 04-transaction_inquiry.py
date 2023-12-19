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
from ast import literal_eval
import os
import sys
import configparser
import time
from pprint import pprint


__author__ = 'Muevy S.A.'


# -- [ Settings Parser ] --------------------------------------------------------------------
CONTEXT = os.getenv('MUEVY_API_CONTEXT', 'SANDBOX')


# -- [Request Payload] -------------------------------------------------
payload = json.loads('''
{
"user_trace_id" : "8cae7a23-0944-40b0-893b-aa611397ae45",
"prod_code"     : "CPC001",
"muevy_transaction_id": "d989956e-d8fc-4789-8e57-47fe89f45a3d"
}
''')

# -- [ Settings Parser ] --------------------------------------------------------------------
DEBUG=False

try:
    config      = configparser.ConfigParser()
    config.read('config.cfg')

    DEBUG       = config[CONTEXT]['debug']
    BASE_URL    = config[CONTEXT]['base_url']
    API_KEY     = config[CONTEXT]['api_key']
    TIMEOUT     = config[CONTEXT]['timeout']
    URL         = BASE_URL + '/transactioninquiry'

except Exception as e:
    print (e)

DEBUG = DEBUG.lower() in ['true', 'yes', 'y', '1', 'ok']


# -- [ Payload Prepare ] -----------------------------------------------------------------

headers = { "Content-Type" : "application/json",
            'Accept'       : 'application/json',
            'X-Api-Key'    : API_KEY
            }

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
print ("######################## Muevy Transaction Inquiry Method    #######################")
print ("####################################################################################\n")

print("\n=== [Context Information] ==========================================================")
print ("Context         : ", CONTEXT)
print ("Base URL        : ", BASE_URL) 
print ("API Key         : ", API_KEY)
print ("Endpoint URL    : ", URL)

print("\n=== [Payload Request] ==============================================================")

print("Headers:", json.dumps(headers, indent=2))
print("Payload:", json.dumps(payload, indent=2))

response         = None

try:
    ini_time = time.time()
    response = requests.post(URL,
                          headers=headers,
                          json = payload,
                          timeout=int(TIMEOUT)
                        )

    end_time = time.time()

except Exception as e:
    print (e)


status           = response.status_code
headers          = response.headers
response         = response.json()

print("\n=== [Muevy Response] ===============================================================")
print("Status: ", status)

print("--- Response Headers ------")
pprint(dict(headers))

print("\n--- Response Payload --------\n")
pprint(response)

print("\nRuntime Ini: {} End: {} Total {} - Status: {}".format(ini_time, end_time, end_time - ini_time, status))
