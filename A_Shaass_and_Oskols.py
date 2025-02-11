n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(m):
    index, no = map(int, input().split())
    index -= 1  
    
    left = no - 1
    right = l[index] - no

    if index > 0:
        l[index - 1] += left  
    if index < n - 1:
        l[index + 1] += right  

    l[index] = 0 

for birds in l:
    print(birds)
