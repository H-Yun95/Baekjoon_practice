'''
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 
나머지가 0이면 q는 p의 약수이다. 

6을 예로 들면

6 ÷ 1 = 6 … 0
6 ÷ 2 = 3 … 0
6 ÷ 3 = 2 … 0
6 ÷ 4 = 1 … 2
6 ÷ 5 = 1 … 1
6 ÷ 6 = 1 … 0
그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.

두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 
작은 수를 출력하는 프로그램을 작성하시오.
'''

a, b = map(int, input().split())  # 두 정수를 입력

answer = []                      # 정답을 위한 빈 리스트 선언

for x in range(a):
    if a % (x+1) == 0:
        answer.append(x+1)       # a의 약수로 이루어진 리스트 생성

try:
    print(answer[b-1])           # 그리고 인덱스 넘버만큼 세서 출력
except:                          # 예외 처리는 진짜 신이다...
    print(0)
