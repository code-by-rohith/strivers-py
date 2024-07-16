def rot(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    return arr


arr=[1,2,3,4,5]
print("Orginal array  : ",arr)
print("Left rotated array by ones : ", rot(arr))


