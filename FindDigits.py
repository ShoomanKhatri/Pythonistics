
def findDigits(n):
    # Write your code here
    count = 0
    original = n 
    while n > 0:
        digit = n % 10  
        if digit != 0 and original % digit == 0: 
            count += 1
        n //= 10 
    return count
    

print("answer is ", findDigits(124))    
