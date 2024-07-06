def fun(arr1,arr2):
    a=set()
    b=[]
    for i in arr1:
        a.add(i)
    for j in arr2:
        a.add(j)
    for k in a:
        b.append(k)
    return b


arr1=[1,1,1,2,2,2,2,3,4,5,6,7,7]
arr2=[5,1,6,7,8,9,9,2,10]
print(f"Union Of Two Sorted  Array : ",fun(arr1,arr2))