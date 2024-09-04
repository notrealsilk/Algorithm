def babygin(player):
    counts = [0] * 10  # 0부터 9까지의 숫자 빈도를 셀 배열
    for num in player:
        counts[num] += 1

    # Triplet 확인
    for count in counts:
        if count >= 3:
            return True

    # Run 확인
    for i in range(8):  # 인덱스 에러 방지를 위해 0~7까지 체크
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            return True

    return False

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    player1 = []
    player2 = []
    winner = 0

    for i in range(6):
        # 플레이어 1이 카드 뽑기
        player1.append(arr[2 * i])
        if len(player1) >= 3 and babygin(player1):
            winner = 1
            break

        # 플레이어 2가 카드 뽑기
        player2.append(arr[2 * i + 1])
        if len(player2) >= 3 and babygin(player2):
            winner = 2
            break

    print(f"#{tc} {winner}")
