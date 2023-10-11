import sys
import re
prev =None
count =1
for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words= line.split()
    
    if words[0] == prev:
        count +=1
    else:
        if prev is None:
            prev=words[0]
        else:
            print('{}\t{}'.format(prev,count))
            count = 1
            prev = words[0]
            

print('{}\t{}'.format(prev,count))           
            
        
        
    
    
    



    
    
    
    
    

        
    
    
    
    
    