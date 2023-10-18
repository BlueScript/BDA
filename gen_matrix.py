import sys
i=1

for line in sys.stdin:
    num = line.strip().split(",")
    row,col = num[0],num[1]
k=1
for i in range(int(row)):
    for j in range(int(col)):
        print('A,{},{},{}'.format(i,j,k))
        k+=1

k=1
for i in range(int(row)):
    for j in range(int(col)):
        print('B,{},{},{}'.format(i,j,k))
        k+=1
   