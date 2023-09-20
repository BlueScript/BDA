from xmlrpc.server import SimpleXMLRPCServer

filec = len(open("data.txt").read().split(" "))

def add(num):
    return num + filec

if __name__ == '__main__':
    s = SimpleXMLRPCServer(('192.168.108.204',8080))
    s.register_function(add)
    s.serve_forever()