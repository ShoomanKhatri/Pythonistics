a = [1,2,3,4];
b=[2,3,4,5];

result = []

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==b[j]:
            result.append(a[i])
     
     

print(result)