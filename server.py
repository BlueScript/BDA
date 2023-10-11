import xmlrpc.server
import os
f = open('client_text.txt','a')

def upload_file(file_contents):
    f.write(

    

def Hello(str):
    print(str)
server = xmlrpc.server.SimpleXMLRPCServer(("192.168.108.18", 8000))
server.register_function(Hello,"Hello")
server.register_function(upload_file, "upload_file")
print("Server listening on port 8000")
server.serve_forever()