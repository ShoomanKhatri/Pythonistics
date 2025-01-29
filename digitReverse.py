
# it works for both positive and negative value 
num = -1234

if num <0:
    print(f"-{str(abs(num))[::-1]}")
    
else:
    print(str(abs(num))[::-1])

    


