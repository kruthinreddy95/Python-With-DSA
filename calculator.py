x = int(input("Enter a number : "))
op = input("Enter an operator : ")
y = int(input("Enter a number : "))
if op == "+":
   z = x + y
   print("The sum is:", z)
elif op == "-":
   z = x - y
   print("The difference is:", z)
elif op == "*":
   z = x * y
   print("The product is:", z)
elif op == "/":
   z = x / y
   print("The quotient is:", z)
elif op == "%":
   z = x % y
   print("The remainder is:", z)
else:   print("Invalid input.") 

