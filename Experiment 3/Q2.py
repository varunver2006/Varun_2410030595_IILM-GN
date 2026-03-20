def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return min_val, max_val


arr = list(map(int, input("Enter array: ").split()))

min_val, max_val = find_min_max(arr)

print("Minimum:", min_val)
print("Maximum:", max_val)