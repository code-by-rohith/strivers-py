arr1 = [56, 450, 87, 12, 85]
max1 = 0
max2 = 0

for num in arr1:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print("The second largest element is:", max2)