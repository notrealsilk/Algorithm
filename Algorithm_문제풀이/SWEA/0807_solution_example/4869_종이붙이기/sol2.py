# 재귀

import sys

sys.stdin = open('input.txt')


def count_ways(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    else:
        return count_ways(n - 10) + 2 * count_ways(n - 20)


# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {count_ways(N)}')
