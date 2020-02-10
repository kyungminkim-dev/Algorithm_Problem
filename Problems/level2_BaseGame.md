#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/17687> #2018 KAKAO BLIND RECRUITMENT
---
```
def make_jin(n,num): #입력된 num을 진법에 맞게 변환하여 문자열로 바꾼뒤 반환한다.
    if num == 0:
        return '0'
    nj = ''
    if n <= 10:
        while num > 0:
            temp = str(num % n)
            nj += temp
            num = num // n
    else:
        while num > 0:
            temp = num % n
            if temp == 10:
                nj += 'A'
            elif temp == 11:
                nj += 'B'
            elif temp == 12:
                nj += 'C'
            elif temp == 13:
                nj += 'D'
            elif temp == 14:
                nj += 'E'
            elif temp == 15:
                nj += 'F'
            else:
                nj += str(temp)
            num = num // n
    return nj[::-1]
               
def solution(n, t, m, p):
    answer = ''
    n_list = []
    flag = True
    num = 0
    while flag:
        k = make_jin(n,num)
        for i in k:
            n_list.append(i)
            if len(n_list) == t*m:
                flag = False
                break
        num += 1
    for j in range(t):
        answer += n_list[p - 1 + m * j]
    return answer
```
---
### 고찰
**이 문제를 풀때는 입력된 매개변수 n에 맞춰 주어진 숫자를 문자열로 반환하는 함수를 만들어 접근하였다. 주어진 t,m 값을 이용하여 t*m 만큼의 숫자를 리스트에 삽입하였다.**
**이후 n_list에서 문제 조건에 맞게 문자를 추출하여 정답을 만들어 내었다. 조건에 맞게 문자열을 찾는 부분에서 시간을 좀 많이쓴것같다.**
    
