'''
인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 
졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 
응시하지 않았다는 사실을 깨달았다!

치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

전공평점은 전공과목별 (학점 x 과목평점)의 합을 학점의 총합으로 나눈 값이다.

인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0
P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.

과연 치훈이는 무사히 졸업할 수 있을까?
'''

total = 0
sub = 0

for x in range(20):
    a, b, c = input().split()
    b = int(float(b))
    sub += b
    if c == 'A+':
        total += (4.5 * b)
    elif c == 'A0':
        total += (4.0 * b)
    elif c == 'B+':
        total += (3.5 * b)
    elif c == 'B0':
        total += (3.0 * b)
    elif c == 'C+':
        total += (2.5 * b)
    elif c == 'C0':
        total += (2.0 * b)
    elif c == 'D+':
        total += (1.5 * b)
    elif c == 'D0':
        total += (1.0 * b)
    elif c == 'F':
        total += (0 * b)
    elif c == 'P':
        sub -= b
        continue  # 너무 길다... 맞긴 하지만 분명 방법이 있을 것

print(f'{total/sub:.6f}')

'''
import sys
v1 = v2 = 0
for i in sys.stdin:
    a,b,c = i.split()
    if c == 'P':
      continue
    b = float(b)
    v2 += b
    v1 += b*(4.5-0.25*'A+A0B+B0C+C0D+D012F'.\
index(c))
print(v1/v2)  모듈로 해결한 방법이 있지만 만만찮게 김 ㅋㅋㅋㅋ
'''
