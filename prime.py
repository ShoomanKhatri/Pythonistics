def prime(n):
    if n<=1:
        return False
        
    for i in range(2, int(n/2)):
        if n%i==0:
            return False
    return True
    
num = int(input("Enter the number:"))
print("Answer is ", prime(num))
            