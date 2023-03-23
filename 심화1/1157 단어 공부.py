'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이
무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지
않는다.
'''


def Max_key(dicts):      # 딕셔너리에서 가장 큰 밸류의 키 반환함수
    return max(dicts, key=dicts.get)  # max 함수 사용, 키는 .get으로 들고 오는듯


def Sort_dict(dicts):  # 딕셔너리를 리스트로 정렬해 주는 함수
    return sorted(dicts.items(), key=lambda x: x[1], reverse=True)
    # 람다를 쓰는데 이건 뭔지 모르겟다... 조만간 할 듯
    # 내림차순 정렬을 위해 리버스에 트루


word = input()   # 문자열 입력
Cword = word.upper()  # 그 문자열을 전부 대문자로 변환
word_dict = {key: 0 for key in dict.fromkeys(Cword).keys()}  # 문자열로 딕셔너리 생성
for num in Cword:   # 생성된 문자열만큼
    for x in word_dict:    # 딕셔너리를 순회
        if num == x:   # 만약 문자열 알파벳이 딕셔너리 키 값에 있다면?
            word_dict[x] += 1  # 그 키의 밸류에 +1
            # 위 작업으로 알파벳 수 만큼의 밸류를 가진 dict 생성
new_list = Sort_dict(word_dict)  # 그리고 이걸 내림차순으로 정렬

if len(new_list) > 1:   # 이건 알파벳 하나만 입력되면 인덱스 오류가 떠서 설정
    if new_list[0][1] == new_list[1][1]:  # 그래서 제일 큰 값과 둘째 값이 같으면?
        print('?')  # 물음표 출력
    else:
        print(Max_key(word_dict))  # 아니라면 제일 큰 값 출력
else:
    print(Max_key(word_dict))

'''
L=[0]*26
for i in input():
    L[(ord(i)-1)%32]+=1    ord 함수를 사용
if L.count(max(L))>1:
    print('?')
else:
    print(chr(L.index(max(L))+65))   index와 max라...
    '''
