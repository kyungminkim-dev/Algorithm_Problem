#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/12977>
---
```
from itertools import combinations
def solution(nums):
    answer = 0
    subset = list((combinations(nums,3)))
    for i in subset:
        temp = 0
        for j in range(len(i)):
            temp += i[j]
        count = 0
        for k in range(1,temp+1):
            if temp % k == 0:
                count += 1
        if count == 2:
            answer += 1
        
    return answer
```
---
### 고찰 
**이 문제를 풀게된 이유는 level2문제 치고는 맞춘 사람이 별로 없어서 어려운 문제라고 생각하고 풀게되었다. 근데 막상 풀어보니 코드도 짧고 간결한 문제였다.
itertools 라이브러리에서 combination모듈을 가져와 3개를 선택하는 경우의 수를 구한뒤 소수인지 아닌지 판별해주면 되었다.**

**다만 약간 거슬리는 부분은 채점할 때 시간이 1000ms가 넘어가는 테스트케이스가 있었는데 소수인지 판별하는 코드부분이 원시적이기 때문이라고 생각한다. 좀 더 빠른 방법을 생각해봐야겠다.**
