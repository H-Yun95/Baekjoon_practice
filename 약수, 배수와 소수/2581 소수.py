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
    return a    # 소수 판별


a = int(input())
alist = [Pnum(x + 1) for x in range(a)]  # 원소 하나하나에 피넘을 씌운 리스트 생성.
Alist = []               # 원래는 밑작업이 필요없길 바랐으나, 함수는 무조건 리턴하여
for x in alist:          # 소수가 아닐 시 0을 리턴하고,
    if x != 0:           # 0이 아닌 뭔소들만 다른 리스트에 담아두는 번거로운 작업 실행.
        Alist.append(x)
    # 리스트를 [소수, 소수, 소수 ... 소수] 꼴로 만들기 위한 작업.


b = int(input())
blist = [Pnum(x + 1) for x in range(b)]
Blist = []
for x in blist:
    if x != 0:
        Blist.append(x)

answer = []

for x in Blist:
    if x not in Alist:
        answer.append(x)  # 두 리스트의 차에서 나오는 부산물을 다른 리스트에 삽입


if Pnum(a) and a != 1:
    answer.append(a)  # 두 소수 입력시 앞의 번호가 씹히는 문제로인하여 추가. 그래도 실패
    # 놀랍게도 이 구문으로 인해 오류가 계속 뜸. 왜냐? 1은 소수가 아닌데
    # 위의 소수 함수에서 지 값을 리턴하기 때문. ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    # 정수론 어렵다

if answer:
    print(f'{sum(answer)}\n{min(answer)}')
else:
    print(-1)

'''
# input
M = int(input())
N = int(input())

# process
decimal = []
for i in range(M, N+1):
	for j in range(2, i+1):
		if j == i:
			decimal.append(i)
		if i % j == 0:
			break

# output
if not decimal:
	print(-1)
else:
	print(sum(decimal))
	print(decimal[0])

남이 쓴거 보니 이런 우둔한 등신이 다 있나 싶다.
애초에 range를 (m, n) 이렇게 받으면 쉬울걸 바득바득 따로 리스트를 만들어버리니...
인덱스 활용을 항상 염두에 두자. 중등부 문제 맞는듯 ㅋㅋㅋㅋㅋㅋㅋ
'''
