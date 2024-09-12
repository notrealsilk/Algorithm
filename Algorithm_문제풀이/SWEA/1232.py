# 후위연산
def postorder(node):
    # 리프노드일 때, 숫자 반환 (재귀의 끝)
    if not graph[node]:
        return int(opers[node])

    left = postorder(graph[node][0]) # 왼쪽 서브트리 숫자
    right = postorder(graph[node][1]) # 오른쪽 서브트리 숫자

    if opers[node] == '-':
        return left - right
    elif opers[node] == '+':
        return left + right
    elif opers[node] == '*':
        return left * right
    else:
        return left / right


for tc in range(1,11):
    N = int(input()) # N : 노드 갯수
    graph = [[] for _ in range(N+1)] # 노드 연결 여부 저장
    opers = [''] * (N+1) # 숫자, 연산자 모두 저장해야하므로 빈 문자열로 저장

    # 입력받기
    for _ in range(N):
        # (노드번호 / 연산자,숫자 / 왼쪽 자식 / 오른쪽 자식)
        temp = input().split()
        node = int(temp[0])
        opers[node] = temp[1]

        if len(temp) == 4: # 연결여부 체크
            graph[node].append(int(temp[2])) # 왼쪽
            graph[node].append(int(temp[3])) # 오른쪽

    result = postorder(1)
    print(f"#{tc} {int(result)}")
