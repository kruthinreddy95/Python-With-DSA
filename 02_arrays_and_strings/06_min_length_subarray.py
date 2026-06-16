# Find minimum length subarray with sum >= target
arr = [3, 1, 2, 10, 1]
target = 15
total = 0
result = []
for i in arr:
    total += i
    result.append(total)
print("Cumulative sum:", result)
