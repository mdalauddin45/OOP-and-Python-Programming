s = input().split()
r=[]
for word in s:
    revers_word=word[::-1]
    r.append(revers_word)
print(' '.join(r))