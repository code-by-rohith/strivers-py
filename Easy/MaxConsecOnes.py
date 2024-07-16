def consec(arr):
    a = 0
    b = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            a += 1
            if a > b:
                b = a
        else:
            a = 0
    return b

arr = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
print(f"Maximum Consecutive ones in {arr} : ", consec(arr))
