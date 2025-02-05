list=[int(x) for x in input().split()]
list2=[int(x) for x in input().split()]
n=list[0]
h=list[1]
su=0
for i in list2:
    if i<=h:
        su+=1
    else:
        t=i//h
        su+=t
        if i%h!=0:
            su+=1
print(su)                