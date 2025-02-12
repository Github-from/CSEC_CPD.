s=input()
total=0
current="a"
for char in s:
    clock=abs(ord(current)-ord(char))
    anti=26-clock
    total+=(min(clock,anti))
    current=char
print(total)