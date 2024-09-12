# SSAFY에 간 임스
"""
5
stack 1
heap 2
queue 2
bfs 3
dijkstra 5
"""

tem_list = []
sort_solv = [] # 정렬된 문제 저장 (최종 결과)

N = int(input()) # 문제수
for i in range(N):
    solv, level = input().split() # 문제, 등급
    level = int(level) # 등급은 숫자형으로 변환

    tem_list.append([level,solv])

# sort() : 각 요소의 첫 번째 원소를 기준으로 오름차순 정렬
# 첫 번째 원소들이 동일하다면, 두 번째 원소를 비교하여 정렬 (사전순 정렬)
tem_list.sort() # 정렬

# 출력
for j in range(N):
    print(tem_list[j][1])