def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter target value: "))

result = search_matrix(matrix, target)

print("Found" if result else "Not Found")