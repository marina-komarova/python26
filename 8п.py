N=int(input())
for i in range(1,N+1): #i колво вопросов
    if 2**i>=N:
        print(i)
        break