#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/42890>  #2019 KAKAO BLIND RECRUITMENT

---
```
from itertools import chain, combinations
def get_subset(iterable): #iterable에 포함되는 모든 원소들의 순서를 포함하지 않는 경우의 수를 구하여 list로 반환한다.
    return list(chain.from_iterable(combinations(iterable,r) for r in range(1,len(iterable)+1)))

def get_unique_subset(relation): #주어진 relation에서 unique한 경우를 찾아내아 list에 저장한다.
    subset_list = get_subset(list(range(len(relation[0]))))
    unique_list = []
    for i in subset_list:
        temp = set()
        for j in range(len(relation)):
            row = ''
            for k in i:
                row += relation[j][k] + '.'
            temp.add(row)
        if len(temp) == len(relation):
            unique_list.append(i)
    return unique_list

def solution(relation):
    unique_list = get_unique_subset(relation)
    answer_list = []
    for i in unique_list:
        temp = set(i)
        check = True
        for j in answer_list:
            if j.issubset(temp):
                check = False
                break
        if check:
            answer_list.append(temp)
    return len(answer_list)
```
---

### 고찰 
**이 문제를 통해 list원소들에 대한 순서가 없는(combination) 또는 순서가 있는(permutaion) 경우의 수를 찾는 방법을 배웠다.**
**알고리즘 문제를 많이 풀다보니 list원소의 경우의 수를 구해야하는 문제를 많이 접했는데 이 문제를 풀게 되어 많은 비슷한 문제를 해결할 수 있었다.**
**마지막 solution함수에서 issubset함수를 이용하여 후보키의 조건인 최소성을 만족하는 경우를 찾아내었다.**
