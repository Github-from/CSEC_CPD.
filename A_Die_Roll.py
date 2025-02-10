list=[int(x) for x in input().split()]
need=max(list)
need2=6-(need-1)
if need2==6:
    print(1,end='')
    print("/",end='')
    print(1)
elif need2==5:
    print(5,end='')
    print("/",end='')
    print(6)
elif need2==4:
    print(2,end='')
    print("/",end='')
    print(3)
elif need2==3:
    print(1,end='')
    print("/",end='')
    print(2)
elif need2==2:
    print(1,end='')
    print("/",end='')
    print(3) 
elif need2==1:
    print(1,end='')
    print("/",end='')
    print(6)           
        