# Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and
# columns is always odd. Return the median of the matrix

import bisect

def matrix_median(mat, n, m):
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    
    desired = (n * m) // 2  
    
    while low < high:
        mid = (low + high) // 2
        
        count = 0
        for row in mat:
            count += bisect.bisect_right(row, mid)
        
        if count <= desired:
            low = mid + 1
        else:
            high = mid
    
    return low


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

median = matrix_median(mat, n, m)
print("Median of matrix:", median)