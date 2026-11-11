n = int(input())
for num in range(1, n + 1):
    s = 0 #сумма делителей ноль перед проверкой нового числа 
    for d in range(1, num // 2 + 1):
        if num % d == 0:
            s += d
    if s == num:
        print(num)

