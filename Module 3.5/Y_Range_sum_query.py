n,m=map(int, input().split())
arr=list(map(int,input().split()))
for _ in range(m):
    s=0
    x,y=map(int, input().split())
    s=sum(arr[x-1:y])
    print(s)
