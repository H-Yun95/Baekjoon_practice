'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이
무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지
않는다.
'''


def Max_key(dicts):
    return max(dicts, key=dicts.get)


def answer(dicts):
    for x in range(len(dicts)-1):
        for y in range(len(dicts)-x-1):
            if dicts[x] == dicts[y+1]:
                return '?'
    return Max_key(dicts)


word = input()
Cword = word.upper()
word_dict = {key: 0 for key in dict.fromkeys(Cword).keys()}
for num in Cword:
    for x in word_dict:
        if num == x:
            word_dict[x] += 1
print(Cword)

print(answer(word_dict))
