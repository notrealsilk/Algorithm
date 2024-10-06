import sys
sys.stdin = open("sample_input.txt", 'r')

def simulation(F, field, commands):
    # RC카 초기 설정
    position = (0, 0)  # 초기 위치 (X)
    direction = 0  # 초기 방향 -> 상(0)
    target = (0, 0)  # 목표 위치 (Y)

    # 초기 위치(X), 목표 위치(Y) 찾기
    for i in range(F):
        for j in range(F):
            if field[i][j] == 'X':
                position = (i, j)
            elif field[i][j] == 'Y':
                target = (i, j)

    # 상(0) 우(1) 하(2) 좌(3)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 최종 결과
    result = []

    for command in commands:
        length, moves = command
        # RC카의 위치 초기화
        cur_position = position
        cur_direction = direction

        # RC카 조정 시작
        for move in moves:
            if move == 'A':  # 앞으로 이동
                next_pos = (cur_position[0] + dir[cur_direction][0], cur_position[1] + dir[cur_direction][1])
                if 0 <= next_pos[0] < F and 0 <= next_pos[1] < F and field[next_pos[0]][next_pos[1]] != 'T':
                    cur_position = next_pos  # 이동
            elif move == 'L':  # 좌회전
                cur_direction = (cur_direction - 1) % 4
            elif move == 'R':  # 우회전
                cur_direction = (cur_direction + 1) % 4

        # 명령어 실행 후 위치 확인
        if cur_position == target:
            result.append(1)  # 도달 가능
        else:
            result.append(0)  # 도달 불가능

    return result

T = int(input())
for tc in range(1, T + 1):
    F = int(input())  # 필드 크기
    field = [list(input().strip()) for _ in range(F)]  # 필드
    Q = int(input())  # 명령어 개수
    commands = [input().split() for _ in range(Q)]  # 명령어 입력

    # 각 명령어의 길이를 정수로 변환
    commands = [(int(length), moves) for length, moves in commands]

    result = simulation(F, field, commands)
    print(f"#{tc} {' '.join(map(str, result))}")
