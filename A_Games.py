n=int(input())
list=[]
su=0
for i in range(n):
    l=[int(x) for x in input().split()]
    list.append(l)
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            if list[i][0]==list[j][1]:
                su+=1
print(su)                     