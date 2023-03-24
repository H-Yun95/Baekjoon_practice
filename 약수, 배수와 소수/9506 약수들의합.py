'''
문제
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

입력
입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

입력의 마지막엔 -1이 주어진다.

출력
테스트케이스 마다 한줄에 하나씩 출력해야 한다.

n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

이때, 약수들은 오름차순으로 나열해야 한다.

n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.
'''

while True:
    try:
        a = int(input())
        answer = []                      # 정답을 위한 빈 리스트 선언

        for x in range(a):
            if a % (x+1) == 0:
                answer.append(x+1)
        answer.remove(answer[-1])     # 앞에서 보여줬던 약수 리스트 생성 복붙
        # 다만, 마지막 원소를 빼줌으로 [n(1), n(2), ... n(n-1)]의 리스트로 마무리 작업해줌
        if a == sum(answer):      # 이제 a가 완전수라면?
            print(f'{a} = 1', end='')
            for x in range(len(answer)-2):
                print(f' + {answer[x+1]}', end='')
            # 출력. 중간에 한번 꼬여서 실패했음. 마지막에 end='' 때문이었던듯
            print(f' + {answer[-1]}')
        else:
            print(f'{a} is NOT perfect.')
        answer = []   # 한번 돌면 초기화. 근데 이제보니 이건 필요가 없네?
    except:
        break   # -1 입력 시 예외처리


'''
while 1:
	N,M=int(input()),[]    똑같이 선언했지만 이냥반은 몬가 다르다. 한 줄에 인풋과 공리스트 동시 선언.
	                       이게 파이썬의 강점인듯
    if N<0:break           n이 음수면 바로 브레이크를 상단에 박아버리기
	for i in range(1,N):   1부터 n 까지
		if N%i<1:
			M.append(i)    이렇게 약수 리스트 생성
	
    if sum(M)==N:print(N,"="," + ".join(list(map(str,M))))   .join 함수로 한번에 출력하는 듯.
	else:print(N,"is NOT perfect.")
'''
