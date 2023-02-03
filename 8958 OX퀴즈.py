a = int(input())     # 케이스 번호 받기
counter, Total = 0, 0   # O를 비교할 때마다 늘어나는 카운트, 총 점수 토탈 선

for x in range(a):   #케이스 번호만큼 반복
    OXstr = input()    #문자열 입력
    for y in range(len(OXstr)):   #문자열 번호만큼 반복
        if OXstr[y] == 'O':   # 만약 문자가 O라면
            counter += 1      # 카운터에 점수 추가하고
            Total += counter  # 토탈에 카운트된 점수 합산
        else:                 # X라면?
            counter = 0       # 카운터 초기화
    print(Total)              # 토탈 점수를 출력하고
    counter, Total = 0, 0     # 다음 순회를 위해 카운트와 토탈 다시 기초


# for i in[*open(0)][1:]:n=0;print(sum((n:=(n+1)*(j=='O'))for j in i))
