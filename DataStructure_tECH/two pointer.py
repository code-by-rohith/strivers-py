def main(arr):

    left = 0
    right = len(arr) - 1

    while left <= right:
        current_sum = arr[left] + arr[right]
        if current_sum == 10:
            print(arr[left], "and", arr[right])
            left += 1
            right -= 1
        elif current_sum < 10:
            left += 1
        else:
            right -= 1

arr = [1, 9, 5, 5, 3, 7, 2, 8, 4, 6]
main(arr)
