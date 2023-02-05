'''
전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 
곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 
돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 
이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 
어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, 
UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 
구하는 프로그램을 작성하시오.
'''
from string import ascii_lowercase  # 편하게 알파벳 문자열 받을 수 있는 모듈이라고 해서 사용해봄

# 번호가 할당된 알파벳 딕 생성
# 딕셔너리 값으로 덧셈 할당

Dial = {}  # 알파벳마다 밸류 할당하는 공딕 생성

for Alpha in ascii_lowercase:
    Dial[Alpha] = 0  # 딕셔너리 만들고,

for x in Dial:  # 이렇게 번거롭게밖에 안 만들어진다....
    if x == 'a' or x == 'b' or x == 'c':
        Dial[x] = 2
    elif x == 'd' or x == 'e' or x == 'f':
        Dial[x] = 3
    elif x == 'g' or x == 'h' or x == 'i':
        Dial[x] = 4
    elif x == 'j' or x == 'k' or x == 'l':
        Dial[x] = 5
    elif x == 'm' or x == 'n' or x == 'o':
        Dial[x] = 6
    elif x == 'p' or x == 'q' or x == 'r' or x == 's':
        Dial[x] = 7
    elif x == 't' or x == 'u' or x == 'v':
        Dial[x] = 8
    elif x == 'w' or x == 'x' or x == 'y' or x == 'z':
        Dial[x] = 9
word = input().lower()
mul = 0

for y in word:
    mul += Dial[y]  # 사실 해법 자체는 간단한 편

print(mul+len(word))


# print(sum(62-int(10000/(ord(v)+102))for v in input()))
