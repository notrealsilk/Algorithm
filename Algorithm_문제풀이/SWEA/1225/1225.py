import sys
sys.stdin = open("input.txt", "r")

# 입력값 받기
for _ in range(10):
    # 테스트 케이스 숫자를 횟수만큼 입력받기
    tc = int(input())
    # arr : 데이터 리스트
    arr = list(map(int, input().split()))

    # while문 : 조건 만족할 때까지 n사이클 돔
    # arr[-1]이 사이클을 돌면서 0보다 작아지거나 0일 경우, 멈춤
    # arr[-1]은 0이 되고, 해당 숫자 배열이 암호가 됨
    while arr[-1] > 0:
        # for문 : 5만큼 순회하면서 1사이클 돔
        for i in range(1,6):
            arr[0] -= i
            # 인덱스 0에 있는 숫자 pop해서 인덱스 맨 끝에 append
            arr.append(arr.pop(0))
            if arr[-1] <= 0:
                arr[-1] = 0
                break

    print(f"#{tc}", *arr)