N = int(input())
row = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    nl = row[i] # 앞에 나보다 키 큰 사람이 올 자리를 비워두고, 내가 갈 위치
    j = 0
    while j < N:
        if result[j] == 0:
            # 내 위치 찾음! result에 넣기!
            if nl == 0:
                result[j] = i + 1
                break
            nl -= 1
        j += 1

print(*result)
