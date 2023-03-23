'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은
경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

dicts = {key: -1 for key in dict.fromkeys(['a', 'b', 'c', 'd', 'e',
                                      'f', 'g', 'h', 'i', 'j',
                                      'k', 'l', 'm', 'n', 'o',
                                      'p', 'q', 'r', 's', 't',
                                      'u', 'v', 'w', 'x', 'y',
                                      'z']).keys()}  # 딕셔너리형으로 일일이
a = input()                                          # 노가다
# 원래 카운트를 따로 선언했으나, 인덱스 값을 쓰면 되기에 필요없어보임

for x in range(len(a)):    # a의 인덱스만큼 반복
    for word in dicts:     # dicts의 원소를 뽑는 반복문
        if dicts[word] == -1:   # 여기서 한번 삑났는데, 밸류 값이 변경됐으면 그 부분은 무시해도 된다는 조건을 걸어야 했음
            if word == a[x]:    # 밸류값이 -1이고, 알파벳이 키 값과 같다면
                dicts[word] = x # 그 알파벳의 밸류값을 인덱스로 바까줌
                break           # 생각해보니 and로 조건 걸었어도 됐을듯
        else:
            continue            # 만약 벨류값이 바꼈다면 무시하고 진행

print(*dicts.values())   # 원소만 출력하는 코드

'''   역시 아스키코드로 쓸 수 있는 수단이 있을 듯 했음
import sys

x = input()

y = [-1 for i in range(26)]

for i in range(len(x)) :
    z = ord(x[i]) - 97
    if y[z] == -1 :
        y[z] = i

for i in range(len(y)) :
    sys.stdout.write(str(y[i]) + ' ')
'''
