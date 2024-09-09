T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 터널의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한 장소의 세로 위치 R, 가로 위치 C, 탈출 후 소요된 시간 L
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]  # 지하터널 지도

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우
    tunnel = {1: [dxy[0], dxy[1], dxy[2], dxy[3]],  # 지하터널 구조물
              2: [dxy[0], dxy[1]],
              3: [dxy[2], dxy[3]],
              4: [dxy[0], dxy[3]],
              5: [dxy[1], dxy[3]],
              6: [dxy[1], dxy[2]],
              7: [dxy[0], dxy[2]]}

    location = [[R, C]]  # 탈주범 초기 위치
    visited = [[False] * M for _ in range(N)]  # 방문 체크
    visited[R][C] = True # 탈주범 초기 위치
    cnt = 1  # 탈주범이 위치할 수 있는 장소의 개수 (초기 위치 포함)

    for t in range(1,L):  # 탈출 경과 시간
        cur_loc = []  # 현재 위치에서 탈주범이 갈 수 있는 위치
        for loc in location:
            cur_tunnel_type = tunnel_map[loc[0]][loc[1]]  # 현재 터널의 유형
            for direction in tunnel[cur_tunnel_type]:  # 현재 터널이 이동 가능한 방향
                nx = loc[0] + direction[0]
                ny = loc[1] + direction[1]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:  # 유효한 범위 내에 있는지 확인
                    next_tunnel_type = tunnel_map[nx][ny]  # 다음 위치의 터 널 유형
                    if next_tunnel_type > 0:  # 터널이 있으면
                        # 현재 방향과 연결될 수 있는지 확인
                        reverse_dir = [-direction[0], -direction[1]]  # 반대 방향 체크해서 연결여부 확인
                        if reverse_dir in tunnel[next_tunnel_type]:
                            visited[nx][ny] = True
                            cur_loc.append([nx, ny])
                            cnt += 1
        location = cur_loc  # 다음 시간대 위치 갱신

    print(f"#{tc} {cnt}")
