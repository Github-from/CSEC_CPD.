
l=[int(x) for x in input().split()]
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
print(4-len(d))            
