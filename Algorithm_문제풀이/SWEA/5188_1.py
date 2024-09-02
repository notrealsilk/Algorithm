def route(x, y, x_cnt, y_cnt, cur_sum):
    global min_sum

    # 오른쪽 아래 도착하면 최소값 갱신
    if x == N - 1 and y == N - 1:
        min_sum = min(min_sum, cur_sum)
        return

    # 오른쪽으로 이동 (x_cnt가 남아 있을 때만)
    if x_cnt > 0:
        route(x + 1, y, x_cnt - 1, y_cnt, cur_sum + arr[x + 1][y])

    # 아래로 이동 (y_cnt가 남아 있을 때만)
    if y_cnt > 0:
        route(x, y + 1, x_cnt, y_cnt - 1, cur_sum + arr[x][y + 1])


# 테스트 케이스 처리
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 1700 # min_sum : 숫자 합계의 최소 (최종결과)

    route(0, 0, N - 1, N - 1, arr[0][0]) # x좌표, y좌표, x가 갈 수 있는 최대 위치, y가 갈 수 있는 최대 위치, 현재 좌표의 숫자

    # 결과 출력
    print(f"#{t} {min_sum}")
