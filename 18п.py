a = int(input())
b = 0 #подсчет подходящих способов
for i in range(1, int(a ** 0.5 + 1)): #+1 чтобы корень тоже вошел в проверку
    for j in range(i, int(a ** 0.5 + 1)):
        if i ** 2 + j ** 2 == a:
            b += 1
print(b)