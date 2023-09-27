n = int(input())
arr = list(map(int, input().split()))

arr2 = arr.copy()
arr2.reverse()

flag = arr == arr2
if flag:
    print('YES')
else:
    print('NO')
