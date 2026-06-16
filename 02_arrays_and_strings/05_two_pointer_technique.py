# Two pointer technique example
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
print("Elements from both ends:")
while left < right:
    print(f"{arr[left]} {arr[right]}", end=" | ")
    left += 1
    right -= 1
print()
