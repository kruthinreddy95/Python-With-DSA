arr = [5, 10, 15, 20, 25]
target = 20
left = 0
right = (len(arr)-1)
while left <= right :
    if arr[left] == target:
        print("Found in left",left)
        break
    if arr[right] == target:
        print("Found in right",right)
        break
    left += 1
    right -= 1    
    
