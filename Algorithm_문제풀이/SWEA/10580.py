T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 전선 갯수
    arr = [list(map(int,input().split())) for _ in range(N)] # 전선이 걸려있는 위치

    arr.sort() # 정렬해서 전봇대 높이대로 순회
    cnt = 0 # 교차점 갯수 (최종 결과)

    # 모든 전선 쌍을 비교
    for i in range(1, N):
        for j in range(i): # i로 찾은 전선보다 아래에 있는 전선들 비교
            if arr[j][1] > arr[i][1]:  # 두 번째 전봇대의 높이(b)가 교차 조건
                cnt += 1

    # 결과 출력
    print(f'#{tc} {cnt}')



