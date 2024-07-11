def lin(arr):
    a="Number Not Found"
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return str(a)



n=2
arr=[10,15,2,3,7,9]
print(lin(arr))