'''
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
'''

a = input()
b = 1  # 프린트될 넘버

for x in range(len(a)):  # 반절만큼만 반복되도 되긴함
    if a[x] == a[-(x+1)]:  # 처음이랑 끝(순회마다 1씩 증가/감소)이 같으면
        continue  # 계속
    else:  # 아니면 b=0으로 하고 컷
        b = 0
        break
print(b)

# s=input();print(+(s==s[::-1])) 신묘;
