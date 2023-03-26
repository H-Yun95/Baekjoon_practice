'''
창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

삼각형의 세 각을 입력받은 다음, 

세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.
'''


def triangle(a, b, c):
    if a + b + c != 180:
        return 'Error'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isosceles'
    else:
        return 'Scalene'


a = int(input())
b = int(input())
c = int(input())

print(triangle(a, b, c))

'''
T = [int(input()) for _ in range(3)]

if sum(T) != 180:
    print("Error")
elif len(set(T)) == 1:
    print("Equilateral")
elif len(set(T)) == 2:
    print("Isosceles")
else:
    print("Scalene") 이렇게 자료를 set해서 갯수로 판단하는 것도 괜찮을듯...
'''
