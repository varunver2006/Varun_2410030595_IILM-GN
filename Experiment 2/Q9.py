def is_subset(a, b):
    set_a = set(a)
    
    for num in b:
        if num not in set_a:
            return False
    return True


a = list(map(int, input("Enter array a: ").split()))
b = list(map(int, input("Enter array b: ").split()))

result = is_subset(a, b)

if result:
    print("b is a subset of a")
else:
    print("b is NOT a subset of a")