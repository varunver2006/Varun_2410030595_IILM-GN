def min_swaps_to_group(arr, k):
    n = len(arr)
    
    good = sum(1 for x in arr if x <= k)
    
    bad = sum(1 for x in arr[:good] if x > k)
    
    min_swaps = bad
    
    for i in range(good, n):
        if arr[i - good] > k:
            bad -= 1
        
        if arr[i] > k:
            bad += 1
        
        min_swaps = min(min_swaps, bad)
    
    return min_swaps


arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter value of k: "))

result = min_swaps_to_group(arr, k)
print("Minimum swaps required:", result)