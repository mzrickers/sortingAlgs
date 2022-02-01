def merge(left, right):
    result = list()
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx = left_idx + 1
        else: # left[left_idx] > right[right_idx]:
            result.append(right[right_idx])
            right_idx = right_idx + 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


alist = [9234, 2859, 28953, 28937, 297590, 894, 892, 895, 902, 945]
test = merge_sort(alist)
print(test)
