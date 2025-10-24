N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]

dirs = (-1, 0, 1) # 우주선이 나아갈 수 있는 방향
result = float('inf') # 최소 연료

def dfs(n, m, prev_dir, fuel):
    global result

    # 종료조건
    if n == N - 1:
        total = fuel + cost[n][m]
        result = min(result, total)
        return

    # 시작
    # 이번 턴 사용 연료
    new_fuel = fuel + cost[n][m]

    # 가지치기
    if new_fuel >= result:
        return

    # 우주선 이동
    for d in dirs:
        if d == prev_dir:
            continue
        nm = m + d
        if 0 <= nm < M:
            dfs(n + 1, nm, d, new_fuel)

for m in range(M):
    dfs(0, m, None, 0) # (n위치, m위치, 이전에 움직인 방향, 지금까지 연료)

print(result)
