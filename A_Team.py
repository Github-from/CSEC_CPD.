x=int(input())
su=0
for i in range(x):
    list=[int(x) for x in input().split()]
    su2=0
    for j in range(3):
        if list[j]==1:
            su2+=1
    if su2==3 or su2==2:
        su+=1
print(su)                