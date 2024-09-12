T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split()) # E : 간선의 갯수 / N : 서브트리의 루트노드
    arr = list(map(int,input().split())) # E개의 부모 자식 노드 번호 쌍

    left = [0]*(E+2) # 왼쪽 자식 노드
    right = [0]*(E+2) # 오른쪽 자식 노드

    # 노드 채우기
    for i in range(E):
        idx = arr[i*2]
        num = arr[i*2+1]
        if left[idx] == 0: # 왼쪽 자식 노드가 비어있다면
            left[idx] = num
        else: # 왼쪽 자식 노드가 채워져있고, 오른쪽 자식 노드가 비어있다면
            right[idx] = num

        cnt = 0  # 서브트리에 속한 노드의 개수
        queue = [N]  # 탐색을 시작할 노드를 담는 큐 (리스트로 구현)

    # 서브트리 갯수 탐색 시작
    while queue:
        i = queue.pop(0)  # 큐의 맨 앞에서 노드를 꺼내기
        cnt += 1  # 현재 노드를 포함

        if left[i]:  # 왼쪽 자식 노드가 존재하면
            queue.append(left[i])  # 큐에 추가
        if right[i]:  # 오른쪽 자식 노드가 존재하면
            queue.append(right[i])  # 큐에 추가

    print(f"#{tc} {cnt}")

