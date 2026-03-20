def spiral_traversal(mat):
    result = []
    
    if not mat:
        return result
    
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    
    while top <= bottom and left <= right:
        
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

result = spiral_traversal(mat)
print("Spiral order:", result)