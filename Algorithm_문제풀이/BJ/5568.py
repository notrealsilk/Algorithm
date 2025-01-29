# 카드놓기

n = int(input()) # 카드 갯수
k = int(input()) # 뽑을 카드갯수

n_list = [int(input()) for _ in range(n)]
v = [0]*n # 방문 표시

result_set = set()  # 중복 제거 / 결과값 : len()으로 갯수 세주기

def dfs(K, cur):
    # 기저조건 : 뽑은 카드가 k개가 되면 결과에 추가
    if K == k:
        result_set.add(cur)  # 현재 조합을 집합에 추가 (중복 제거)
        return

    # 숫자 뽑기
    for i in range(n):
        if not v[i]:  # 아직 선택되지 않은 카드라면
            v[i] = 1  # 방문 처리
            dfs(K + 1, cur + str(n_list[i]))  # 카드 선택
            v[i] = 0  # 백트래킹 (다시 선택 가능하게 돌려놓음)

dfs(0, "")
print(len(result_set))
