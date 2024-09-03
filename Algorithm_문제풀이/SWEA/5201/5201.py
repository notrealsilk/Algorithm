import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # N : 컨테이너 수 / M : 트럭 수
    wi = list(map(int, input().split())) # wi : N개 화물의 무게
    ti = list(map(int, input().split())) # ti : M개 트럭의 적재용량

    result = 0 # 옮겨진 무게 (최종 결과)
    
    # 정렬
    wi.sort(reverse=True)
    ti.sort(reverse=True)

    # 트럭을 기준으로 화물 무게 순회
    for i in range(len(ti)):
        n = 0 # N개 화물 순회
        while n < len(wi):
            if wi[n] <= ti[i]: # 트럭이 짐을 옮길 수 있으면
                result += wi[n] # 짐 추가
                wi.remove(wi[n]) # 옮겨진 화물은 삭제
                break
            n += 1

    print(f"#{tc} {result}")
