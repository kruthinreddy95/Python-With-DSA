# Linear Search - Basic approach
arr = [1, 4, 3, 5, 8, 3, 0]
X = 7
found = False
for i in range(len(arr)):
    if arr[i] == X:
        print("Got it")
        found = True
        break
if not found:
    print("not found")
