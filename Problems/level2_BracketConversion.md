#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/60058> #2020 KAKAO BLIND RECRUITMENT
---
```
def splitString(p):
    r_count = 0
    l_count = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            l_count += 1
            u += p[i]
        else:
            r_count += 1
            u += p[i]
        if r_count == l_count:
            v = p[i+1:]
            break
    return u, v 

def solution(p):
    answer = ''
    if p == '':
        return p
    u, v = splitString(p)
    flag = True
    count = 0
    for i in u:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            flag = False 
            break
    if flag == True: #올바른 문자열이라면 
        return u + solution(v)
    else: 
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
    return answer
```
---
### 고찰
**이 문제는 재귀함수를 사용해서 푸는 문제이다. 주어진 문자열을 문제 조건에 맞게 분리하는 함수를 만든다. 이후 문제 조건에 맞게 따라 코드를 작성하면 되는데**
**u가 올바른 문자열일때 v에대해 재귀함수를 사용하고 올바른 문자열이 아닐때 v에대해서 재귀함수를 사용하는 부분이 있다. 올바른 문자열인지 아닌지 판별하는 방법은 
count 변수를 주어 '('이면 +1 , ')' 이면 -1을 하여 count가 음수가 되면 올바른 문자열이 아니라고 판별한다.**
