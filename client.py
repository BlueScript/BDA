import xmlrpc.client
import sys
import re
import os
proxy = xmlrpc.client.ServerProxy("http://192.168.108.41:8000/")
file1 = 'data.txt'

os.system("type data.txt | python map.py | sort | python reduce.py ")
for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words= line.split()
    for word in words:
        proxy.upload_file(word)









    




    