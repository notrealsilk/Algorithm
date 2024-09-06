def solution(p):
    # 1. 빈 문자열이면 반환
    if p == "":
        return p

    p_list = list(p)  # 리스트 형식으로 문자열 분리

    # 2. 올바른 괄호인지 확인
    if is_correct(p_list):
        return "".join(p_list)

    # 3. 올바른 괄호가 아니므로 u와 v로 분리
    u, v = split_str(p_list)

    # 4. u가 올바른 문자열이라면
    if is_correct(u):
        # 올바른 문자열 u를 그대로 두고, v를 재귀적으로 처리한 결과를 이어붙임
        return "".join(u) + solution("".join(v))
    else:
        # 올바르지 않은 문자열 u를 변환하여 새로운 문자열 생성
        answer = '('  # 빈 문자열에 열린 괄호 붙이기
        answer += solution("".join(v))  # v를 재귀적으로 처리한 결과 이어 붙이기
        answer += ')'  # 그 뒤에 닫힌 괄호 이어붙이기

        # u의 첫 번째와 마지막 문자를 제거하고 나머지 괄호를 뒤집음
        u = u[1:-1]  # 첫 번째와 마지막 문자 제거
        new_u = []
        for char in u:
            if char == '(':
                new_u.append(')')
            else:
                new_u.append('(')
        answer += "".join(new_u)  # 뒤집은 괄호 문자열을 추가

    return answer


def is_correct(p_list):
    """
    올바른 괄호 문자열인지 확인하는 함수
    """
    stack = []
    for char in p_list:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0  # 스택이 비었으면 올바른 괄호


def split_str(p_list):
    """
    문자열을 u, v로 분리하는 함수
    """
    cnt_open = 0
    cnt_close = 0

    for i in range(len(p_list)):
        if p_list[i] == "(":
            cnt_open += 1
        else:
            cnt_close += 1

        # 열린 괄호와 닫힌 괄호의 수가 같으면 균형잡힌 문자열
        if cnt_open == cnt_close:
            return p_list[:i + 1], p_list[i + 1:]  # 균형잡힌 부분을 u로, 나머지를 v로 분리
