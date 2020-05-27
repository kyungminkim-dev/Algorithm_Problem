def solution(key,lock):
    M = len(key)  #열쇠의 길이
    N = len(lock) #자물쇠의 길이
    keyList = [key] #key 리스트를 만들고 입력받은 키를 넣어둠. 나중에 90도, 180,도 ,270도 회전시키 키를 append함

    
    def init(M): #키의 길이와 같은 0으로 초기화된 res block을 만듦. ex) if M == 3 : [[0,0,0],[0,0,0],[0,0,0]] 
        res = []
        for i in range(M):
            temp = []
            for j in range(M):
                temp.append(0)
            res.append(temp)
        return res

    for i in range(3): #한개의 키를 90도 회전시켜 keyList안에 append한다 
        new_key = init(M)
        for p in range(M):
            for q in range(M):
                new_key[q][M-p-1] = key[-1][p][q] #90도 회전시키는 과정. -1은 90도 회전할때 항상 keyList의 마지막 key를 사용
        keyList.append(new_key)


    def padding(lock,M,N): #lock에 zero padding을 붙인 리스트를 반환
        width = N + 2 * (M - 1)  # 최종리스트의 가로 길이 
        res = []
        for i in range(width):
            temp = []
            for j in range(width):
                temp.append(0)
            res.append(temp)
        
        for p in range(width):
            for q in range(width):
                res[p+M-1][q+M-1] = lock[p][q]
        return res
    
    def check(key,lock_padding):
        import copy 
        T = len(lock_padding)
        M = len(key)
        for gab1 in range(T-M+1): #lock_padding안에 키가 움직일수 있는 범위
            for gab2 in range(T-M+1):
                res = True
                cand_padding = copy.deepcopy(lock_padding) #lock_padding을 여러번 계산해야되므로 deepcopy 사용해서 복사
                for i in range(M):
                    for j in range(M):
                        cand_padding[i+gab1][j+gab2] += key[i][j] #lock 

                check_area = []
                for p in range(M-1,T-M+1): #lock_padding 안에있는 lock을 check_area로 옮김
                    temp = []
                    for q in range(M-1,T-M+1):
                        temp.append(cand_padding[p][q])
                    check_area.append(temp)
                
                for p in range(len(check_area)):
                    for q in range(len(check_area)):
                        if check_area[p][q] != 1:
                            res = False
                            break
                    if res == False:
                        break
                if res == True:
                    return res
                #else:    왜 else문을 return 하면 답이 달라지는가?
                #    return res # 답: else문으로 False를 return 하면 나머지 경우를 탐색을 안함True가 하나만 나오면 답은 성립하지만 False는 다시 끝까지 탑색해야함
        return False
    lock_padding = padding(lock,M,N)
    answer = False
    for i in range(4):
        cand_key = key[i]
        if check(cand_key,lock_padding) == True:
            return True
    return answer
                




     



