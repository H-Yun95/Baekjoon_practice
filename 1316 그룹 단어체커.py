'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 
연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 
c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 
연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 
떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 
프로그램을 작성하시오.
'''


def distinc(a):  # 문자열이 그룹단어인지 아닌지 판단
    empty_list = []  # 공리스트 1 생성
    empty_list2 = []  # 공리스트 2 생성
    for x in range(len(a)):  # 문자열 길이만큼 반복해서,
        empty_list.append(a[x])  # 우선 공1에 알파벳 삽입
        if a[x] != a[x-1] and a[x] in empty_list2:  # 여기서 삽입된 알파벳이 이전과 동일하지 않으면서 공2에 있다면?
            return False  # 거짓 반환
        empty_list2.append(a[x])  # 그리고 공2에 알파벳 같이 삽입
    return True  # 위 조건에 부합하지 않으면 진실 반환


a = int(input())
count = 0   # 갯수 세기 위한 카운트

for x in range(a):
    word = input()  # 입력받을거 입력받고
    if len(word) > 2:  # 문자열 길이가 3 이상이면
        if distinc(word) == True:  # 그게 그룹단어라면
            count += 1  # 카운트 +1
        else:
            continue  # 그룹단어가 아니면 씹고 진행
    else:
        count += 1  # 두 자리 이하면 그냥 +1

print(count)


# n = int(input())
# cnt = n
# for i in range(n):
#     word = input()
#     for j in range(len(word)-1):  문자열 -1 길이만큼?
#         if word[j] == word[j+1]:   만약 알파벳이 뒤와 같다면
#             pass                  그냥 패쓰하고
#         elif word[j] in word[j+1:]:  ? 인덱스를 나눠서 써버림 ㄷ
#             cnt -= 1             카운트에 -1 해주고 종료
#             break
# print(cnt)      word[j+1:] == 이 알파벳이 한 칸 건너뛴 뒤에 있다면!
