arr = [1, 2, 5, 7, 8, 10]
target = 12
n = len(arr)

for i in range (0, n):
    for j in range (i+1, n):
        if arr[i] + arr[j] == target:
            print(arr[i] + arr[j])
