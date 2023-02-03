'''
N개의 숫자가 공백 없이 쓰여있다.
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''
a = int(input())
b = input()
count = 0

for num in b:   # 문자열도 '열'이니까 이게 통할거 같았음
    count += int(num)  # 한자리수씩 정수로 변환해서 가

print(count)

'''
input()
print(sum(map(int,input())))
'''
