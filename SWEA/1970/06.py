import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    coin = [0] * len(money)  # 거스름돈 총 8개
    cur_money = N  # 순회하면서 남은 돈 저장

    for i in range(len(coin)):
        coin[i] = cur_money // money[i]
        cur_money = cur_money % money[i]

    print(f"#{tc}")
    print(" ".join(map(str, coin)))  # join..리스트 안 문자열을 결합