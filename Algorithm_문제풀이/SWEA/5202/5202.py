import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N : 신청서 개수
    work_list = [list(map(int,input().split())) for _ in range(N)] # 작업시간, 종료시간 입력받기

    # 종료 시간이 빠른 순으로 작업 리스트 정렬 (버블 정렬)
    for i in range(N-1):
        for j in range(i+1,N):
            if work_list[i][1] > work_list[j][1]:
                work_list[i],work_list[j] = work_list[j],work_list[i]

    cnt = 0 # 화물차를 최대로 이용할 수 있는 횟수 (최종 결과)
    end_time = 0 # 현재 작업을 종료한 시간

    for j in range(N):
        if work_list[j][0] >= end_time: # 작업을 시작할 수 있다면
            cnt += 1
            end_time = work_list[j][1]

    print(f"#{tc} {cnt}")