'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후
출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째
문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric"
문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:
이다.
'''
a = int(input())  # 반복횟수 입력
new_word = []     # 새 문자열이 들어갈 공리스트 선언

for x in range(a):  # 처음 입력한 반복횟수만큼
    num, word = input().split()  # 문제의 a, b 쌍으로 입력
    for y in range(len(word)):  # b 문자열을 바꿔야하므로 그 길이만큼
        new_word.append(word[y]*int(num)) # 방금만든 공리스트에 반복된 알파벳 삽입
        if y > 0: # 이제 두 번째 문자열부턴?
            new_word[0] += new_word[y] # 0번 인덱스의 문자에 합산
    print(new_word[0]) # 그리고 첫 번째 문자 출력
    new_word = [] # 계속 순회해야 하므로 리스트 초기화
