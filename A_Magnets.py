n=int(input())
su=1
list=[]
for i in range(n):
    y=input()
    list.append(y)
for j in range(n):
    t=list[j]
    if j<n-1:
        if t==list[j+1]:
            continue
        else:
            su+=1
print(su)                    