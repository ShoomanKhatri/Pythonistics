string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width =4

n = len(string)

sum=0

for i in range(0,n):
    print(string[i], end='')
    if(i+1)%max_width==0:
        print()
    
   
   
    
