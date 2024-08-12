# a : 주어진 배열 / k : 결정할 원소 / n : 배열의 길이 (원소 갯수).. 필요한 크기가 맞춰서 설정가능
def backtrack(a, k, n):
# 후보를 저장할 배열을 만듬 (최대한 가질 수 있는 원소의 갯수)
    c = [0] * MAXCANDIDATES


    if k == n:
        process_solution(a, k)  # 트리 바닥, 즉 답이면 원하는 작업을 한다.
    else:
    # ncandidates .. 추천된 후보(=c)수가 리턴 값으로 들어옴..len(c)
        ncandidates = construct_candidate(a, k, n, c)  # c에 현재 추천한 후보 추천 및 저장
        for i in range(ncandidates):  # 추천해준 후보를 하나씩 꺼내서 확인
            a[k] = c[i]
            backtrack(a, k + 1, n)  # 다음번 backtrack()을 부름


def construct_candidate(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 2  # 후보를 저장할 크기
NMAX = 4  # 부분 집합 크기 ..num의 크기
a = [0] * NMAX
num = [1, 2, 3, 4]
backtrack(a, 0, 4)