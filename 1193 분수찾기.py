'''
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 
과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 
분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
'''

# 이번 문제를 while로 풀어볼까?
# 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 4/1 5/1....
# a/b 에서, 전단계에서 a가 1이면 b에 +1
# 그 뒤 b에 -1씩, a에 +1씩 하다가 b가 1이되면 또 a에 +1


def Fraction(a):
    fn = 3
    sn = 1
    cnt = 4
    while cnt != a:

    cnt += 1
    return f'{fn}/{sn}'


a = int(input())


if a == 1:
    print('1/1')
elif a == 2:
    print('1/2')
elif a == 3:
    print('2/1')
else:
    print(Fraction(a))
