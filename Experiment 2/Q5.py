import math

def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge_without_extra_space(a, b):
    n, m = len(a), len(b)
    gap = next_gap(n + m)
    
    while gap > 0:
        i = 0
        
        while i + gap < n:
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1
        
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1
      
        if j < m:
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1
        
        gap = next_gap(gap)
    
    return a, b


a = list(map(int, input("Enter first sorted array: ").split()))
b = list(map(int, input("Enter second sorted array: ").split()))

a, b = merge_without_extra_space(a, b)

print("Modified a:", a)
print("Modified b:", b)