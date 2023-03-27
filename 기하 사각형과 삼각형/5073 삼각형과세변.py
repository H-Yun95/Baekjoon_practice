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
# 처음부터 다시
# 0, 0, 1 = Invalid,
# 0, 2, 1 = Invalid,
# 2, 2, 8 = Invalid,
# 6, 2, 6 = Isosceles 등이 나와야 함.


def c(a):                       # 삼각형 판별 함수
    if sum(a) == 0:             # 만약 총합이 0이면 = 0, 0, 0이면
        return False            # False 리턴
    if len(set(a)) == 1:        # set 원소가 1개면 = 3개 다 같으면
        return 'Equilateral'    # 정삼각형
    b = max(a)                  # 가장 큰 값 지정
    a.remove(b)                 # '중요' 그 원소 단 하나만 빼기
    if b >= sum(a):   # 0이 낑겨있거나 뺀 원소가 나머지보다 크거나 같다면 (0, 2, 2 의 경우 2 하나 빼도 어?)
        return 'Invalid'        # 삼각형 안됨. 위에 0 in a 삭제해도 됨 ㅋㅋ
    a.append(b)                 # 마무리 이등변 판별을 위해 뺀 원소 다시 더해줌. 순서 상관 없어서 append
    if len(set(a)) == 2:        # 이제 set 원소가 2개면 = 2개만 같다면
        return 'Isosceles'      # 이등변
    return 'Scalene'            # 나머지는 걍 삼각형


while 1:
    T = list(map(int, input().split()))
    a = c(T)      # 이게 중요한데, 함수 결과값을 따로 변수로 지정 안하니까
    if a:         # 루프가 이상하게 돌아감. 암튼 a가 True라면,
        print(a)  # a 출력
    else:
        break

# 예외를 어떻게 처리하냐 로직 짜는걸걸로 짱구 좀 굴렸다....

'''
for z in open(0):
    s=sorted(map(int,z.split()))
    print(('Invalid','Equilateral','Isosceles','Scalene')[(s[2]<s[0]+s[1])*len({*s})]*(s[0]>0))
숏코딩. 저 zip과 open은 알아둘 필요성이 보인다.
'''
