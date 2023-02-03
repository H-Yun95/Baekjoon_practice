a, b = map(int,input().split())
nl = list(map(int, input().split()))
nl2 = []

for x in range(a):    #원래는 공리스트 안만들려고 제거를 했는데
    if nl[x] < b:     #인덱스 범위 에러 떴다....
        nl2.append(nl[x])   #아마 제거하면서 인덱스가 같이 줄어서 그런듯
print(*nl2)      # *에스터리스크 쓰면 리스트 내용물만 출력 삽가능


'''
n,x,*a=map(int,open(0).read().split())
for i in a:i<x!=print(i)
'''
