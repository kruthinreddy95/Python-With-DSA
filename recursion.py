def fun(n):
    #base condition
    if (n == 0):
        return 0
    
    #Recursive call
    return n * fun(n - 1)

number = 5
result = fun(number)
print(result)


    