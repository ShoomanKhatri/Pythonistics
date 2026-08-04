# n = 123
n = int(input("Enter a number: "))
original = n

rev = 0

while(n>0):
    rem = n%10
    rev = rev*10+rem
    n=n//10
if original==rev:
    print("palindrome")
else:
    print("not palindrome")
print("reversed is :",rev)
    