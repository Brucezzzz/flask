#!/usr/bin/env python
# coding: utf-8

# In[36]:


from __future__ import print_function
from flask import Flask
from collections import OrderedDict
import socket
import json

app = Flask(__name__)
@app.route('/status')

def hostname_Ip():
    name = socket.gethostname()
    return name

def Ip_address():
    name = socket.gethostname()
    ip_address = socket.gethostbyname(name)
    return ip_address
    
def cpus():
    i = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            i += 1
    return i

def memory():
    with open('/proc/meminfo') as g:
        for line in g:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return("memory:{0}".format(meminfo['MemTotal']))

status = {"hostname":hostname_Ip(), "ip_address":Ip_address(), "cpus":cpus(),"memory":memory() }
json_status = json.dumps(status)
print(json_status)
    

