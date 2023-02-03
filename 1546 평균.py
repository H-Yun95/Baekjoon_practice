a = int(input())
Num_list = list(map(int, input().split()))
Change_list = []

for x in range(a):
    Change_scr = Num_list[x]/max(Num_list)*100
    Change_list.append(Change_scr)

print(sum(Change_list)/a)

'''
n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)
'''
