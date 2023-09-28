n = int(input())
arr=list(map(int,input().split()))
ans=0
while True:
    if any(i%2!=0 for i in arr):
        break
    for i in range(n):
        arr[i]//=2
    ans+=1
print(ans)