# T = int(input())
#
# for _ in range(T):
#     strings = input()
#     stack=[] # 스택
#     q=-1 # 스택 좌표 현위치
#
#     for s in strings:
#         if s == '(' and 0<=q and stack[q] == ')':
#             stack.pop()
#             q -= 1
#         elif s == ')' and 0<=q and stack[q] == '(':
#             stack.pop()
#             q -= 1
#         else:
#             stack.append(s)
#             q += 1
#
#     if len(stack) == 0:
#         print('YES')
#     else:
#         print('NO')

T = int(input())

for _ in range(T):
    strings = input()
    stack=[] # 스택
    flag = True # 플래그

    for s in strings:
        if s == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif s == '(':
            stack.append(s)
        else:
            flag = False # 위의 조건에 부합 x -> not VPS -> 더 이상 볼 가치도 없음
            break

    if not stack and flag: # 스택이 비어있고, 플래그가 T를 유지하고 있다면
        print('YES')
    else:
        print('NO')
