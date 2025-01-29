numbers = [1,2,3]

result = []

for i in range(len(numbers)):
    product = 1
    
    for j in range(len(numbers)):
         if i != j: 
             product *= numbers[j]
    
    result.append(product) 
print(result)
    

             
        
       