'''
도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 
N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 
가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, 
..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 

도현이는 앞으로 M번 바구니의 순서를 회전시키려고 만들려고 한다. 
도현이는 바구니의 순서를 회전시킬 때, 순서를 회전시킬 범위를 정하고, 
그 범위 안에서 기준이 될 바구니를 선택한다. 도현이가 선택한 바구니의 
범위가 begin, end이고, 기준이 되는 바구니를 mid라고 했을 때, 
begin, begin+1, ..., mid-1, mid, mid+1, ..., end-1, end 순서로 
되어있는 바구니의 순서를 mid, mid+1, ..., end-1, end, begin, 
begin+1, ..., mid-1로 바꾸게 된다.

바구니의 순서를 어떻게 회전시킬지 주어졌을 때, M번 바구니의 순서를 
회전시킨 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 
프로그램을 작성하시오.
'''

a, b = map(int, input().split())

numlist = [x + 1 for x in range(a)]


for x in range(b):
    c, d, e = map(int, input().split())
    newlist = numlist[c-1:d]
    print(newlist)
    print(numlist)
'''
c = [1, 2, 3]

for x in range(len(c)):
    c.reverse()
    numlist.insert(3, c[x])
print(numlist)   리스트를 만들고 원소로 삽입하는 법.
'''
