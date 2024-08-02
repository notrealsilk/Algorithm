# GNS

import sys
sys.stdin = open("GNS_test_input.txt", "r")

# 함수 :
def BubbleSort(word_len,num_list_order):
    global num_list
    word_len = int(word_len)
    for i in range(word_len):
        for j in range(0,(word_len)-i-1):
            if num_list.index(num_list_order[j]) > num_list.index(num_list_order[j+1]):
                num_list_order[j], num_list_order[j+1] = num_list_order[j+1], num_list_order[j]
    return num_list_order



# 기준이 되는 리스트
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# 테스트 케이스 입력 받고 변수 저장
T = int(input()) # 테스트 횟수

for i in range(1, T + 1):
    # tc = 테스트 케이스 횟수 / word_len = 단어 갯수
    # 다른 문제와 다르게 (#tc횟수 단어갯수) 형식으로 입력이 들어오니 주의!
    tc, word_len = input().split() # tc, word_len.. str 형식
    num_list_order = list(input().split())

    # 함수 호출
    result = BubbleSort(word_len,num_list_order)
    print(f"{tc} {result}")