# Flatten

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11): # 테스트 케이스 10번 반복
    dump = int(input()) # 덤프횟수 입력받음
    box_high = list(map(int, input().split())) # 상자높이 입력받음

    # 최대 dump 횟수 이전에 과정에 완료되면 bresk
    for _ in range(dump): # 최대 dump횟수 만큼 반복

        # dump 한 번 할 때마다 max, min변수 값이 초기화되야 for문을 돌면서 갱신되는 높이 차를 구할 수 있음
        # 인덱스로 접근
        max_high = box_high[0]
        min_high = box_high[0]
        max_idx = 0
        min_idx = 0

        for i in range(100): # 상자가 놓여진 가로 길이를 순회 (가로 길이는 항상 100이므로 0~99(100화)반복)
            # 할당된 max_high보다 더 큰 값이 등장하면 갱신
            if max_high < box_high[i]:
                max_high = box_high[i]
                max_idx = i
            # 할당된 min_high보다 더 작은 값이 등장하면 갱신
            if min_high > box_high[i]:
                min_high = box_high[i]
                min_idx = i

        # dump 횟수가 완료 전에 평탄화 완료되면 break
        # = 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내
        if max_high - min_high <= 1:
            break

        # for문 순회 끝나면 인덱스를 사용해서 box_high를 덤프 작업
        box_high[max_idx] -= 1
        box_high[min_idx] += 1

    # 마지막 덤프 후 최대값과 최소값을 계산하여 결과 출력
    # (덤프를 순회하는) for문에서 나오면 낙차값을 재계산하여 정확도 높이기
    max_high = box_high[0]
    min_high = box_high[0]
    for i in range(1, 100):
        if max_high < box_high[i]:
            max_high = box_high[i]
        if min_high > box_high[i]:
            min_high = box_high[i]

    # 낙차값 구하기
    result = max_high - min_high
    print(f"#{tc} {result}")
