#### 문제 <https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3>
---
```
def solution(arr1, arr2):
    answer = []
    transarr2 = list(zip(*arr2))
    for i in range(len(arr1)):
        temp = []
        for j in range(len(transarr2)):
            tempsum = 0
            for k in range(len(transarr2[j])):
                tempsum = tempsum + arr1[i][k] * transarr2[j][k]
            temp.append(tempsum)
        answer.append(temp)
    return answer
```
---
### 고찰 
이 문제는 행렬의 곱을 구하는 문제이다. 주어진 문제의 행렬은 행렬의 곱이 가능한 경우만 주어진다. 그러므로 arr1의 열과 arr2의 행의 개수는 같다.

arr2의 행과 열을 zip함수를 사용해서 바꾸어준다. 이후 첫번째 for문을 통해 arr1의 행을 순서대로 가져온다. 가져온 행을 arr2의 행과 componentwise하게 곱한다.

곱한 결과를 차례대로 temp에 넣어주고 temp를 answer리스트에 넣어주면 답이 구해진다. 






