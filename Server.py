import os
import socketserver
from urllib import response

class CustomHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global response

        data = self.request.recv(1024)
        # Decode client message to string
        parsed = data.decode("utf8")

        print(parsed)
        if(parsed == ":Login"):
            response = ":LoginOK"
            self.request.sendall(str.encode(response))

if __name__ == "__main__":
    HOST, PORT = "192.168.0.2", 8090
    # os.getenv('IP'),os.getenv('PORT') 
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to IP:Port
    server = socketserver.TCPServer((HOST, PORT), CustomHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
