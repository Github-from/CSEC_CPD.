n=int(input())
list=[int(x) for x in input().split()]
su=0
su2=0
for j in list:
    if j==-1:
        if su>=1:
            su-=1
        else:
            su2+=1
    else:
        su+=j 
print(su2)