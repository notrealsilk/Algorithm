import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
for tc in range(1,T+1):
    # N :  돌의 갯수 / M : 뒤집기 횟수
    N, M = map(int, input().split())
    # N_rock : N개 돌의 초기 상태
    N_rock = list(map(int, input().split()))
    # i : 기준 돌 / j : 마주보는 돌 갯수
    for _ in range(M):
        i,j = map(int, input().split())

        # 1번째부터 돌을 세므로 이므로 인덱스로 접근할 때는 -1 씩 해줘야 함
        #N_rock[i-1]

