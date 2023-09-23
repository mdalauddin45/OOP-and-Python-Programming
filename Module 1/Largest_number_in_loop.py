n = int(input())
arr = [int(input()) for _ in range(n)]

# larg=max(arr) #shortcut
largest=arr[0]
for value in arr:
    if value>largest:
        largest=value
print(largest)

