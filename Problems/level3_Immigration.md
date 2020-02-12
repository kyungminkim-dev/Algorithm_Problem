#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/43238>
---
```
def solution(n,times):
    answer = 0
    lo = 1
    hi = max(times) * n
    while lo <= hi:
        mid = (lo + hi) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break
        if people >= n:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer
```
---
### 고찰
**이 문제는 이진탐색과 관련된 문제이다. 모든 사람이 입국심사를 마칠때의 최소시간을 구하는 문제인데 최악의 경우 가장 오래걸리는 심사관에게 모든사람이 심사를 받는 시간을 구한다.**
**이후 이진탐색을 이용해 mid의 시간일때 모든 심사관이 심사할수 있는 사람의 수를 구한다. 그 수가 심사해야할 사람의 수인 n보다 크면 hi를 mid-1로 두어 구간을 줄이고**
**n보다 작다면 lo를 mid+1 두어 구간을 줄인다. 이 과정을 lo <= hi일때까지 반복하여 최단시간을 찾아낸다.**
