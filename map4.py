import sys
i=1

for line in sys.stdin:
    num = line.strip().split(',')
    print(num[1],num[2],num[3])
    