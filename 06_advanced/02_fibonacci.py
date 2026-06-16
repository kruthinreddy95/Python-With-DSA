# Fibonacci sequence using recursion
def fibo(n):
    # base condition
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

number = 8
print(f"Fibonacci number at position {number}:", fibo(number))
