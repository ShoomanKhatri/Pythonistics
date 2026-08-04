n = 153

temp = n
result = 0

while(n>0):
    digit = n%10
    result = result + digit**3
    n =n//10

if result == temp:
    print("armstrong")
else:
    print("not armstrong")