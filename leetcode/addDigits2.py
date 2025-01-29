#digital sum
def addDigits(num:int)->int:
    if num ==0:
        return 0
    else :
        return 1+ (num-1)%9

print(addDigits(123))  

# output
# 6
