import sys
sys.stdin = open("input.txt","r")

def is_baby_gin(nums):
    # 카드 숫자를 카운팅할 배열
    counts = [0] * 10

    # 각 숫자의 등장 횟수 세기
    for num in nums:
        counts[num] += 1

    triplet = 0
    run = 0

    i = 0
    while i < 10:
        # Triplet 체크
        if counts[i] >= 3:
            triplet += 1
            counts[i] -= 3
            continue

        # Run 체크
        if i <= 7 and counts[i] >= 1 and counts[i + 1] >= 1 and counts[i + 2] >= 1:
            run += 1
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1
            continue

        i += 1

    # 트리플릿과 런이 각각 두 개씩 발견되면 베이비 진
    return triplet + run == 2


# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().strip()))

    if is_baby_gin(nums):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
