arr = [3, 2, 1, 0, 5, 6, 7]
n = len(arr)

for i in range (0, n):
    min = i
    for j in range (i+1, n):
        if arr[i] < min:
            min = arr[i]
            arr[i],arr[min] = arr[min], arr[i]
print(arr) 
