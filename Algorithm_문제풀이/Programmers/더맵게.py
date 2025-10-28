import heapq

def solution(scoville, K):
    answer = 0
    # 힙
    heapq.heapify(scoville) # 리스트 넣기

    # 섞을 수 있는 지 확인 (scoville이 존재 하거나, scoville 값이 K를 넘지 않아야 ㅇ)
    while scoville and scoville[0] < K:
        
        # 스코빌 지수를 K 이상으로 만들 수 없는 경우 (값이 1개만)
        if len(scoville) < 2:
            return -1
        
        # 드뎌 섞음
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_sco = first+2*second
        
        heapq.heappush(scoville, new_sco)
        answer+=1
        
    
    return answer
