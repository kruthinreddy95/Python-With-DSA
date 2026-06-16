def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


arr = [3, 0, 2, 1, 5, 7]

print(merge_sort(arr))