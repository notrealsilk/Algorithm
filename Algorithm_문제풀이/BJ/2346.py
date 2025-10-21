n = int(input())  # 풍선 개수
balloon = list(map(int, input().split())) # 풍선 리스트 (변함)
idx = list(range(1, n+1)) # 원래 풍선 리스트 (인덱스 값 추출해서 result에 넣을 용도)
nx = 0 # 다음 터트릴 풍선 인덱스
result = []

while balloon:
    # 현재 위치
    move = balloon[nx]

    # 터트림
    result.append(idx[nx])
    idx.pop(nx)
    balloon.pop(nx)

    # 더 이상 터트릴게 없으면
    if not balloon:
        break

    # 다음번 풍선 터트리기 위한 인덱스 정비
    if move > 0:
        nx = (nx + move - 1) % len(balloon)
    else:
        nx = (nx + move) % len(balloon)

print(*result)
