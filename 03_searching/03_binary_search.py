# Binary Search
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
left, right = 0, len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Found {target} at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print(f"{target} not found")
