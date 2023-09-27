n = int(input())
arr = list(map(int, input().split()))
arr_max = max(arr)
arr_min = min(arr)
mx_index=arr.index(arr_max)
mn_index=arr.index(arr_min)
arr[mx_index] = arr_min
arr[mn_index] = arr_max
print(*arr)
