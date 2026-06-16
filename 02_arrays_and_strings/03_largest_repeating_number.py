# Find second largest element
arr = [99, 2, 3, 9, 5]
max_val = arr[0]
max2_val = arr[0]
for i in range(len(arr)):
    if arr[i] > max_val:
        max2_val = max_val
        max_val = arr[i]
    else:
        if arr[i] > max2_val and arr[i] != max_val:
            max2_val = arr[i]
print("Second largest element is:", max2_val)
