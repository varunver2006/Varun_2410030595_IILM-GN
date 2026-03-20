def common_elements(a, b, c):
    i = j = k = 0
    n1, n2, n3 = len(a), len(b), len(c)
    
    result = []
    
    while i < n1 and j < n2 and k < n3:
        if a[i] == b[j] == c[k]:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            
            i += 1
            j += 1
            k += 1

        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    
    return result if result else [-1]

a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
c = list(map(int, input("Enter third array: ").split()))

result = common_elements(a, b, c)
print("Common elements:", result)