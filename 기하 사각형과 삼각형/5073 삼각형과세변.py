'''
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 
를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 
나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.
'''


def c(T):
    a = max(T)
    if sum(T) == 0:
        return False
    elif len(set(T)) == 1:
        return 'Equilateral'
    elif len(set(T)) == 2 and 0 not in T:  # 처음 돌려보니 실패를 해서
        return 'Isosceles'       # 0, 0, 1 꼴에서도 Isosceles이 출력되는걸 발견,
    else:                        # 그래서 고쳤는데도 또 틀렸다. 왜지?
        T.remove(max(T))         # 반례 찾아보니 2, 2, 8 같은경우 이등변이 나온다.

    if a >= sum(T):
        return 'Invalid'
    else:
        return 'Scalene'


while 1:
    T = list(map(int, input().split()))
    b = c(T)
    if b:
        print(b)
    else:
        break

# A = [0, 0, 0]
# print(c(A))
