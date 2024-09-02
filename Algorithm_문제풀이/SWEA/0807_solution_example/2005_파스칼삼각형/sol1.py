# 한 번 계산된 값을 memo 리스트에 저장해두고 재사용함으로써 중복 계산을 피하고 실행 시간을 단축

import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

# 메모이제이션 리스트 생성
memo = [[0 for _ in range(11)] for _ in range(11)]

# 삼각형의 크기가 10이하이므로 10의 파스칼의 값을 생성한다.
for i in range(10):
    for j in range(i + 1):
        # 첫번째 줄과 마지막 줄일 경우(i번째 열 i == j번째 자리.) 1로 채운다.
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            # 나머지 요소는 위 두 개의 숫자의 합
            # memo[i - 1][j - 1] -> 상위, 왼쪽
            # memo[i - 1][j] -> 바로 위 숫자
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

pprint(memo)

for tc in range(1, T + 1):
    N = int(input())

    # 이미 생성해둔 메모이제이션을 이용, 삼각형의 크기만큼만 출력하면 끝
    print(f'#{tc}')
    
    for i in range(N):
        for j in range(i + 1):
            print(f'{memo[i][j]}', end=" ")
        print()
