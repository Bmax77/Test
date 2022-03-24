from server.server_flask import *
# import server.server_flask
app.run(host='0.0.0.0', port=8080, debug=True)

# try:
#     web_dir = os.path.join(os.path.dirname(__file__), 'server')
#     os.chdir(web_dir)
#     handler_object = MyHttpRequestHandler
#     PORT = 8080
#     my_server = socketserver.TCPServer(("", PORT), handler_object)

#     # Star the server
#     print('Server started at PORT ', PORT)
#     my_server.serve_forever()
# except KeyboardInterrupt:
#     print('Server stopped')
#     my_server.socket.close()