import json
import os
import socket
import struct

from pprint import pprint

def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

with open('./aws_ip_ranges.json') as f:
    data = json.load(f)



prefixes = data['prefixes']


for key in prefixes:
  ip = key['ip_prefix'].split('/')[0]
  subnet = key['ip_prefix'].split('/')[1]
  print ( 'route ' + cidr_to_netmask(key['ip_prefix'])[0] + ' ' + cidr_to_netmask(key['ip_prefix'])[1] )
