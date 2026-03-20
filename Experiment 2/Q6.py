def merge_intervals(intervals):
    intervals.sort()
    
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

n = int(input("Enter number of intervals: "))

intervals = []
print("Enter intervals (start end):")
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

result = merge_intervals(intervals)

print("Merged intervals:")
for interval in result:
    print(interval)