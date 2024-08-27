def three_sum_zero(arr):
    result = set()

    for i in range(len(arr)):
        seen = set()
        target = -arr[i]

        for j in range(i + 1, len(arr)):
            if target - arr[j] in seen:
                triplet = tuple(sorted([arr[i], arr[j], target - arr[j]]))
                result.add(triplet)
            seen.add(arr[j])

    return list(result)

arr = [8, 9, 5,2,-3,-8,-1,78,-79,4,-5]
print(three_sum_zero(arr))



