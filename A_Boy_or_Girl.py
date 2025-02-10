s=input()
su=0
list=[]
for i in range(len(s)):
    if s[i] not in list:
        list.append(s[i])
        su+=1
if su%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")