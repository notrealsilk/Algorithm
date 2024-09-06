# import sys
# sys.stdin = open("input.txt","r")

def backtrack(i, prob):
    global max_prob
    # 가지치기: 현재 확률이 최대 확률보다 작으면 더 이상 진행하지 않음
    if prob <= max_prob:
        return
    # 모든 일을 배정했을 때
    if i == N:
        max_prob = max(max_prob, prob)
        return
    # i번째 직원이 j번 일을 맡았을 때의 경우 탐색
    for j in range(N):
        if not assigned[j]:  # j번 일이 아직 할당되지 않았다면
            assigned[j] = True
            backtrack(i + 1, prob * (arr[i][j] / 100))  # 확률을 곱함
            assigned[j] = False  # 다시 원래 상태로 돌림

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_prob = 0  # 최대 성공 확률
    assigned = [False] * N  # 각 일이 할당되었는지 여부를 추적

    backtrack(0, 1)  # 0번째 직원부터 시작, 초기 확률은 1

    # 결과 출력 (소수점 아래 6자리)
    print(f"#{tc} {max_prob * 100:.6f}")
