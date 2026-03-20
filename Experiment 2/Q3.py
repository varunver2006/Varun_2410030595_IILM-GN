def can_reach_end(arr):
    max_reach = 0
    
    for i in range(len(arr)):
        if i > max_reach:
            return False
        
       
        max_reach = max(max_reach, i + arr[i])
    
    return True


arr = list(map(int, input("Enter array: ").split()))

result = can_reach_end(arr)

if result:
    print("True (You can reach the end)")
else:
    print("False (You cannot reach the end)")