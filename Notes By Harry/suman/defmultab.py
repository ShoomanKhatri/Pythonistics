
def mul(num): 
    """ This function prints multiplication table of a given number"""
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
# end of function table


# input a number
n = int(input("Please Enter a number to print its multiplication table:"))

# call the function tanle by passing actual parameter 'n' 

mul(n)
