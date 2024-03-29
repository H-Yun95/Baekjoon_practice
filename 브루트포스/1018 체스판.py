'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 
크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 
흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 
만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 
칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 
다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 
경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 
경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 
체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 
정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

# 모름지기 하나의 알고리즘이 ㅈㄴ 쓰일것같으면 일단 함수부터 짜보자


def change(a):
    t = 0
    for x in range(7):
        if a[x] == a[x+1] == 'B':
            a[x+1] = 'W'
            t += 1
        elif a[x] == a[x+1] == 'W':
            a[x+1] = 'B'
            t += 1
    return t
# 1줄 8칸짜리 단기 판별 로직


a, b = map(int, input().split())

board = [list(input()) for _ in range(a)]
t = 0

for x in range(a):
    for y in range(b-7):
        t += change(board[x])

print(t)

# 일단 이전 원소와 같다면 다르게 칠하는 함수를 하나 만들어야 하고,
# 또... 이걸 8X8사이즈로 잘라야 하니 붙여서 뭔갈 해야 할 듯
# 04.01 8*8 버전은 완료
