s=input()
su=0
for i in range(len(s)):
    t=s[i].lower()
    if t==s[i]:
        su+=1
ma=len(s)//2
if len(s)%2!=0:
    ma+=1        
if su>=ma:
    print(s.lower())
else:
    print(s.upper())        