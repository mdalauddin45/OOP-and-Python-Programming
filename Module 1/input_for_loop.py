n = int(input())
arr = [int(input()) for _ in range(n)]

total = sum(arr) 
index=0
for value in arr:
    print(f"Index {index}: Value {value}")
    index += 1
print("Sum of elements:", total)
