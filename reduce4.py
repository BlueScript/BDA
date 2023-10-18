import sys
i=None
j=None
k=None
for line in sys.stdin:
    num = line.strip().split()
    num1,num2,num3 = num[0],num[1],num[2]
    if i == num1 and j == num2:
        print('C,{},{},{}'.format(num1,num2,int(k)+int(num3)))
    else:
        i = num1
        j= num2
        k = num3
        