def addDigits(num: int) ->int:
    while num >10:
        temp = 0
        while num>0:
            temp +=num%10
            num //=10
        num = temp
    return num
    
p = addDigits(123)    
print("sum is:",p)
    
    # output
    # sum is: 6