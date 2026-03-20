def two_sum(nums, target):
    seen = {}  
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

nums = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

result = two_sum(nums, target)
print("Indices:", result)