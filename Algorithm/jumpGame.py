t = int(input())
answerList = []
for i in range(t):
    n = int(input())
    board = []
    for j in range(n):
        temp = list(map(int,input().split()))
        board.append(temp)

    cache = [[-1 for i in range(n)]for j in range(n)]

    def jump(y,x,cache):
        if y >= n or x >= n:
            return 0
        if y == n-1 and x == n-1:
            return 1
        ret = cache[y][x]
        if ret != -1:
            return ret 
        jumpSize = board[y][x]
        ret = jump(y+jumpSize,x,cache) or jump(y,x+jumpSize,cache)
        cache[y][x] = ret
        return ret

    answer = jump(0,0,cache)
    if answer == 1:
        answerList.append("YES")
    else:
        answerList.append("NO")

for i in answerList:
    print(i)



        
    