import heapq

# 1. Efficient Priority Queue Operations
# Fact: heapq allows for efficient priority queue operations where the smallest element is always at the root,
# enabling O(1) access time and O(log n) insertion and removal time.
pq = []
heapq.heappush(pq, (5, 'task5'))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (3, 'task3'))
print("1. Priority Queue Operations:")
print(heapq.heappop(pq))  # (1, 'task1')

# 2. Maintaining a Fixed-Size Heap
# Fact: You can use heapq to maintain a fixed-size heap of the largest or smallest elements from a data stream.
# This is useful for tracking top k items.
stream = [5, 1, 8, 3, 9, 2]
k = 3
top_k = []
for num in stream:
    if len(top_k) < k:
        heapq.heappush(top_k, num)
    else:
        heapq.heappushpop(top_k, num)
print("\n2. Fixed-Size Heap:")
print(top_k)  # [5, 8, 9]

# 3. Merging Multiple Sorted Iterables
# Fact: heapq.merge can merge multiple sorted iterables into a single sorted iterator, making it useful for combining sorted data streams.
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]
merged = list(heapq.merge(list1, list2, list3))
print("\n3. Merging Sorted Iterables:")
print(merged)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. Heapify an Existing List
# Fact: heapq.heapify converts an existing list into a heap in-place, ensuring that the heap property is satisfied.
data = [4, 1, 7, 3, 8, 5]
heapq.heapify(data)
print("\n4. Heapify Existing List:")
print(data)  # [1, 3, 4, 7, 8, 5]

# 5. Finding the k Largest or Smallest Elements
# Fact: heapq.nlargest and heapq.nsmallest functions can be used to find the largest or smallest k elements from a list efficiently.
data = [10, 20, 4, 45, 99, 2]
largest = heapq.nlargest(3, data)
smallest = heapq.nsmallest(3, data)
print("\n5. k Largest and Smallest Elements:")
print("Largest:", largest)  # [99, 45, 20]
print("Smallest:", smallest)  # [2, 4, 10]

# 6. Implementing a Priority Queue with Tuples
# Fact: You can use tuples with heapq to implement priority queues where the first element of the tuple represents the priority.
tasks = [(2, 'write report'), (1, 'email client'), (3, 'schedule meeting')]
heapq.heapify(tasks)
print("\n6. Priority Queue with Tuples:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")

# 7. Heap Operations are Logarithmic in Time Complexity
# Fact: Both insertion and deletion operations in a heap are performed in O(log n) time, making them efficient even for large datasets.
heap = [1, 3, 5, 7, 9]
heapq.heapify(heap)
heapq.heappush(heap, 4)
print("\n7. Logarithmic Time Complexity Operations:")
print(heap)  # [1, 3, 4, 7, 9, 5]

# 8. Heap Property for Sorting
# Fact: The heap property can be used to implement efficient heap sort, where elements are repeatedly removed from the heap and collected to produce a sorted list.
data = [5, 2, 9, 1, 5, 6]
heapq.heapify(data)
sorted_data = [heapq.heappop(data) for _ in range(len(data))]
print("\n8. Heap Sort:")
print(sorted_data)  # [1, 2, 5, 5, 6, 9]

# 9. Custom Sorting with Heaps
# Fact: You can use heaps to manage custom sorting criteria by storing tuples where the first element is the key used for sorting.
data = [(3, 'apple'), (100, 'banana'), (2, 'cherry')]
heapq.heapify(data)
print("\n9. Custom Sorting with Heaps:")
while data:
    print(heapq.heappop(data))  # (1, 'banana'), (2, 'cherry'), (3, 'apple')

# 10. Handling Real-Time Data Streams
# Fact: Heaps are useful for managing real-time data streams where you need to keep track of the top k elements as new data arrives continuously.
data_stream = [5, 1, 8, 3, 9, 2]
top_k = []
k = 3
for num in data_stream:
    if len(top_k) < k:
        heapq.heappush(top_k, num)
    else:
        heapq.heappushpop(top_k, num)
print("\n10. Real-Time Data Streams:")
print(top_k)  # [5, 8, 9]
