# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
visited = []


# 버전1
# 기저조건의 가지치기..문제에서 발견하기 힘듦
def dfs(level, sum, idx):
    # 가지치기 : 합이 10이면 종료
    if sum == 10:
        print(*visited)
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return

    # 후보군의 가지치기..방문처리로 함 / 파라미터로 후보군 없애주기 (파라미터에 idx할당)
    # idx의 의미: 현재 수보다 작은 수들은 이미 고려돼있기에
    # idx보다 작은 후보는 pass
    for i in range(idx, len(arr)):
        # 가지치기 : 이미 사용한 숫자라면 생략ㅉ
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


# 버전2
# 트리 구조처럼 사용하면 훨씬 쉽고 빠르다
# 이진트리처럼 사용(후보를 사용하느냐 vs 마느냐) 하면 훨씬 쉽고 빠름
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*visited)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    visited.append(arr[level])
    dfs2(level + 1, sum + arr[level])
    visited.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)