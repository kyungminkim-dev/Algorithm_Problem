# 문제

'''import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    flag = True
    for i in scoville:
        if i >= K:
            continue
        else:
            flag = False
            break
    if flag == True:
        return 0
    flag2 = True
    while flag2:
        if len(scoville) < 2:
            return -1
        new = 0
        new += heapq.heappop(scoville)
        new += 2 * heapq.heappop(scoville)
        heapq.heappush(scoville,new)
        answer += 1
        for i in scoville:
            if i >= K:
                flag2 = False
                continue
            else:
                flag2 = True
                break
    return answer 
'''
