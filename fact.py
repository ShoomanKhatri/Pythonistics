# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# print(fact(5))


# using recursion



def fact(n):
    if n == 0 or n==1:   
        return 1       
    else:
        return n * fact(n-1)

print(fact(5))
    