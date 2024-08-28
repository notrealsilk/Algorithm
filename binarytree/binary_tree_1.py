
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회 함수
# T = node
def pre_order(T):
    if T:
        print(T, end = ' ') # 본인을 먼저 확인 (전위)
        pre_order(left[T])
        # print(T, end=' ') # 왼쪽을 보고나서, 본인을 확인 (중위)
        pre_order(right[T])
        # print(T, end=' ')# 왼쪽, 오른쪽을 보고 본인을 확인 (후위)

# left, right를 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번 씩만 들어온다고 가정
N = int(input())        # 1번부터 N번까지인 정점
E = N-1 # 간선 수
arr = list(map(int, input().split()))
# 예) left[3] = 2 -> 3번 부모의 왼쪽 자식은 2이다

# 노드 번호가 1부터 시작하므로 0번 인덱스 비워놓기 위해 N+1
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       # 오른쪽 자식번호를 저장할 리스트
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1] # p는 idx 홀수, c는 idx 짝수
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]
    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c         # 왼쪽에 삽입
    else:
        right[p] = c        # 왼쪽 자식은 있는데(완전이진트리 이므로), 오른쪽 자식이 없다면 오른쪽에 삽입
    par[c] = p
# print(left) #[0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
# print(right) #[0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]

# 순회 구현 (루트 노드 찾기)
c = N
while par[c]!= 0:        # 부모가 있으면
     c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root

print(root)
pre_order(root)