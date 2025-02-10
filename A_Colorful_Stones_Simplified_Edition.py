s=input()
t=input()
index=0
for i in range(len(t)):
    if t[i]==s[index]:
        index+=1
print(index+1)
