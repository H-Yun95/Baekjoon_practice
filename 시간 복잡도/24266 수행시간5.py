'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''
n = int(input())
print(n**3)
print(3)

'''
이제 대강 시간복잡도의 기초에 대한 감이 잡힌 것 같다. 위 코드의 경우 각각 n번씩 반복하는
코드가 3중첩이 되어 있으므로, 총 연산수는 n^3으로 표현할 수 있을 듯하다.
코드로 나타내면
for x in range(n):
    for y in range(n):
        for z in range(n):
            t += 1
이런 식으로 말이다.
'''
