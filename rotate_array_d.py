def left_rotate_by_two(arr):
    first_two_elements = arr[:2]
    for i in range(2, len(arr)):
        arr[i - 2] = arr[i]
    arr[-2:] = first_two_elements
    return arr

arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
arr = left_rotate_by_two(arr)
print("Left Rotated Array by two positions:", arr)