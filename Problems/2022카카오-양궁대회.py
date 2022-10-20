''' 
중복조합으로 풀었습니다. 
라이언이 n번 화살을 쐈을 때, 맞힐 수 있는 점수의 모든 경우의 수를 구한 뒤, 완전탐색으로 점수의 차가 가장 큰 경우를 조건에 맞게 출력합니다.
'''

from itertools import combinations_with_replacement  # 중복순열을 구하는 모듈을 호출합니다. 

def solution(n, info):
    answer = [-1] # 라이언이 이길 수 없는 경우에 [-1]을 return하게 하기 위해 세팅했습니다.
    pointSet = [i for i in range(11)] # 양궁의 모든 점수를 리스트에 담았습니다.
    
    reComSet = combinations_with_replacement(pointSet,n)  # 라이언이 가질 수 있는 점수의 중복순열 경우의 수의 집합을 구합니다.
    maxSubPoint = -1  # 어피치와 라이언의 점수의 차를 구합니다. 이 변수가 가장 클 때의 경우가 정답입니다.
    
    for recom in reComSet: # 중복순열 경우의 수를 하나씩 탐색합니다. 
        temp = [0] * 11 # 라이언이 가질 수 있는 점수 경우입니다. 주어진 info 처럼 라이언의 점수가 저장됩니다.
        lionPoint = 0 # 라이언의 양궁점수입니다.
        apeachPoint = 0 # 어피치의 양궁점수입니다.
        for i in recom: # 경우의 수를 탐색하며 라이언의 양궁점수를 표현합니다. ex) [2,1,0,0,0,1,0,0,0,0,0]
            temp[i] += 1
        
        for i in range(11):  # 0점부터 10점까지를 탐색합니다. 
            if temp[i] > info[i]: #라이언의 점수가 어피치의 점수보다 클 경우 라이언의 점수가 추가됩니다. 리스트의 0번째가 10번째이므로 10-i를 하여 점수를 추가합니다.
                lionPoint += 10 - i
            elif temp[i] < info[i]:
                apeachPoint += 10 - i
            elif (temp[i] != 0) and (temp[i] == info[i]):  ## 라이언과 어피치의 점수가 둘다 0이 아닐때, 어피치의 점수를 올려줍니다. 
                apeachPoint += 10 - i
        if lionPoint > apeachPoint: #라이언의 점수가 어피치의 점수보다 크고 그 점수차이가 과거의 점수차이보다 클 경우 정답과 점수차이를 갱신합니다.
            if maxSubPoint < (lionPoint - apeachPoint):
                maxSubPoint = lionPoint - apeachPoint
                answer = temp
            elif maxSubPoint == (lionPoint - apeachPoint): # 점수의 차이가 같을 경우, 가장 낮은 점수를 가장 많이 맞춘경우를 정답으로합니다.
                for i in range(10,-1,-1):
                    if temp[i] > answer[i]:
                        answer = temp
                        break
                    elif temp[i] < answer[i]:
                        break
                    else:
                        continue
    return answer