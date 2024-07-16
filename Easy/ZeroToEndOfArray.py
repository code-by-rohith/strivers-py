def fun(arr):
    a=[]
    b=[]
    for i in range(len(arr)-1):
        if arr[i]==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    return b+a


arr = [1, 0, 5, 8, 6, 0, 2, 0, 3, 4]
print(fun(arr))












