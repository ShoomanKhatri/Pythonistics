nums = [1,2,3,4,5,6,7,8,9,10]

odd = []
even=[]

for i in nums:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even numbers are {even}")
print(f"Odd numbers are {odd}")


