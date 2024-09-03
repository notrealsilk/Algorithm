import sys
sys.stdin = open("sample_input.txt","r")

def babygin(player):
    # 뽑은 카드 정렬
    player.sort()
    # 베이비진 탐색
    for j in range(1,5):
        # run
        if player[j-1]-1 == player[j] == player[j+1]+1 :
            return True
        # triplet
        if player[j - 1] == player[j] == player[j + 1] :
            return True
    return False # 베이비진이 아니라면

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))

    player1 = []
    player2 = []

    # 플레이어1,2가 카드 뽑기
    for i in range(len(arr)//2):
        player1.append(arr[i*2])
        player2.append(arr[i*2+1])

    # 베이비진인지 확인
    p_1 = babygin(player1)
    p_2 = babygin(player2)

    # 승자 확인
    if p_1 == True:
        print(f"#{tc}", 1)
    elif p_2 == True:
        print(f"#{tc}", 2)
    else:
        print(f"#{tc}", 0)




