from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    pointSet = [i for i in range(11)]
    
    reComSet = combinations_with_replacement(pointSet,n)
    maxSubPoint = -1
    
    for recom in reComSet:
        temp = [0] * 11
        lionPoint = 0
        apeachPoint = 0
        for i in recom:
            temp[i] += 1
        
        for i in range(11):
            if temp[i] > info[i]:
                lionPoint += 10 - i
            elif temp[i] < info[i]:
                apeachPoint += 10 - i
            elif (temp[i] != 0) and (temp[i] == info[i]):  #이 조건을 빼먹음 
                apeachPoint += 10 - i
        if lionPoint > apeachPoint:
            if maxSubPoint < (lionPoint - apeachPoint):
                maxSubPoint = lionPoint - apeachPoint
                answer = temp
            elif maxSubPoint == (lionPoint - apeachPoint):
                for i in range(10,-1,-1):
                    if temp[i] > answer[i]:
                        answer = temp
                        break
                    elif temp[i] < answer[i]:
                        break
                    else:
                        continue
    return answer