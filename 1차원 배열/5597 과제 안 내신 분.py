Std = [x for x in range(1,31)]
Num = []

for x in range(28):
    a = int(input())
    Num.append(a)

for y in range(30):
    if Std[y] not in Num:
        print(Std[y])

# print(*{*map(int,open(0))}^{*range(1,31)})
