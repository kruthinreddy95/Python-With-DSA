arr=[90,25,36,99,20,34,49]
max=arr[0]
max2=arr[0]
max3=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max3=max2
        max2=max
        max=arr[i]
    elif arr[i]>max2 and arr[i]!=max:
        max3=max2
        max2=arr[i]
    elif arr[i]>max3:
        max3=arr[i]
print(max3)