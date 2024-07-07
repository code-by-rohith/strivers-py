def getSingleElement(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        cnt = 0
        for j in range(n):
            if arr[j] == num:
                cnt += 1
        if cnt == 1:
            return num
    return -1



arr = [4, 1, 2, 1,8, 2,4]
ans = getSingleElement(arr)
print("The single element is:", ans)
