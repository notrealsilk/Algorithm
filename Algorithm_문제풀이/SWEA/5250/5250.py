import sys
sys.stdin=open('sample_input.txt','r')

import heapq

dir = [[-1,0],[0,1],[1,0],[0,-1],] # 상우하좌
def dijk(N,field):
    pq = [(0, 0, 0)] # 우선순위 //(현재까지 연료 소비량, x좌표, y좌표)
    distance = [[float('inf')] * N for _ in range(N)] # 최단거리 테이블
    distance[0][0] = 0 # 출발점은 연료 0

    # 시작
    while pq:
        cur_fuel,x,y = heapq.heappop(pq)

        # 함수 종료 조건 =>  도착
        if x == N-1 and y == N-1:
            return cur_fuel # 연료 소비량 반환

        # 인접한 곳의 방향 탐색
        for i in range(4):
            nx,ny = x+dir[i][0],y+dir[i][1]

            if 0 <= nx < N and 0 <= ny < N: # 범위 내에 있다면
                # 한 칸 이동
                nx_fuel = cur_fuel+1 # 현재까지의 연료 + 이동했으므로 연료 +1
                # 높이가 있다면 그만큼 연료 소비하면서 이동
                if field[nx][ny]>field[x][y] :# 높이에 따른 연료 -> 높이 차이가 있다면
                    nx_fuel += (field[nx][ny]-field[x][y])

                # 최소 연료 찾았으면 갱신
                if nx_fuel < distance[nx][ny]:
                    distance[nx][ny] = nx_fuel
                    #print(distance)
                    heapq.heappush(pq,(nx_fuel,nx,ny))

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 가로, 세로 칸수
    field = [list(map(int, input().split())) for _ in range(N)] # 지역 높이

    result = dijk(N,field)
    print(f'#{tc} {result}')