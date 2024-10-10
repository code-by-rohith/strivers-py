
def bub_Sort(arr):
    count = 0
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                count += 1
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    print(count)
arr=[5,2,50,88,22,65]
bub_Sort(arr)
print("Sorted array :", arr)
