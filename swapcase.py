s="Hello" 
result=[]


for i in s:
        if i.isupper():
            result.append(i.lower())
        elif i.islower():
            result.append(i.upper())
        else:
            result.append(i)
            
str = "".join(result)
print(str)    
 
  
