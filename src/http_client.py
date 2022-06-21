import json
import logging
from urllib.parse import urlencode

import urllib3


def doConnect():
    http = urllib3.PoolManager()
    # plain text data
    print('\nGET\n')
    r = http.request('GET', 'http://httpbin.org/robots.txt')
    print(r.data)
    print(r.status)
    print(r.headers)

    # json data
    print('\nGET JSON\n')
    r = http.request('GET', 'http://httpbin.org/ip')
    print(json.loads(r.data.decode('utf-8')))

    # post json to server
    print('\nPOST JSON\n')
    data = {'attribute': 'value'}
    encoded_data = json.dumps(data).encode('utf-8')
    r = http.request(
        'POST',
        'http://httpbin.org/post',
        body=encoded_data,
        headers={'Content-Type': 'application/json'}
    )
    print(json.loads(r.data.decode('utf-8'))['json'])
    print(json.loads(r.data.decode('utf-8'))['headers'])

    print('\nQUERY STRING PARAMETERS\n')
    # query string parameters
    encoded_args = urlencode({'arg': 'value'})
    url = 'http://httpbin.org/post?' + encoded_args
    r = http.request('POST', url)
    print(json.loads(r.data.decode('utf-8'))['args'])

    print('\nEXCEPTIONS\n')
    try:
        http.request('GET', 'nx.example.com', retries=False)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')
