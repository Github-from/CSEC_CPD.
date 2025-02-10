list=[int(x) for x in input().split()]
k=list[0]
r=list[1] 
su=1
i=list[0]
while k%10!=0:
    if (k-r)%10==0:
        break
    else:    
        k=k+i
        su+=1
print(su)  