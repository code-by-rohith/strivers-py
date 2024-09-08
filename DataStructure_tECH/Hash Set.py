def find_pairs(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))

        seen.add(num)

    for pair in pairs:
        print(pair[0], "and", pair[1])


# Example usage
arr = [7, 3, 6, 5, 8, 7, 5]
target_sum = 10
find_pairs(arr, target_sum)
