import sys
sys.stdin = open("input.txt", "r")

# 1. 입력값 받기
T = 10
for tc in range(1, T+1):
    num = int(input())  # 계산식 길이
    cal = list(input()) # 계산식

    priority = {'+': 1, '*':2}
    stack = []  # 스택
    num_list = []  # 스택에서 나온 연산자, 피연산자 저장

# 2. 중위표현식  to 후위표현식
    # cal이 빌 때 까지 반복
    for cur1 in cal:

        ## 숫자면 num_list에 추가
        #if cur1.isdigit():
        if cur1 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num_list.append(int(cur1))  # 입력받은 숫자가 str이므로 int로 바꾸기

        ## 연산자
        elif cur1 == "+" or cur1 == '*':
            # 스택에 값이 있고, cur1연산자 우선순위가 스택에 있는 연산자보다 작아질 때까지 pop
            while stack and priority[stack[-1]] >= priority[cur1]:
                num_list.append(stack.pop())
            stack.append(cur1)

    # 스택에 남아있는 연산자 pop
    while stack:
        num_list.append(stack.pop())

    print(num_list)

# 3. 후위표현식 to 계산
    for cur2 in num_list:
        # 숫자면 stack에 넣기
        if cur2 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            stack.append(cur2)

        if cur2 == "+":
            # 스택에서 숫자 2개 stack에서 뽑기
            num2 = stack.pop()
            num1 = stack.pop()
            # 계산한 값을 다시 stack에 넣기
            stack.append(num1 + num2)


        if cur2 == "*":
            # 스택에서 숫자 2개 stack에서 뽑기
            num2 = stack.pop()
            num1 = stack.pop()

            # 계산한 값을 다시 stack에 넣기
            stack.append(num1 * num2)

    # 최종 결과값 스택에서 빼서 출력
    result = stack.pop()

    print(f"#{tc} {result}")