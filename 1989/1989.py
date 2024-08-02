# 1989. 초심자의 회문 검사

import sys
sys.stdin = open("input.txt", "r")

# 함수 Word_Check() : 파라미터로 입력된 단어가 회문인지 확인
# word.. 테스트 케이스 단어
def Word_Check(word):

# 반복문 돌면서 순서상 대칭에 있는 단어가 같은 문자인지 확인
    for i in range(len(word)):
        if word[i] != word[len(word)-i-1]: # 대칭이 되는 문자들이 같지않으면 0 반환
            return 0
        return 1 # 반복문을 성공적으로 다 돌면 1을 반환

# 테스트 케이스 반복횟수와 테스트 케이스 단어입력
# Word_Check()에 입력받은 단어를 넣어서 조건에 맞는지 확인
T = int(input())
for tc in range(1, T + 1):
    word = input()

    print(f"#{tc} {Word_Check(word)}")