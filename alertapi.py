#!/usr/bin/env python

from flask import Flask
from flask import jsonify
from flask import request
import requests
import json
import requests

import urllib
import time

aurl = 'http://mon.qiniu.io/Alertapi'

app = Flask(__name__)


def postinfo(payload):
    headers = {"Content-type": "application/json; charset=UTF-8"}
    r = requests.post(aurl, data=json.dumps(payload), headers=headers)
    return r.text


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/alert/jkb', methods=['POST'])
def jkb_alert():
    str_body = {}
    msg = request.form
    str_body['alertstatus'] = msg['message_status']
    str_body['statuscode'] = msg['message_status']
    str_body['messageid'] = msg['task_id']
    str_body['alertitem'] = msg['task_summary']
    str_body['alertsource'] =  "JKB"
    str_body['alerttime'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(msg['fault_time'])))
    str_body['alerthost'] = msg['task_name'].decode('utf-8')
    str_body['alertmsg'] = urllib.unquote(str(msg['content']))
    print str_body
    postinfo(str_body)
    return "yes", 200

if __name__ == '__main__':
    app.run()
