n=int(input())
a=list(map(int, input().split()))
d = {}
ans = 0
for key,value in enumerate(a):
    if value not in d.keys():
        d[value] = 0
    d[value] += 1
for key, value in d.items():
    if value < key:
        ans += value
    else:
        ans += value - key
print(ans)
