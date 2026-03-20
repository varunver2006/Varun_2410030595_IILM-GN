def find_union(a, b):
    union_set = set()
    
    for num in a:
        union_set.add(num)
    
    for num in b:
        union_set.add(num)
    
    return list(union_set)


a = list(map(int, input("Enter array a: ").split()))
b = list(map(int, input("Enter array b: ").split()))

result = find_union(a, b)

print("Union:", result)