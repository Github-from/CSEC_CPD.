n=int(input())
list=[int(x) for x in input().split()]
sereja=0
dima=0
f=n
for i in range(n):
    if i%2==0:
        if list[f-1]>list[0]:
            t=list[f-1]
        else:
            t=list[0]    
        sereja+=t
        list.remove(t)
        f-=1
    else:
        if list[f-1]>list[0]:
            t=list[f-1]
        else:
            t=list[0]    
        dima+=t
        list.remove(t)
        f-=1
print(sereja,dima)            
        