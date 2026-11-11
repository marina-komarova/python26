n = int(input())
for num in range(2, n + 1):
    for d in range(2, int(num ** 0.5) + 1): #подбор делителя
        if num % d == 0:
            break
    else:
        print(num)
