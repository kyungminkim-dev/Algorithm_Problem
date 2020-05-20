#풀이 : banned_id 리스트의 크기만큼 user_id 리스트에서 순서에 상관있게 뽑음(permutaions사용, 조합사용x)
#가능한 리스트를 match 함수를 이용해 추출
#추출한 가능한 아이디들은 전부 이어붙인다음 중복을 제거해서 갯수를 셈


from itertools import permutations 
def match(uid,bid): #user_id와 banned_id를 비교하여 match가 가능하면 True를 반환 ex) uid="frodo" ,bid="f*odo" : True 
    if len(uid) != len(bid): #길이가 다르면 애초에 성립불가이므로 False반환
        return False
    else: #길이가 같다면 각 글자마다 비교해서 가능한지 확인
        for i in range(len(uid)): 
            if uid[i] != bid[i] and bid[i] != '*': #uid와 bid의 글자가 다르고 bid가 "*"가 아니라면 가능하지 않은 아이디이므로 False반환
                return False
            else:
                continue
    return True 
            
            
def solution(user_id, banned_id):
    answer = 0
    answerList = []
    poslist = list(permutations(user_id,len(banned_id))) #user_id리스트에서 banned_id의 길이만큼 가능한 경우의 수를 구함 
    for i in poslist: #각 경우를 확인함 
        flag = True
        for j in range(len(i)):
            if match(i[j],banned_id[j]) == False:
                flag = False
                break
        if flag == False:
            continue
        else:
            answerList.append(i)
    for i in range(len(answerList)): #answerList의 원소들은 sort함. 나중에 중복을 제거하기 위해서 sort를 해야함. 안하면 중복된 원소를 가지게됨
        answerList[i] = sorted(answerList[i])

    for i in range(len(answerList)): #각 원소들은 tuple이므로 tuple의 원소들을 이어붙여줌
        answerList[i] = ''.join(answerList[i])

    answer=len(set(answerList)) #마지막으로 answerList에 set함수를 취해 중복을 제거함. 중복이 제거된 집합의 길이를 구하면 답.
    return answer