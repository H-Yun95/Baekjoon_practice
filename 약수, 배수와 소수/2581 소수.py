'''
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 
최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 
89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 
출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''


def Pnum(a):
    for x in range(2, a):
        if a % x == 0:
            return 0
    return a


a = int(input())
alist = [Pnum(x + 1) for x in range(a)]
Alist = []
for x in alist:
    if x != 0:
        Alist.append(x)

b = int(input())
blist = [Pnum(x + 1) for x in range(b)]
Blist = []
for x in blist:
    if x != 0:
        Blist.append(x)

answer = []

for x in Blist:
    if x not in Alist:
        answer.append(x)

if Pnum(a):
    answer.append(a)  # 두 소수 입력시 앞의 번호가 씹히는 문제로인하여 추가. 그래도 실패

if answer:
    print(f'{sum(answer)}\n{min(answer)}')
else:
    print(-1)
