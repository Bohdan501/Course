
s=float(input("скількки треба здачі ? :"))
print(s)
s=round(s*100,0)
# while - до поки умова виконується
k=0
while s > 0:
    if s >= 25:
        s=s-25
        k=k+1
    elif s >=10:
        s=s-10
        k=k+1
    elif s >=5:
        s=s-5
        k=k+1
    elif s >= 1:
        s=s-1
        k=k+1
    else:
        s=0
print(k)
