#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/60057> #2020 KAKAO BLIND RECRUITMENT 

---
```
def solution(s):
    if len(s) <3:
        return len(s)
    answer  = len(s)
    for interval in range(1,int(n/2)+1):
        start = interval
        res = []
        pre_s = s[0:interval]
        num=1
        while True:
            now_s=s[start:start+interval]
            if now_s==pre_s:
                num+=1
            else:
                res.append([num,pre_s])
                num=1
                pre_s = now_s
            
            if start > len(s):
                break
            start += interval
        len_cand = 0
        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand += len(res[k][1])
            else:
                len_cand += len(str(res[k][0]))
                len_cand += len(res[k][1])
        answer = min(answer,len_cand)
    return answer
```
---

### 고찰
**이문제는 2020카카오 공채 1번문제이다.**
**문자열압축 단위를 하나씩 늘려나가 압축률이 제일 좋은단위의 길이를 반환하는 문제이다. 압축단위 크기의 최대값은 전체 문자열 길이의 절반인 것을 이용한다. for문을 이용해서 각 압축단위마다 압축길이를 구하여 list에 저장하고 가장 작은 값은 반환한다.**
