def fun1(n):
    def fun2(n):
        n=5
        print(n)
    fun2()
    print(n)

fun1(7)    


# above code and below code looks same for me but above code throws error.

def fun1(n):
    def fun2(n):  # This line now accepts an argument `n`
        n = 5
        print(n)
    fun2()  # This call to fun2() is missing the required argument `n`
    print(n)

fun1(7)


        