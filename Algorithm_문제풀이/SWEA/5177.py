def enq(n): # n : 자연수
    global last
    last += 1 # 마지막 노드 추가 (for 완전이진트리)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last # c : 자식노드
    p = c // 2 # p : 부모노드
    while p>=1 and h[p]>h[c]: # 부모노드가 존재하고, 부모노드가 더 크다면
        h[p], h[c] = h[c], h[p] # 교환
        c = p # 조상노드 타고 올라가기
        p = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N : 자연수 갯수
    arr = list(map(int, input().split())) # arr :  서로 다른 N개의 자연수

    h = [0]*(N+1) # 최소힙
    last = 0 # 힙의 마지막 노드 번호

    for num in arr : # N개의 자연수를 최소힙으로 만들기
        enq(num)

    # 조상노드의 합 구하기
    result = 0
    p = N//2
    while p >= 1:
        result += h[p]
        p = p//2 # 다음 조상 노드를 위해 갱신
    print(f"#{tc} {result}")
