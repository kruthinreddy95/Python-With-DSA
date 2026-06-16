arr = [2, 1, 5, 2, 3, 2]
x >= 7
minlen = 0
for i in range(len(arr)):
    if arr[i]+arr[i+1] == x :
        print(arr[i] + arr[i+1])
    