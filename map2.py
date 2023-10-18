# f1 = open('data.txt').read().split()
import sys
import re

for line in sys.stdin:
    words = line.strip().split(',')
    if 'null' in words:
        continue
    print("salary\t{}".format(words[2]))
