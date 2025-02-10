l=[int(x) for x in input().split()]
n=l[0]
t=l[1]
y=input()
l2=list(y)
for i in range(t):
    k=0
    for j in range(n):
        j=k
        if j<n-1:
            if l2[j]=="B":
                if l2[j+1]=="G":
                    l2[j+1]="B"
                    l2[j]="G"
                    k+=2
                else:
                    k+=1
            else:
                k+=1 
                           
for i in l2:
    print(i,end='')
print()    