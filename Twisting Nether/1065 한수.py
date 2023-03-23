'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을
작성하시오. 
'''
def Order_m(a):    # 되려 셀프넘버보단 쉬웠던듯...
    if a < 100:    # 100 미만은 무조건 한수로 치는 듯 했다.
        return a   # 그래서 그대로 출력
    elif 100 <= a < 1000:   # 100이상 1000 미만부터가 문제인데
        a = str(a)    # 우선 인덱스 구분을 위해 문자열로 변경
        if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):  # 인덱스 간의 차를 비교
            return int(a)  # 그래서 차이가 같으면 a 정수로 반환
    elif a == 1000:   # 그럼 1000은?
        return None   # 그냥 노반환 ㅋ
    else:             # 근데 여기서 다른 넘버들은 0으로 처리해도 알아서 None이
        return 0      # 나오던데 1000은 왜 굳이 None을 붙여야 하는지 몰겟다

a = int(input())   # 정수 입력
num_list = [x for x in range(1,a+1)]  # 정수 크기의 리스트 생성
count = []   # 숫자 세알리는 공리스트 생성

for num in num_list:
    if Order_m(num) != None:  # 함수로 변환한 값이 한수라면?
        count.append(num)     # 카운트에 적립

print(len(count))   # 카운트 길이 출력
