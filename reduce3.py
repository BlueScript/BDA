import sys
sum = 0
count=1
for line in sys.stdin:
    words= line.strip().split()
    sum += int(words[1])

print("No. of records: ",sum)
    

