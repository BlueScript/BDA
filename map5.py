import sys
count = 0

for line in sys.stdin:
    num = line.strip().split(',')
    while count != 3:
        if count == 3:
            count =0
        if num[0] == 'A':
            print('C,{},{},{},{}'.format(num[1],count,num[2],num[3]))
            count +=1
        
    