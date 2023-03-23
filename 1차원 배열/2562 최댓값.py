nl = []

for x in range(9):
    a = int(input())   
    nl.append(a)
for y in range(9):
    if nl[y] == max(nl):
        print(nl[y],y+1,sep='\n')

# print(*max((int(input()),i+1)for i in range(9)))
