N = int(input())
a=1 #начинаем с первого куба. длина ребра 1
b=a**3 #обЪем
while b<=N:
    print(b,end=" ")
    a+=1
    b=a**3