import sys
sys.stdin = open("input.txt","r")

T = int(input())
for i in range(1, T+1):
    N = int(input()) # N : 사람 수 이자 일 갯수
    arr = [list(map(int,input().split())) for _ in range(N)] # Pi, j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위

    working = [0] * N # i번째 사람(idx)이 맡을 일(인덱스 안의 값)

    for j in range(N): # 일
        cur_per = 0 # 현재 순회에서 일을 맡으면 좋은 직원의 확률
        for i in range(N): # 직원
            if cur_per < arr[i][j] : # 더 일을 잘하는 직원을 찾았다면
                cur_per = arr[i][j]  # 갱신

        # 직원에게 실제로 일 할당
        if working[j]: # 근데! 이미 그 직원을 다른 일을 할당 받았다면
            for k in range(N): # 아직 놀고있는 직원 찾기
                if working[k] == 0: # 놀고 있는 직원 찾았다면
                    pass


        working[j] = cur_per



