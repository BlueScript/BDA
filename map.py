# f1 = open('data.txt').read().split()
import sys
import re

for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words = line.split()
    
    for word in words:
        print('{}\t{}'.format(word,1))
    
    
