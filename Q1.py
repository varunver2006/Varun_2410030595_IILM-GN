def min_chocolate_diff(arr, m):
    n = len(arr)
    
    if m == 0 or n == 0:
        return 0
    if m > n:
        return -1
    
    arr.sort()
    
    min_diff = float('inf')
    
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff


arr = list(map(int, input("Enter chocolate packets : ").split()))
m = int(input("Enter number of students: "))

result = min_chocolate_diff(arr, m)

if result == -1:
    print("Not enough packets for students")
else:
    print("Minimum difference:", result)