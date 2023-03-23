a = int(input())   # 케이스 넘버 입력

for x in range(a):   # 케이스 넘버만큼 반복
    student = list(map(int, input().split()))  # 과목 수와 점수를 입력
    sub_num = student[0]    # 여기서 과목 수는 별개의 변수로 지정
    del student[0]    # 과목 수를 삭제해서 온전한 점수 리스트로 변경
    count = 0    # 평균을 넘는 점수를 세기 위한 카운트 선언
    for y in range(sub_num):   # 과목 수만큼 반복(있는 변수는 써야제)
        if student[y] > sum(student)/sub_num:  # 개별 성적 하나가 평균을 넘는다면?
            count += 1   # 카운트에 1 적립
    print(f'{count/sub_num*100:.3f}%')   # 형식 맞춰서 출


# for i in[*open(0)][1:]:a,*b=map(int,i.split());print(f'{sum(a*j>sum(b)for j in b)/a:.3%}')
