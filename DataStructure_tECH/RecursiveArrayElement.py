def recursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])

# Example usage
arr = [58,99,65]
result = recursive_sum(arr)
print("Sum of array:", result)










