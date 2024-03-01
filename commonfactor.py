a = 15
b = 10

if a > b :
    large = a
else:
    large = b
count = 0
for i in range(1,large+1):
    if a % i == 0 and b % i == 0 :
        count+=1
    else :
        continue
print('The Number of Cofactors are' , count)