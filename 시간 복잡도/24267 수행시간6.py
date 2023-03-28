'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
t = 0
for x in range(1, n-1):
    t += x*(x+1)//2

print(t)
# 밑의 코드로 돌려보았을 때, 연산은 n-2 이하 모든 정수 각각의 구간합으로
# 이루어져 있다는 것을 발견했다.
# Ex) n=7
# (5+4+3+2+1)+(4+3+2+1)+(3+2+1)+(2+1)+(1)
# 그러므로, n-2만큼 반복해서 점차 작게 서로를 더해가는 코드를 작성
# 물론 3중첩이므로, 최고차항은 3

'''
n = int(input())
t = 0
for x in range(n-2):
    for y in range(x+1, n-1):
        print(t)
        for z in range(y+1, n):
            t += 1

print(t)
'''
'''
n = int(input())
print(int(n*(n-1)*(n-2)/(2*3))) = n^3-3n^2+2n
print(3)

단순 식으로는 이렇게 작성하면 되는 듯하다.
생각해보면 실제 연산을 반복문으로 하기 싫어서 만든게 곱셈인데
반복한다는 생각이 웃길 따름이긴함 ㅋㅋㅋㅋㅋㅋㅋㅋ
'''
