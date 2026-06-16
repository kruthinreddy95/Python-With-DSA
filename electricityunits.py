units = int(input("Enter the units : "))
if units <= 100:
    result = units * 5
elif units <= 200:
    result = 100 * 5 +(units - 100) * 7
elif units <= 300:  
    result = 100 * 5 + 100 * 7 + (units - 200) * 10
elif units > 300:
    result = 100 * 5 + 100 * 7 + 100 * 10 + (units- 300) * 12
print("The total bill is : ", result)