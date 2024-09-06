def backtracking(i, cur_prob):
    global max_prob
    # 가지치기 : 현재 확률이 지금까지 찾은 최대 확률보다 작으면 더 이상 진행할 필요 없음
    if cur_prob <= max_prob:
        return

    # 기저조건
    # 모든 일 배정했다면, 최대 확률 찾기
    if i == N:
        max_prob = max(max_prob, cur_prob)
        return

    # i번째 직원이 j번째 일을 맡았을 경우들을 탐색
    for j in range(N):
        if not assigned[j]:  # j번 일이 할당되지 않았을 때
            assigned[j] = True  # 방문 표시
            backtracking(i+1, cur_prob * (arr[i][j] / 100))  # 확률로 환산해서 할당
            assigned[j] = False  # 방문 끝났으므로 반납

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N : 사람 수 이자 일 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]  # Pi,j: i번 사람이 j번 일을 성공할 확률

    max_prob = 0  # 최대 성공 확률
    assigned = [False] * N  # 할당 여부 표시

    backtracking(0, 1)  # 0번째 직원부터 시작, 초기 확률 = 1

    print(f"#{tc} {max_prob * 100:.6f}")  # 소수점 6자리까지 출력
