'''
문제
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 
21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 
블랙잭은 카지노마다 다양한 규정이 있다.

한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 
창영이와 게임하려고 한다.

김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 
딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 
숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 
한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 
않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 
가까운 카드 3장의 합을 구해 출력하시오.

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 
양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
t = 0

for x in range(n-2):
    for y in range(1, n-1):
        if x == y:           # 밑의 문제를 해결하기 위해, x와 y가 다를 시 코드가 돌아가게 작동
            continue         # 생각해보면 if x != y 하고 밑에 주르륵 썼으면
        else:                # 더 간단하지 않았을까 싶음.
            for z in range(2, n):
                if z != x and z != y:       # 여기서도 z가 x, y와 다르다면 코드 실행
                    s = a[x] + a[y] + a[z]  # 세 수를 전부 더해주고,
                    if s > t and s <= m:    # 그 수가 이전 합계보다 크면서 m 이하라면
                        t = s               # 더한 수를 t로 정의

print(t)

# ! 이렇게 단순 반복으로만 짜면 동일한 수 ex) x=y=1일때 등
# 가 더해질 수 있어서 값이 이상하게 나옴. 그걸 해결해야 함.

'''
밑에는 시간이 굉장히 짧게 걸려서 가져와본 녀석
다른 짧은 코드들은 모듈을 잘 갖고 오는데, 이녀석은그런 것도 없이 굉장히 짧게 끝남.

N, M = map(int,input().split())
cards = list(map(int,input().split()))
maxv = 0

def myfunc():              어쩌면 함수 선언이 짧은 비결일 수도?
    global maxv            C와 비슷하게? 함수 밖 변수에 영향을 주는 것으로 보임
    for i in range(N):     아니다 싸피에서 배웠던 것 같은데
        temp_maxv = cards[i]
        if temp_maxv > M:
            continue
        for j in range(i+1, N):
            temp_maxv = cards[i] + cards[j]
            if temp_maxv > M:
                continue
            for k in range(j+1, N):
                temp_maxv = cards[i] + cards[j] + cards[k]
                if temp_maxv == M:
                    maxv = temp_maxv
                    return
                if maxv < temp_maxv < M:
                    maxv = temp_maxv  # 갱신
                    # print(maxv)
    return

myfunc()
print(maxv)

ㅇㅎ. 총 n번 반복하고, 반복을 겹칠 수록 그때 카드를 더해서
값이 m과 같다면 바로 리턴, 아니라면 밑으로 마저 연산을 해서
이전값과 비교하여 다시 갱신하는 프로세스. 근데 이게 왜 이렇게
짧게 걸릴까?
'''
