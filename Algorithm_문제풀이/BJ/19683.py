import heapq

giant_cnt, centi_hei, cnt = map(int, input().split())  # 거인 인구수 / 센티 키 / 뿅망치 횟수
giant_heis = [int(input()) for _ in range(giant_cnt)]

# 파이썬 heapq 최소힙 -> 음수로 넣어서 최대힙으로 사용
heap = []
for h in giant_heis:
    heapq.heappush(heap, -h) # 최대힙

r_cnt = 0  # 실제 사용 뿅망치 횟수

while cnt > 0:
    tallest = -heap[0]

    # 종료 조건 (센티가 더 큼 or 키가 1)
    if tallest < centi_hei or tallest == 1:
        break

    # 뿅망치 뿅
    new_h = tallest // 2

    heapq.heappop(heap)  # 최댓값 제거
    heapq.heappush(heap, -new_h)
    # heapq.heapreplace(heap, -new_h) # 더 빠름

    r_cnt += 1
    cnt -= 1

# 결과
fin_tallest = -heap[0]
if fin_tallest < centi_hei:
    print('YES')
    print(r_cnt)
else:
    print('NO')
    print(fin_tallest)
