list=[]
su=0
for i in range(5):
    list2=[int(x) for x in input().split()]
    list.append(list2)
t=False    
for i in range(5):
    for j in range(5):
        if list[i][j]==1:
            row=i+1
            col=j+1
            t=True
            break
    if t==True:
        break        
if row>=3:
    t=row-3
    su+=t
else:
    t=3-row
    su+=t
if col>=3:
    t2=col-3
    su+=t2
else:
    t2=3-col
    su+=t2
print(su)                           