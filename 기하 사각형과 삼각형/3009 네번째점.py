'''
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 
네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 
1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''


def an(a):
    return min(a, key=a.get)
# 딕셔녀리의 키 중 벨류가 가장 작은 값을 리턴


x = {}
y = {}  # x, y 좌표를 담을 공리스트 작성
for i in range(3):  # 3번 들어오니까 3번 반복
    a, b = input().split()  # 키값을 받아주고,
    if a in x:
        x[a] += 1
    else:
        x[a] = 1
    if b in y:
        y[b] += 1    # 키값이 있으면 벨류에 +1, 없으면 'a':1의 딕셔너리 삽입
    else:            # 그렇게 해서 {a:1, b:2}의 형식이 만들어지면
        y[b] = 1     # 벨류가 더 낮은 a를 출력하면 됨.

print(an(x), an(y))

# a = {'e': 1,
#      'b': 2,
#      'c': 3,
#      'd': 4, }

# print(min(a.values()))

# if 'c' in a:
#     print("c is here")
# else:
#     print('no')

# if 'f' in a:
#     print('yes')
# else:
#     print('f not')
# 연구의 흔적
