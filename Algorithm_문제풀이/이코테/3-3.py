# 한 행에 (가장 큰수 - 가장 작은수)의 값이 작은 행을 선택
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
########
# 2 4
# 7 3 1 8
# 3 3 3 4
########

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

Min_N_idx = 0 # 차가 가장 작은 행 인덱스
Min_N = 101

for i in range(N):
    tem_N = (max(arr[i]) - min(arr[i]))

    if Min_N > tem_N:
        Min_N = tem_N
        Min_N_idx = i

print(max(arr[Min_N_idx]))
