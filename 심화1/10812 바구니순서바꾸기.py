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

a, b = map(int, input().split())  # 리스트, 횟수 입력

numlist = [x + 1 for x in range(a)]  # 문제 풀이를 위한 [1,2,3...x] 꼴의 리스트 생성

for x in range(b):  # b만큼 반복
    c, d, e = map(int, input().split())  # 시작지점, 끝지점, 리스트를 뒤집을 구간 입력
    newlist = numlist[c-1:d]  # 여기서 지점을 포함한 새 리스트 생성
    for y in newlist:
        if y in numlist:
            numlist.remove(y)  # 없애는건 성공. 뉴리스트의 요소를 원래의 리스트에서 제거
    for z in range(d-e+1):  # 움직일 구간만큼 반복
        num = newlist[-1]  # 뉴리스트의 제일 끝 지점을 변수로 선언하고,
        newlist.remove(num)  # 그 부분을 제거하고 제일 앞에 넘버를 삽입하는걸 반복
        newlist.insert(0, num)  # 근데 이상하게 이 두 부분을 거꾸로 했을땐 작동하지 않음...

    newlist.reverse()  # 여기서부턴 다시 뉴리스트를 원리스트에 입력하는 프로세스. 먼저 뉴리스트를 뒤집어준다.
    for w in range(len(newlist)):  # 뉴리스트만큼 반복, 근데 여기서 인덱스를 거꾸로 가게 했으면 굳이 뒤집지 않아도 괜찮은듯?
        numlist.insert(c-1, newlist[w])  # 하나씩 원래 들어가야 할 c-1 위치에 삽입
print(*numlist)

'''
n,m=map(int,input().split())  숏코딩
l=[i for i in range(1,n+1)]  이렇게 생성하는것까진 동일
for _ in range(m):
    i,k,j=map(int,input().split()) 인수도 동일하게 받긴 하는데...
    l[i-1:k]=l[j-1:k]+l[i-1:j-1]  여기서 갱장히 인덱스를 잘 활용한다.
    구간을 l[i-1:k]로 자르고, 그 구간의 순서를 바꾸는 ㅇㅎ 이해했음
print(*l)
'''

'''

c = [1, 2, 3]
c.reverse()

for x in range(len(c)):
    numlist.insert(3, c[x])
print(numlist)   리스트를 만들고 원소로 삽입하는 법.
'''
