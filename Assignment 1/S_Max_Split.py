s=str(input())
cntr=0
cntl=0
arr=[]
for i in s:
    if(i=='L'):
        cntl+=1
    else:
        cntr+=1
    if cntl==cntr:
        arr.append(s[:cntl+cntr])
        s=s[cntl+cntr:]
        cntl=0
        cntr=0
print(len(arr))
for j in arr:
    print(j)
