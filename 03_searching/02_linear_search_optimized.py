# Linear Search - Optimized
arr = [10, 20, 30, 40, 50]
target = 30
found = False
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        print("Found in index", i)
        break
if found == False:
    print("Not Found")
