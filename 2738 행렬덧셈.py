'''
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 
M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 
주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 
작거나 같은 정수이다.
'''

n, m = map(int, input().split())

Alist = [list(map(int, input().split())) for _ in range(n)]
Blist = [list(map(int, input().split()))
         for _ in range(n)]  # 드간대로 2차원 리스트를 만드는 방법
Clist = []

for x in range(n):
    for y in range(m):
        c = Alist[x][y] + Blist[x][y]
        Clist.append(c)
    print(*Clist)
    Clist = []  # 이 부분은 축약이 힘들다...

'''
a = [1, 2, 3]
b = [4, 5, 6]

c = [a[x] + b[x] for x in range(len(a))] 행렬 덧셈으로 리턴하는 리스트


(r,c),*M=[map(int,l.split())for l in open(0).readlines()]
for a,b in zip(M[:r],M[r:]):print(*map(sum,zip(a,b)))  이건 대체..?


c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
c를 더 간단하게 축약하는 방법. for문을 for문으로 한번 더 감싸는 방법
'''
