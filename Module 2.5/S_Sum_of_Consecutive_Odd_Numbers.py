n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    s=0
    if x<y:
        for num in range(x+1,y):
            if num%2==1:
                s+=num
            
    else:
        for num in range(y+1,x):
            if num%2==1:
                s+=num
    print(s)
