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
import uuid

__author__ = 'Muevy S.A.'

# -- [ Settings Parser ] --------------------------------------------------------------------
CONTEXT = os.getenv('MUEVY_API_CONTEXT', 'SANDBOX')


# -- [Request Payload] -------------------------------------------------

payload  = json.loads('''
{
"user_trace_id": "3cc9dfd2-2efc-4551-a05a-32fc4488d24e",
"prod_code": "'BFC001'",
"dst_amount": 0.04,
"src_amount": 0.21,
"bin_num": "404132",
"cur_code": "EUR",
"sender_reference": "311577288",
"sender_name": "Lucas Martins ",
"sender_address": "Rua da Paz 123",
"sender_city": "Barueri",
"sender_state": "SP",
"sender_country": "BRA",
"recipient_fullname": "ANDRE COSTA",
"recipient_pan": "4779890032407152",
"recipient_country_code": "PRT",
"card_acceptor_id": "Muevy10078252BR",
"card_acceptor_name": "Test Muevy",
"card_acceptor_city": "Barueri",
"card_acceptor_state": "SP",
"card_acceptor_country": "BRA",
"card_acceptor_zip": "06454000"
}
''')


try:
    config      = configparser.ConfigParser()
    config.read('config.cfg')

    DEBUG       = config[CONTEXT]['debug']
    BASE_URL    = config[CONTEXT]['base_url']
    API_KEY     = config[CONTEXT]['api_key']
    TIMEOUT     = config[CONTEXT]['timeout']
    URL         = BASE_URL + '/transactionsend'

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
print ("######################## Muevy Transaction Rate Method       #######################")
print ("####################################################################################\n")

print("\n=== [Context Information] ==========================================================")
print ("Context         : ", CONTEXT)
print ("Base URL        : ", BASE_URL) 
print ("API Key         : ", API_KEY)
print ("Endpoint URL    : ", URL)

print("\n=== [Payload Request] ==============================================================")

show      = json.dumps(payload, indent=2)
s_headers = json.dumps(headers, indent=2)

print("Headers:", s_headers)
print("Payload:", show)

response         = None

try:
    ini_time = time.time()
    response = requests.post(URL,
                          #cert = (cert, key),
                          headers=headers,
                          json = payload,
                          timeout=int(TIMEOUT)
                        )

    end_time = time.time()

except Exception as e:
    print (e)


print("\n=== Muevy Response ===============================================================")

status           = response.status_code
headers          = response.headers
response         = response.json()

print("Status: ", status)

print("--- Response Headers ----------------")
pprint(dict(headers))

print("--- Response Payload -----------")
pprint(response)

print("\nRuntime Ini: {} End: {} Total {} - Status: {}".format(ini_time, end_time, end_time - ini_time, status))
