def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif a <= arr[mid] <= b:
            mid += 1
        
        else:  
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr


arr = list(map(int, input("Enter array: ").split()))
a = int(input("Enter lower bound a: "))
b = int(input("Enter upper bound b: "))

result = three_way_partition(arr, a, b)

print("Partitioned array:", result)