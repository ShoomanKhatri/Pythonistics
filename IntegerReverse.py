def SUM(n):
    rev = 0
    while(n>0):
        num = n%10
        rev = rev*10+num
        n = n//10
    return rev
  
    

print("answer is ", SUM(124))    
