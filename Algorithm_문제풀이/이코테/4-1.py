# 상하좌우
# 5
# R R R U D D
# 3 4

N = int(input()) # 공간 크기
rute = list(map(str, input().split())) # 이동 계획

coordinate = (1,1) # 시작 좌표

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(len(rute)):
    if rute[i] == 'L':
        pass

print(coordinate[0], coordinate[1])
