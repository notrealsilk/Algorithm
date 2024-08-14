import sys
sys.stdin = open("sample_input.txt", "r")

# 입력값 받기
T = int(input())
for tc in range(1, T+1):
    # N : N의 배수 번호를 위한 숫자 N
    N = int(input())

    # num : 현재까지 본 숫자를 리스트에 저장
    num = []

    i = 0 # 양 세는 배수

    # while문 : len(num) == 10이 될 때까지,
    # 즉, [0,1,2,3,4,5,6,7,8,9]가 될 때까지 반복
    while len(num) < 10:
        i += 1
        cur_num = str(N * i)

        # 문자열 cur_num를 순회하면서 num 리스트에 해당 숫자 문자열들 저장
        for j in cur_num:
            # num 리스트에 이미 저장하지 않은 숫자들만 append
            if j not in num:
                num.append(j)

    # 호석이는 xN번 양을 세고 있다.
    print(f"#{tc} {i*N}")