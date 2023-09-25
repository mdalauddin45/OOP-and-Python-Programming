def reverse_digits(num):
    digits = list(str(num)[::-1])
    return digits

n = int(input())
for _ in range(n):
    arr = int(input())
    reversed_digits = reverse_digits(arr)
    print(*reversed_digits)
