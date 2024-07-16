def reverse_num(arr):
    left=0
    right=len(arr)-1
    while(left<right):
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
        right-=1
    return arr

arr=[1,2,5,10,20]
print(reverse_num(arr))