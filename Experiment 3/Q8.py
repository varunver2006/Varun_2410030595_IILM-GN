def search_insert(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

result = search_insert(arr, target)
print("Index:", result)