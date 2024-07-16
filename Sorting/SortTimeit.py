import random
import timeit

def bub_Sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [random.randint(0, 100000) for _ in range(10)]
print("Original array:", arr)

time_taken = timeit.timeit(lambda: bub_Sort(arr), number=1)
print("Sorted array:", arr)
print("Time taken to sort:", time_taken, "seconds")
