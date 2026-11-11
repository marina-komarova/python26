best=int(input())
score=int(input())
while score !=-1:
    if score>best:
        best=score
        score=int(input())
print(best)