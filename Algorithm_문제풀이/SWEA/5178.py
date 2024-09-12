T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split()) # N : 노드의 개수 / M : 리프 노드의 개수 / L : 값을 출력할 노드 번호
    arr = [0] * (N+1)

    # arr에 idx에 따른 num저장 (입력받으면서)
    for _ in range(M):
        idx, num = map(int, input().split())
        arr[idx] = num

    # 리프노드에서 거슬러 올라가면서 부모 노드 값 +=
    for i in range(N,0,-1):
        p = i // 2
        arr[p] += arr[i]

    print(f"#{tc} {arr[L]}")