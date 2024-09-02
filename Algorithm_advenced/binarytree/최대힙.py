'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''


# 최대힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지) / len 연산을 피하기 위해 이런식으로 마지막 노드의 인덱스 관리
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모번호 계산
    # 제자리를 찾거나 루트노드(루트노드는 부모가 없으므로..)일 때 까지 반복
    while p >= 1 and h[p] < h[c]:   # 부모가 있는데, 더 작으면 (비교)
        h[p], h[c] = h[c], h[p]  # 교환 (swap)
        c = p
        p = c//2

# 1. 루트에 마지막 노드 값을 복사
# 2. 마지막 노드 삭제
# 3. 자리를 찾는다
def deq():
    global last
    tmp = h[1]   # 루트의 키값 보관
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2         # 왼쪽 자식 확인
    while c <= last:  # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽자식이 있고 더 크면
            c += 1

        if h[p] < h[c]: # 부모가 작으면 swap
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:   # 부모가 작은 경우가 없다 = 제자리를 찾았다
            break
    return tmp


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대힙 (완전 이진 트리 보장 -> 1차원 리스트로 구현/N노드의 자식.. N*1,N*2+1)
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')
