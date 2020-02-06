#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/42626>

---
```
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    flag = True         
    for i in scoville:   #처음 주어진 scoville리스트의 원소가 모두 K보다 큰 경우 0을 반환
        if i >= K:
            continue
        else:
            flag = False
            break
    if flag == True:
        return 0
        
    flag2 = True
    while flag2:
        if len(scoville) < 2:  #scoville의 원소가 2보다 작으면 K보다 커질 수 없으므로 -1을 반환
            return -1
        new = 0
        new += heapq.heappop(scoville)
        new += 2 * heapq.heappop(scoville)
        heapq.heappush(scoville,new)
        answer += 1
        for i in scoville:
            if i >= K:
                flag2 = False
                continue
            else:
                flag2 = True
                break
    return answer 
```
---

### 고찰
**문제를 처음 풀었을때는 python내장 모듈인 heapq를 사용하지 않고 list를 사용하여 풀었다. 그랬더니 효율성 부분에서 전부 틀리고 말았다. 그 때부터 더 효율적인 자료구조를 찾다가 힙(heap)이라는것을 발견했다. 구글에 python heap을 검색해서 공부한 뒤 코드를 수정하니 효율성 테스트케이스 5문제를 모두 통과하게 되었다. 
최소힙은 새로운 값을 힙에 추가하였을 때 자동으로 정렬이 되어 list에서 새로운 값을 추가 할 때마다 정렬을 해주는 과정을 없앨 수 있었다.**
