a=int(input())
while True:
    if a%2==0 and a!=1:
        a//=2
    if a==1:
        print("верно")
        break
    if a%2 !=0:
        print("не верно")
        break