# n! 구현

# 반복
def factorial_1(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀
def factorial_2(n):
    # 종료조건
    if n <= 1:
        return 1
    return n * factorial_2(n-1)

print(factorial_1(5),factorial_2(5)) # 120, 120
