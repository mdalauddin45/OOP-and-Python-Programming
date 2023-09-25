x, n = map(int, input().split())
S = 0

for i in range(0, n + 1, 2):
    S += x ** i
print(S-1)
