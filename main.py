#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path,time
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import tornado.escape
import tornado.netutil
import tornado.ioloop
import socket
import json

# my own import start
# my own import end
ISOTIMEFORMAT='%Y-%m-%d %X'

define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class AlertapiHandler(tornado.web.RequestHandler):
    def post(self):
        a=[]
        params = self.request.body.decode('utf-8')
        data = json.loads(params)
        print (data)
        self.write("OK")



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",           IndexHandler),
        (r"/Alertapi",      AlertapiHandler)

        ]



        settings = {
   "upload_path":os.path.join(os.path.dirname(__file__),'files'),
   "static_path": os.path.join(os.path.dirname(__file__), "static"),
   "template_path":os.path.join(os.path.dirname(__file__), "templates")
    }

        tornado.web.Application.__init__(self,handlers,**settings)
def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




if __name__ == "__main__":
    main()
