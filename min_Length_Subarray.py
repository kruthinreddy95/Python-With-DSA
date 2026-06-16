arr = [2, 1, 5, 2, 3, 2]
x = 7

left = 0
windowSum = 0
minlength = len(arr)

for right in range(len(arr)):
    windowSum += arr[right]

    while windowSum >= x:
        minlength = min(minlength, right - left + 1)
        windowSum -= arr[left]
        left += 1

print(minlength)
