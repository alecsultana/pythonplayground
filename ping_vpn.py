import urllib2
import time
import json

from pprint import pprint

url = "https://httpstatuses.com"

while True:
    time.sleep(5)
    result = urllib2.urlopen(url)
    print(result.getcode())
    payloadResult = result.read();
    payloadResult = json.loads(payloadResult)
    print('--------------')
