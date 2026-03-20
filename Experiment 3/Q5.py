def find_largest(arr):
    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
    
    return max_val


arr = list(map(int, input("Enter array: ").split()))

result = find_largest(arr)
print("Largest element:", result)