n,m=map(int, input().split())
arr=list(map(int,input().split()))
s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+arr[i-1]
for _ in range(m):
    x,y=map(int, input().split())
    q=s[y]-s[x-1]
    print(q)
