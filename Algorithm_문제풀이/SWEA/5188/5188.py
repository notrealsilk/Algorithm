import sys
sys.stdin = open("sample_input.txt","r")

def route (x, y, cur_sum):
    """
    :param x: 현 시점의 x 좌표
    :param y: 현 시점의 y 좌표
    :param cur_sum: 현재까지 지나온 길에 있던 숫자 합계
    :return: 기저조건 만나면 종료
    """
    global min_sum
    # 기저 조건
    if x == N-1 and y == N-1: # 맨 오른쪽 아래에 도착했다면
        min_sum = min(min_sum,cur_sum) # 지금까지 이동한 구간의 합이 최솟값이라면 갱신
        return

    # x축 이동
    if x+1 < N : # 인덱스 범위 벗어나지 않게
        route(x+1, y, cur_sum+arr[x+1][y])
    # y축 이동
    if y+1 < N : # 인덱스 범위 벗어나지 않게
        route(x, y+1, cur_sum+arr[x][y+1])

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N : 가로 세로 칸 수
    arr = [list(map(int,input().split())) for _ in range(N)] # arr : NxN 숫자판

    min_sum = 2000 # min_sum : 숫자 합계의 최소 (최종결과)

    route(0,0,arr[0][0]) # x좌표, y좌표, 현재 좌표의 숫자

    print(f"#{tc} {min_sum}")


