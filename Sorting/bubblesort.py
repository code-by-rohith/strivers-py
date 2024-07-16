

def bub_Sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr = [88, 22, 65, 95, 25]
bub_Sort(arr)
print(arr)
