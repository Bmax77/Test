#!/bin/env python3
import os
import socketserver
import http.server
from urllib.parse import urlparse, parse_qs, unquote, urlsplit
import urllib.parse as urllib


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        if self.path == '/health/readiness':
            self.send_response(200)
            self.send_header('mimetype', 'text/text')
            self.end_headers()
            self.wfile.write(str("Ready").encode())
            return
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    try:
        handler_object = MyHttpRequestHandler
        PORT = 8080
        my_server = socketserver.TCPServer(("", PORT), handler_object)

        # Star the server
        print('Server started at PORT ', PORT)
        my_server.serve_forever()
    except KeyboardInterrupt:
        print('Server stopped')
        my_server.socket.close()
