T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 가로, M : 세로
    data = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0  # 가장 긴 구조물(최종 결과)

    # 행 탐색
    for i in range(N):
        tem_result = 0
        for j in range(M):
            if data[i][j] == 1:
                tem_result += 1
            if data[i][j] == 0 or j == M - 1:
                if tem_result > 1:  # 최소 크기(2m 이상)인 경우만 고려
                    if max_result < tem_result:
                        max_result = tem_result
                tem_result = 0

    # 열 탐색
    for j in range(M):
        tem_result = 0
        for i in range(N):
            if data[i][j] == 1:
                tem_result += 1
            if data[i][j] == 0 or i == N - 1:
                if tem_result > 1:  # 최소 크기(2m 이상)인 경우만 고려
                    if max_result < tem_result:
                        max_result = tem_result
                tem_result = 0

    print(f"#{tc} {max_result}")
