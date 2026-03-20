import heapq

def kth_smallest(arr, k):
    heapq.heapify(arr)
    
    for _ in range(k - 1):
        heapq.heappop(arr)
    
    return heapq.heappop(arr)


arr = list(map(int, input("Enter array : ").split()))
k = int(input("Enter value of k: "))
print("Kth smallest element:", kth_smallest(arr, k))