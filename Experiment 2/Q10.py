def has_triplet(arr, target):
    arr.sort()
    n = len(arr)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return False



arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

result = has_triplet(arr, target)

print("True" if result else "False")