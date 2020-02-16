#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/17686> #2018 KAKAO BLIND RECRUITMENT
---
```
import re
def solution(files):
    temp = [re.split("([0-9]+)",s) for s in files]
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))    
    answer = ["".join(s) for s in temp]
    return answer
```
---
### 고찰
**이 문제는 파이썬의 re모듈을 이용하면 쉽게 풀리는 문제이다. re모듈의 split함수를 이용하여 숫자를 기준으로 head,number,tail을 나눈다.**
**이후 sorted함수와 lambda를 이용하여 소문자로 변환한 head를 기준으로 정렬하고, 같은 head가 있으면 그 안에서 number를 기준으로 두번째 정렬을 한다.**
**마지막으로 join을 이용하여 리스트 안에있는 원소들을 결합하여 반환한다.**
