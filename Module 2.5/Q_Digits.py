#codeforce accepted
n=int(input())
for _ in range(n):
    arr=int(input())
    digits = list(str(arr)[::-1])
    print(*digits)