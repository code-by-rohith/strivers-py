def fun(arr):
    a = 0
    for i in range(len(arr)):
        if arr[i] >= 10:
            a += 1
    return a

arr = input("Enter numbers separated by spaces: ")
numbers_str = arr.split()
numbers = [int(num) for num in numbers_str]
print("List of numbers:", numbers)
print(fun(numbers))
