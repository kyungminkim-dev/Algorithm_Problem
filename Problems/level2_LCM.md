#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/12953>
---
```
def solution(arr):
    answer = 0
    arr = sorted(arr)
    max_num = max(arr)
    n = 1
    flag = True
    while flag:
        flag2 = True
        for i in range(len(arr)-1):
            if n * max_num % arr[i] == 0:
                continue
            else:
                flag2 = False
                break
        if flag2 == False:
            n += 1
        else:
            answer = n * max_num
            return answer
```
---
### 고찰
**이 문제는 주어진 리스트안에 숫자들의 최소공배수를 구하는 문제이다. 보통 최소공배수는 2개의 숫자에서 구하는데 이문제는 리스트안에있는 모든숫자들의 최소공배수를 구하는 문제이다.**
**먼저 주어진 리스트를 정렬한뒤, 리스트안에 있는 원소중 가장 큰수에 1부터 곱해나가면서 가장 큰 수를 제외한 나머지 원소들이 max_num * n 을 나누는지를 알아내어 문제를 풀었다.**
**모든 원소들이 max_num * n을 나누면 그때의 max_num * n이 최소공배수임을 알 수 있다.**
