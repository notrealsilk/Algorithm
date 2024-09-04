def solution(numbers, hand):
    key_pad = {1 :(0,0), 2:(0,1), 3:(0,2),
               4 :(1,0), 5:(1,1), 6:(1,2),
               7 :(2,0), 8:(2,1), 9:(2,2),
               '*' :(3,0), 0:(3,1), '#':(3,2)}

    left = key_pad['*'] # 왼손 현재 위치
    right = key_pad['#'] # 오른손 현재 위치
    answer = ''  # 사용한 손 (최종결과)

    for num in numbers :
        if num in [1,4,7]: # 왼손으로 누르기
            left = key_pad[num]
            answer += 'L'
        elif num in [3,6,9]: # 오른손으로 누르기
            right = key_pad[num]
            answer += 'R'
        else: # 2,5,8,0 이라면 어떤 손으로 누를 지 거리계산 시작
            # 1. 거리 계산
            left_distance = abs(left[0] - key_pad[num][0]) + abs(left[1] - key_pad[num][1])
            right_distance = abs(right[0] - key_pad[num][0]) + abs(right[1] - key_pad[num][1])

            if left_distance < right_distance:
                answer += "L"
                left = key_pad[num]
            elif right_distance < left_distance:
                answer += "R"
                right = key_pad[num]

            # 2. 거리가 같다면 손잡이 고려
            else:
                if hand == "left":
                    answer += "L"
                    left = key_pad[num]
                else:
                    answer += "R"
                    right = key_pad[num]

    return answer
