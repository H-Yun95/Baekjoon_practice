'''
입력 받은 대로 출력하는 프로그램을 작성하시오.
'''

while True:
    try:
        a = input()
        print(a)
    except:
        break
# try, except 중 except는 오류날 수 있는 요건에 '예외처리' 하는 역할
