a = float(input())
b = float(input())
c = 0 #для подсчета когда температура снижалась
while b != 0: #пока значение температуры не станет 0
    if b < a:
        c += 1
    a = b
    b = float(input())
print(c)
