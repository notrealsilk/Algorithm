# a : 주어진 배열 / k : 결정할 원소 / n : 배열의 길이 (원소 갯수).. 필요한 크기가 맞춰서 설정가능

# 후보군을 정해서 BFS로 순열 구하기
def backtrack(a, k, n):
    # 후보를 저장할 배열을 만듬 (최대한 가질 수 있는 원소의 갯수)
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0, k):
            print(a[i], end=" ")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        # a[0]~ a[k-1]까지 사용된 적이 없는 후보 확인
        in_perm[a[i]] = True  # a[k]에 들어갈 후보를 정해서 c에 할당

    # 후보의 숫자
    ncandidates = 0

    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
backtrack(a, 0, 3)
