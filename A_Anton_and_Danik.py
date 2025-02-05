x=int(input())
s=input()
a=0
d=0
for i in range(x):
    if s[i]=="A":
        a+=1
    elif s[i]=="D":
        d+=1    
if a>d:
    print("Anton")
elif a<d:
    print("Danik") 
else:
    print("Friendship")