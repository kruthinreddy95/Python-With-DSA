arr = [99, 2, 3, 9, 5]
max=arr[0]
max2=arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max2=max
        max=arr[i]
    else:
        if arr[i] > max2 and arr[i] != max:
            max2=arr[i]
print("Second largest element is:", max2)
