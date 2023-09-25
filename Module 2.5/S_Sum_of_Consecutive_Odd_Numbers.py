n = int(input())

for _ in range(n):
    #ak line a input nity holy aivhaby nity hoby
    x, y = map(int, input().split())
    s=0
    if x+1<y:
        for num in range(x,y):
            if num%2==1:
                s+=num
            
    else:
        for num in range(y,x):
            if num%2==1:
                s+=num
    print(s)
