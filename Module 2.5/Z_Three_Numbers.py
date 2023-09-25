k,s=map(int, input().split())
sum=0
for x in range(k+1):
    for y in range(k+1):
        if s-x-y>=0 and s-x-y<=k:
            sum+=1
print(sum)