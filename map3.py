# f1 = open('data.txt').read().split()
import sys
i=1

for line in sys.stdin:
    words = line.strip().split(',')
    print("count\t{}".format(i))
   