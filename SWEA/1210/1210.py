# ladder

import sys
sys.stdin = open("input.txt", "r")

# 1. 테스트 케이스 번호 입력 -> 입력되는 테스트 케이스를 2차원리스트(ladder)로 저장
# 테스트 케이스는 100개씩 100번 입력됨 (100 X 100 행렬)
for test_case in range (1, 11) :
    tc = int(input())
    N = 100
    ladder = [list(map(int,input().split())) for _ in range (N)]   # 100 X 100 행렬

# 2. 도착지점 ~ 출발지점으로 사다리를 이동하는 방식으로 탐색하려고 함
# ladder[99][0] ~ ladder[99][99]를 탐색하면서 도착점인 2 찾기 (반복문)
    x = 0 # j값 = 열값
    for x in range(0, N):
        if ladder[N-1][x] == 2 :
            last_point_j = x
            break

# 3. 이동하면서 현재지점(ladder[i][j])을 기준으로 사디리타기 규칙에 따라 사다리를 탐
# 만약, [i][j]에서 양 옆 [i][j-1] [i][j+1]이 1이라면 현재지점에서 옆으로 이동(행을 따라 이동)
# 옆으로 이동하는 과정에서 [i-1][j]가 1이 이라면 위로 이동 (열을 따라 이동)
    for i in range (N-1, 0, -1) : # 인덱스 i값 = 행 값
        for j in range():



# 4. ladder[0][0]~ladder[0][99]에 도달하면 사다리 타기 끝
# ladder[0][j] 에서 j값이 결과

print(f"#{tc} {result}")
