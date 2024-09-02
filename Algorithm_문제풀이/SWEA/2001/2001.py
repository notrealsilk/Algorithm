# 파리퇴치

# 1. 테스트 케이스 입력
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split()) # N : 파리가 있는 공간 // M : 파리채 공간

# 2. 파리가 있는 공간 2차원 리스트(NxN)로 만들기
    fly_space = []                  # 파리가 있는 공간
    for _ in range(N):
        fly_space.append(list(map(int,input().split())))   # NxN에 들어갈 숫자 입력 받음
        # fly_space = [list(map(int,input().split())) for _ in range(N)] # list comprehension

# 3. MxM 파리채로 NxN공간을 순회
    fly_max = 0  # 파리잡은 최댓수 저장하는 변수

    # MxM 파리채가 NxN공간을 순회
    for i in range(N-M+1):
        for j in range(N-M+1):

# 4.파리채(MxM) 공간 순회하면서 잡은 파리수 구하기
# [i][j]를 기준으로 파리채 공간을 순회하면서 파리수 구함
            fly_cur = 0 # 현재 순회에서 잡은 파리수
            for k in range(M):
                for l in range(M):
                    fly_cur +=fly_space[i+k][j+l] # 파리채는 [i][j]를 기준으로 그 공간만 순회가능

# 5. 현재까지의 파리잡은 최댓수 보다 높은 값이 나오면 갱신
                    if fly_cur > fly_max:
                        fly_max = fly_cur

    print(f"#{tc} {fly_max}")
