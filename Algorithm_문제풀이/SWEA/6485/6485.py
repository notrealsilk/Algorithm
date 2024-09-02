import sys
sys.stdin = open("s_input.txt", "r")

# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    # N..버스 노선 수
    N = int(input())

    # 버스 정류장 카운트 배열 (1~5000 정류장)
    bus_stop = [0] * 5001

    # N개의 버스 노선
    for _ in range(N):
        A, B = map(int, input().split())
        # A에서 B까지 모든 정류장을 다니므로, 해당 구간에 대해 카운트 +1
        for i in range(A, B + 1):  # A이상 B이하 이므로 B+1 구간을 해야함
            bus_stop[i] += 1

    # P개의 버스 정류장
    P = int(input())
    result = []
    for _ in range(P):
        C = int(input())
        result.append(bus_stop[C])  # C번 정류장의 값을 결과 리스트에 추가

    # 최종 결과 출력
    print(f"#{tc} {' '.join(map(str, result))}")
