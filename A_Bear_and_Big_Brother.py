list=[int(x) for x in input().split()]
l=list[0]
b=list[1]
su=0
while l<=b:
    l=l*3
    b=b*2
    su+=1
print(su)    