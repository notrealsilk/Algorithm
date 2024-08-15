import sys
sys.stdin = open("input1.txt", "r")

# 테스트 케이스 입력
T = int(input())
for tc in range(1,T+1):
    # 풍선이 M개씩 N개의 줄
    N,M = map(int,input().split())
    # N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수
    arr = [list(map(int,input().split())) for i in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    # 꽃가루 최대 개수 (최종 결과)
    max_balloon = 0

    # NxM순회
    for y in range(N):
        for x in range(M):
            # 현 순회에서의 꽃가루 개수
            cur_balloon = arr[y][x] # 현 위치의 꽃가루 개수 카운트
            # 델타 순회
            for d in range(4):
                # 꽃가루 갯수만큼 이동해서 또 순회
                for k in range(1, arr[y][x]+1):
                    nx = x + dx[d] * k
                    ny = y + dy[d] * k

                    if 0 <= nx < M and 0 <= ny < N :
                        cur_balloon += arr[ny][nx]

            # 최댓값 갱신
            # if max_balloon < cur_balloon:
            #     max_balloon = cur_balloon
            max_balloon = max(max_balloon,cur_balloon)

    print(f"#{tc} {max_balloon}")
