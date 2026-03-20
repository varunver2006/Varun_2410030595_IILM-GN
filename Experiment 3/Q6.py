def rotate_by_one(arr):
    n = len(arr)
    
    last = arr[-1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = last
    
    return arr


arr = list(map(int, input("Enter array: ").split()))

rotate_by_one(arr)

print("Rotated array:", arr)