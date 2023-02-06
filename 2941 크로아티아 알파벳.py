'''
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, 
a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 
알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 
보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 
한 글자씩 센다.
'''


word = list(input())  # 문자열 입력
croa_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0    # 제시돤 알파벳들의 리스트 작성, 카운트 선언

for x in range(len(word)-2):  # dz= 만을 걸러내기 위한 작업
    if word[x] + word[x+1] + word[x+2] == 'dz=':
        count += 2  # dz=가 알파벳 3개오 이루어지므로 카운트 += 2

for y in range(len(word)-1):  # 걸러낸 뒤
    if word[y] + word[y+1] in croa_alpha and word[y-1] + word[y] + word[y+1] != 'dz=':
        count += 1   # 크로아티아 알파벳에 해당하고, z=가 dz=의 부속이 아니라면
        # 카운트에 += 1
print(len(word)-count)   # 솔직히 위 y-1땜에 인덱스 에러날 줄 알았는데.... 그건 또 아닌가보다

# lj/e/s=/nj/a/k
# d/dz=/z=

# croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# word = input()

# for i in croatia:
#     word = word.replace(i,'*')  ! 아 이건 크로아티아 알파벳에 해당하는
#                                   단어들을 별첨자로 바꾸는 작업으로 해결한 것 같다.
# print(len(word))
