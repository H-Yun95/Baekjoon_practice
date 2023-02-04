'''
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 
몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 
한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
'''


def Sangsu(a):   # 순서를 바꾸는 함수
    cha_a = list(a)  # 우선 받은 문자열을 리스트로 변환
    return_num = []  # 뒤집은 원소를 하나씩 스텍하는 공리스트
    for x in range(3):  # 3자리수니까 3번 반복
        return_num.append(cha_a[2-x])  # 거꾸로 공리스트에 삽입
    return ''.join(return_num)  # 리스트 원소를 문자열로 출력


fir_n, sec_n = input().split()   # 두 개의 넘버를 스트링으로 받고

print(max(int(Sangsu(fir_n)), int(Sangsu(sec_n))))
# 두 수를 각각 상수함수로 씌우고 정수로 바꿔준 뒤, 더 큰 값을 받음

# print(max(input()[::-1].split()))
