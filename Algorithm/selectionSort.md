#### 선택 정렬(selection sort)
- 선택정렬은 가장 단순한 정렬알고리즘으로 가장 작은 숫자를 탐색하여, 가장 왼쪽부터 바꾸어 나간다. 가장 작은 숫자를 선택하기 때문에 선택정렬 이라고 한다.
---
```
def selectionSort(arr): #오름차순 정렬
    for i in range(len(arr)-1):  
        minIndex = i              
        for j in range(i+1,len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j 
        arr[minIndex], arr[i] = arr[i], arr[minIdex]
    return arr
```
---
 
 선택 정렬의 시간 복잡도는 for문이 두 개 중첩되어 있으므로 O(N^2)이다. 선택 정렬의 시간 복잡도는 arr에 포함된 원소들과는 상관없이 
 arr의 크키 N에 의해서만 결정되므로 최악의 경우와 최선의 경우의 시간복잡도는 O(N^2)으로 같다.
