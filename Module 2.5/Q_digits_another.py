# n = int(input())

# for _ in range(n):
#     arr = int(input())
#     digits = []
#     while arr > 0:
#         digit = arr % 10
#         digits.append(digit)
#         arr = arr // 10
        
#     print(*digits)

# n=int(input())
# for _ in range(n):
#     arr=int(input())
#     digits=[]
#     while arr>0:
#         digit = arr % 10
#         digits.append(digit)
#         arr = arr // 10
#     print(*digits)
# test = int(input())

# for t in range(1, test + 1):
#     n = int(input())
#     while n != 0:
#         print(n % 10, end=" ")
#         n = n // 10
#     print()

def print_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits

T = int(input())

for _ in range(T):
    N = int(input())
    digits = print_digits(N)
    print(" ".join(map(str, digits)))
