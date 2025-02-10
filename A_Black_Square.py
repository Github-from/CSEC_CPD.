list=[int(x) for x in input().split()]
s=input()
su=0
for i in range(len(s)):
    if s[i]=="1":
        su+=list[0]
    elif s[i]=="2":
        su+=list[1]
    elif s[i]=="3":
        su+=list[2]
    else:
        su+=list[3]
print(su)                    