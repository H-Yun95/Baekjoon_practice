'''
문제
오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 
이해했는지 문제를 통해서 확인해보자.

알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.

O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

이 정의는 실제 O-표기법(https://en.wikipedia.org/wiki/Big_O_notation)과 다를 수 있다.

함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

입력
첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)

다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)

다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

출력
f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.

f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이다. f(1) = 14, c × g(1) = 8이므로 O(n) 정의를 만족하지 못한다.

f(n) = 7n + 7, g(n) = n, c = 8, n0 = 10이다. 모든 n ≥ 10에 대하여 7n + 7 ≤ 8n 이므로 O(n) 정의를 만족한다.
'''


def f(a, b, c):
    return a*c+b
# 단순히 수식만 세우니 감도 안잡힌다. 그래서 반례를 보고 그래프에서 아이디어를 착안,
# 정확히 두 함수를 정림하는 것부터 시작함.


def g(a, b):
    return a*b


a, b = map(int, input().split())
c, d = int(input()), int(input())
e = False

while d != 100:                # 우선 n의 범위가 1~100까지라 d부터 100까지 반복
    # 이러면 좌표평면 상에서 문제의 범위에서 두 함수의 대소를
    if f(a, b, d) > g(c, d):   # 모두 구분할 수 있다고 생각. 근데 101로 했어야 했나?
        print(0)               # 암튼 그래서 f(n)이 g(n)보다 더 큰 구간이 하나라도 있다면,
        e = True               # 밑에서 1을 출력하기 위해 e를 True로 바꾸고
        break                  # 0을 출력하고 끝
    d += 1

if e:
    pass
else:
    print(1)


'''
a,b,c,d=map(int,open(0).read().split())

print(int(a*d+b<=c*d and a<=c))

이래서 문제를 이해하고 식을 세우는게 ㅈㄴ 중요하구나...
그러고 보니 이렇게 식을 세우면 True일 때 알아서 1이 나오는듯?

a,b = map(int, input().split())
c = int(input())
n = int(input())

r=1 if a*n+b<=c*n and c>=a else 0
print(r)
이런 표현식으로도 쓰이는 듯함.
'''
