import sys
sys.stdin = open("input.txt", "r")

# 함수 : 삼각형 크기 (N)을 입력하면 파스칼 삼각형을 만들어줌
def Pascal(N):
    # 배열 만들기
    # [1]을 기준으로 삼각형 배열을 만듦
    # for a in range(N):
    #     arr = [1] * (a+1)
    arr = [[1]*(a+1) for a in range(N)]

    for i in range(N): # 행 순회
        for j in range(1, i) : # 열 순회 (양 끝은 항상 1이므로 순회에서 제외)
            # [i][j]를 기준으로 자신(i)의 왼쪽 위와 오른쪽 위의 숫자를 가져와 합으로 갱신
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # 출력
    # arr 2차원 리스트 순회하면서 요소 출력
    for row in arr:
        for ele in row:
            print(ele, end = ' ') # 공백을 두면서 출력!
        print() # 내부 for문이 끝나면 줄바꿈

# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    # N : 삼각형 크기
    N = int(input())

    print(f"#{tc}")
    Pascal(N)
