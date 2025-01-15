def armstrong(n):  #narcisstic
    temp = n
    armstrong_sum = 0  
    
    while n>0:
        digit=n%10
        armstrong_sum = armstrong_sum + digit ** 3
        n //= 10
    
    if armstrong_sum ==temp:
        return True
    else: 
        return False
        
n = 153

if armstrong(n):
    print("The number is armstrong")

else:
    print("The number is not armstrong")
        
    
    