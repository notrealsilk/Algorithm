def in_order(node):
    global cur
    if node <= N:  # 노드가 N을 넘어가면 안 됨
        in_order(node * 2)  # 왼쪽 자식 노드로 이동
        tree[node] = cur # 현재 노드에 값 채우기
        cur += 1  # 다음에 채울 값 증가
        in_order(node * 2 + 1)  # 오른쪽 자식 노드로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    cur = 1 # 트리에 넣을 값 (재귀 함수 작동하면서 계속 갱신)

    # 중위 순회로 트리에 값 채우기
    in_order(1)

    print(f"#{tc} {tree[1]} {tree[N//2]}")