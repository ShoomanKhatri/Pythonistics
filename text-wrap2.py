string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width =4

result=""    
n = len(string)

for i in range(0,n):
    result +=string[i]
    if(i+1)%max_width==0:
      result+="\n"
print(result)
    
   
   
    
