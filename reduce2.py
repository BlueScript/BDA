import sys
import re
sum = 0
count=1
for line in sys.stdin:
    words= line.strip().split()
    sum += int(words[1])
    count +=1

print("average salary: ",sum/count)
    

