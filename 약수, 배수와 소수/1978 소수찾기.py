'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 
수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

# 소수를 판별하는 함수 작성


def Pnum(a):
    for x in range(2, a):  # 2부터 그 수까지 순회,
        if a % x == 0:     # a가 그 이전의 모든 자연수 중 하나로 나눠떨어진다면
            return False   # False를 return
    return True            # 아니라면 True를 return


a, Alist, count = int(input()), list(map(int, input().split())), 0
# a, 리스트, 숫자를 셀 카운트를 각각 선언

for x in range(a):
    if Pnum(Alist[x]) and Alist[x] != 1:   # 소수가 참이고, 1이 아니라면 카운트 += 1
        count += 1                         # 놀랍게도 1은 소수가 아니라고함. ㄷ
    else:
        continue

print(count)
