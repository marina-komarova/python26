n = int(input()) #количество ступеней
for i in range(1, n + 1): #i номер ступеньки
    print(" " * (n - i) + "*" * i)