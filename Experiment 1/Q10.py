# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the
# array is sorted in non-decreasing order. Your task is to find and return the index of the
# first row that contains the maximum number of 1s. If no such row exists, return -1

def row_with_max_ones(arr, n, m):
    max_row_index = -1
    j = m - 1 
    
    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            max_row_index = i
    
    return max_row_index


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter matrix row by row:")
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

result = row_with_max_ones(arr, n, m)

print("Row with maximum 1s index:", result)