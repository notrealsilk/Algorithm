T = int(input())
for tc in range(1, T+1):
    N = float(input()) # N : 0보다 크고 1미만인 십진수

    n = 1
    i = 1
    result = ""
    while N > 0 :
        if i == 13 : # 13자리 이상이 필요한 경우
            result = "overflow"
            break

        if N - (n/2) >= 0:
            N -= (n/2)
            result += "1"
        else:
            result += "0"

        n /= 2
        i += 1 # 해당 순회 끝나면 다음 순회로

    print(f"#{tc} {result}")






