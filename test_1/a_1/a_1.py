import sys
sys.stdin = open("sample_input.txt", "r")

#from pprint import pprint

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)] # 2차원 리스트
arr_power =  [[0]*N for _ in range(N)] # 하강력을 저장할 리스트

down_cnt = 0 # 하강한 블록 수 카운트
right_cnt = 0 # 우측 하강한 블록 수 카운트

for tc in range(1,10) :
    # 아래 방향 하강 (열 탐색)
    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == 1 : # 셀에 블록이 있으면

                i_t = i
                while arr[i_t][j] == 1: # 하강 가능할 때 까지 반복

                    if arr[i_t+1][j] == 1: # 하강하는 아랫칸에 장애물이 있으면

                        # 하강력 계산
                        n = 0
                        power = 1
                        while arr[i_t+1 +n][j] == 1 :# 하강하는 아랫칸에 장애물이 사라질 때까지
                            power *= arr_power[i_t+1 +n][j] # 하강력 계산

                            if arr[i_t+1 +n][j] == 0:
                                break
                            n += 1

                        # 저항력 계산
                        m = 0
                        resist = 1
                        while arr[i_t+1 +m+1][j] == 1 :# 하강하는 아랫칸에 장애물이 사라질 때까지
                            resist *= arr_power[i_t+1 +n][j] # 하강력 계산

                            if arr[i_t+1 +m+1][j] == 0:
                                break
                            m += 1

                        # 하강력과 저항력 비교해서 블록이 하강 가능한 지 확인
                        if power > resist:
                            pass
                            #arr[]

                    elif arr[i_t+1][j] == 0: # 하강하는 아랫칸에 장애물이 없으면
                        if i > N : # i행이 인덱스 범위 넘어가지 않게
                            arr_power[i_t+1][j] = arr_power[i_t][j]*1.9

                    i_t += 1
    # 하강완료한 블록 갯수 세기
    for n in range(N):
        if arr[N-1][n] == 1: # 블록이 있다면
            down_cnt += 1


    # # 오른쪽 하강 전, 하강력 저장한 리스트 초기화
    # arr_power = 0
    #
    # # 오른쪽 방향 하강 (행 탐색)
    # for i in range(N):
    #     for j in range(N-1):
    #         pass

    # 우측하강 완료한 블록 갯수 세기
    for n in range(N):
        if arr[n][N-1] == 1: # 블록이 있다면
            right_cnt += 1

    print(f"#{tc} {down_cnt} {right_cnt}")

